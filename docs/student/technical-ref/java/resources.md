# Using Resources in Java Programs

## Overview

One commonly wants to use icons, configuration files, and other kinds of resources in Java programs.
While there are many ways to do accomplish, doing it in a way that is portable requires some thought
because of the way different IDEs and deployment mechanisms (e.g., [.jar files](jar.md))
organize code.

## Icons

To easiest way to refer to icons in a portable fashion is to use a `URL` object (from the `java.net` package), and the easiest way to get the appropriate `URL` object is to use a `Class` object. For example, if you want to get the `URL` for a resource named `logo.png` that is in the `images` directory **under the top-level directory containing the class of the object referred to by `this`** then you would do the following:

``` java
URL url = this.getClass().getResource("images/logo.png").
```

You could then load it as follows:

``` java
ImageIcon icon = new ImageIcon(url);
```

## Resource Bundles

The static `getBundle()` method in the `ResourceBundle` class can be passed a `ClassLoader` that it will use to locate the resources. For example, if you want to get the `ResourceBundle` with the prefix `Strings` that is in the **top-level directory containing the class of the object referred to by `this`** then you would do the following:

``` java
ResourceBundle strings;
strings = ResourceBundle.getBundle("Strings", Locale.getDefault(), this.getClass().getClassLoader());
```

## Other Kinds of Resources

For other kinds of resources (e.g., configuration files), the easiest way to ensure that your code is portable is to use an `InputStream` object (from the `java.io` package) to refer to the resource and use a `Class` object to retrieve the appropriate `InputStream` object.

For example, if you want to get the `InputStream` for a text resource named `default.cfg` that is in the `configurations` directory **under the top-level directory containing the class of the object referred to by `this`** then you would do the following:

``` java
InputStream is = this.getClass().getResourceAsStream("configurations/config.txt").
```

You could then read the first line of this text resource as follows:

``` java
BufferedReader in = new BufferedReader(new InputStreamReader(is));
String   line = in.readLine();
```

## Copying Resources to a Temporary Directory

Sometimes it is necessary to copy resources from a .jar file to a temporary directory on the files system (e.g., if you want to load .html files that are in a .jar file into a browser). The following utility class can be used for this purpose.

``` java
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.FileSystem;
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Stream;

public class ResourceCopier {

    /**
     * Copy all of the files from a resources package to a temporary directory
     * on the file system (whether or not the code and resources are in a .jar
     * file or on the file system).
     * 
     * This implementation assumes the resource package is a subpackage of the
     * package that contains this class (though that can be changed_.
     * 
     * @param id The ID to use for the temporary directory
     * @param subdir The name of the subpackage that contains the resources
     * @return The Path of the temporary directory
     * @throws IOException If something goes wrong
     * @throws URISyntaxException If something goes wrong
     */
    public static Path copyResourcesToTemp(String id, String subdir)
            throws IOException, URISyntaxException {

        // Get the location of the ResourceCopier.class file
        String canonicalName = ResourceCopier.class.getName();
        String packageName = ResourceCopier.class.getPackageName();
        String className = canonicalName.substring(packageName.length()+1) + ".class";
        String thisLocation = ResourceCopier.class.getResource(className).toString();

        // Remove the file name from the location and create a URI
        int fileStart = thisLocation.indexOf(className);
        String rootURL = thisLocation.substring(0, fileStart);
        URI sourceURI = new URI(rootURL + subdir);

        // Get the Path for source files (whether in a .jar file or the file system)
        Path sourcePath;
        FileSystem fileSystem = null;
        if (sourceURI.getScheme().equals("jar")) {
            fileSystem = FileSystems.newFileSystem(sourceURI, new HashMap<String, Object>());
            sourcePath = fileSystem.getPath("/" + packageName + "/" + subdir);
        } else {
            sourcePath = Paths.get(sourceURI);
        }

        // Get a List of all of the files in the source Path
        Stream<Path> files = Files.list(sourcePath);
        List<Path> filesList = files.toList();

        // Create a temporary directory on the local file system
        Path temp = Files.createTempDirectory(id);
        Path destinationPath = Path.of(temp.toString());

        // Copy all of the files from the source Path to the temporary directory
        for (Path file : filesList) {
            Path targetFile = Path.of(destinationPath.toString(), file.getFileName().toString());
            Files.copy(file, targetFile);
        }

        files.close();
        if (fileSystem != null) fileSystem.close();

        return destinationPath;
    }
}
```

## Under the Hood

These technique use the `ClassLoader` infrastructure to retrieve resources from the `.jar` file. So, it is very important that you understand the relative locations of the resource and the object that you call `getClass()` on. A leading `/` will start at the root of the directory tree, but you still must understand where in the `.jar` file is the root. Omitting the leading `/`, on the other hand, will start at the location of the `.class` file of the object referred to by `this`.
