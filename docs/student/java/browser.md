# Opening An External WWW Browser

## The Basics

It is pretty easy to start a WWW browser from a Java application. The Desktop class in the java.awt package has a static method named getDesktop() that returns a Desktop object that can be used for this purpose. You just needs to construct a URI object (from the java.net package) and pass it to the Desktop object's browse() method. For example:

    Desktop desktop = Desktop.getDesktop();
    URI     uri     = new URI("http://www.jmu.edu/");

    desktop.browse(uri);

To read from the local file system you can use the file protocol rather than the http protocol.

## Converting URIs and URLs

URI objects and URL objects are closely related (and the distinction exists mostly for historical reasons). The URI class has a toURL() method that constructs a URL from a URI. Similarly, the URL class has a toURI() method that constructs a URI from a URL.
