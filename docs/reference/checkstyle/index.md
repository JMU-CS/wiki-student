# Checkstyle

1.  [Configuration Files](configuration-files.md)
2.  [Common Defects](common-defects.md)

## Running Checkstyle from the Command Line

Checkstyle is a Java program contained in the Checkstyle JAR file. To run it on a single java file, use the following command format:

    java -jar <PATH TO CHECKSTYLE JAR> -c <PATH TO CHECKSTYLE CONFIGURATION XML> <PATH TO JAVA FILE>

For example, if using the `checkstyle-9.1-all.jar` version of Checkstyle on the Google configuration file `google_checks.xml` on the Java file `HashTable.java` all stored in current working directory, you would run:

    java -jar checkstyle-9.1-all.jar -c google_checks.xml HashTable.java
