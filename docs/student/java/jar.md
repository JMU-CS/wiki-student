# The Java Archive Tool (jar)

## Overview

The `jar` tool can be used to bundle multiple files into a single file. JAR files typically contain the class files and resources (e.g., images) required by an application.

## Viewing the Contents of a JAR File

To view the contents of a JAR file:

<code>
jar tf *jar-file*
</code>

## Creating a JAR File

To create a JAR file:

<code>
jar cf *jar-file* *input-files*
</code>

where *input-files* can include `.class` files, packages, and resources of various kinds.

## Creating an Executable JAR File

You can create an executable JAR file by including a manifest that includes a `Main-Class:` directive. For more information, see the [tutorial](http://java.sun.com/docs/books/tutorial/deployment/jar/appman.html).

The manifest can include a `Class-Path` entry that can contain external class files and jar files. FOr more information, see the
[tutorial](https://docs.oracle.com/javase/tutorial/deployment/jar/downman.html).

## Running an Executable .jar File

You can run an executable .jar file from a command shell/terminal window as follows:

1.  Open a command shell/terminal window.
2.  Change the working directory to the directory that contains the `.jar` file (using the [cd command](https://ss64.com/))
3.  Execute the application as follows: `java -jar filename.jar`

You can also run an executable .jar file from a file explorer/finder by double-clicking on it. However, your associations and permissions must first be setup.

## Permissions and Executable .jar Files

Depending on your operating system, you may need to change the permissions of the executable `.jar` file (i.e., provide permission to execute). In most OSs this can be done from the command line (using the [chmod command](https://ss64.com/)) or from the GUI (in a variety of different ways).

## Associations and Executable .jar Files

You may also need to set the default manner in which it is "opened" (i.e., instruct the OS to used the Java runtime). This is sometimes also called the files "association" or "default program". From the command line: in MS Windows you can use `assoc`, in OS X you can edit `~/Library/Preferences/com.apple.LaunchServices.plist`, and in Linux you can edit `/usr/share/applications/defaults.list` From the GUI: in MS Windows you can click on "Start"+"Default Programs", in OS X you can right-click on the file and use "File"+"Get Info", and in Linux you can right-click and select "Properties".

## Testing an Executable .jar File that You Created

If you just click/double-click on an executable `.jar` file and the code throws an exception you (typically) won't see it. Hence, when testing it is often useful to run the application from the command line. To do so, see the relevant instructions above.

If you get a message like the following:

    Exception in thread "main" java.lang.UnsupportedClassVersionError
    The program has been compiled by a more recent version of the Java Runtime (class file version XX.0),
    this version of the Java Runtime only recognizes class file versions up to YY.0

it means that you need to update your version of Java. When doing so, you need to be careful because many systems have both the Java Runtime Environment (JRE) and the Java Development Kit (JDK) installed, and updating the one may not update the other. In Linux/OSX you can use `which java` and in MS-WIndows you can use `where java` to find the path to the Java interpreter. You can change the `path` environment variable (not the `classpath` environment variable) to change which Java interpreter is used (i.e., either the one installed with the JRE or the one installed with the JDK).

## Using Resources in a .jar File

You may want to include files other than `.class` files in a `.jar` file (e.g., images, configuration files, input files). Such files are often called resources. See the discussion of
[using resources](resources.md) for more information.

## Changing the Icon of Executable .jar Files

By default, executable `.jar` files use the Java icon.

To change the icon in OS X, copy the icon you want to use (using "Commmand"+"c"), right-click on the `.jar` file, pull down to "Get Info", click on the icon in the upper-left corner of the dialog box, and paste the icon (using "Command"+"v").

To change the icon in many Linux distributions, right-click on the `.jar` file, pull down to "Properties", click on the "Basic" tab, and then click-and-drag the icon you want to use to the icon in the upper-left corner of the dialog box.

In MS-Windows you can't change the icon of the `.jar` file directly. However, you can create a shortcut and change it's icon. To do so, right-click on the `.jar` file and pull down to "Create shortuct". Then, right-click on the shortcut, pull down to "Properties", click on the "Shortcut" tab, click on "Change Icon...", navigate to the `.ico` file, click on "OK", and click on "OK".

## For More Information

The jar tool is very powerful and has a number of capabilities that are not discussed here. For more information, see the [tutorial](https://docs.oracle.com/javase/tutorial/deployment/jar/).
