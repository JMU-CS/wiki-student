# Java Versions and Numbering Systems

Java was first released in 1995/1996 and has had many versions since then. The original versions were distributed as the Java Development Kit (JDK) and were numbered 1.0 and 1.1. The next few versions after that were distributed as Java 2 Standard Edition (J2SE) and were numbered 1.2-1.4. Starting with version 1.5, also called version 5, they were distributed as Java Standard Edition (Java SE) and were numbered 1.5/5 - 17 (and beyond).

`.class` files use a different versioning system, and have both a major and minor version. For example, J2SE v1.2 uses major version 46 and Java SE v17 uses major version 61 (as described, for example, on [Wikipedia](https://en.wikipedia.org/wiki/Java_class_file)).

If you are given a ".class" file and need to know its version (e.g., to determine if it will work with the version of the JVM that you are using), you can use the "javap" command from the command line. For example, on Linux/OSX:

javap -version \<i\>name\</i\>.class \| grep "major"

and on MS-Windows:

javap -version \<i\>name\</i\>.class \| findstr "major"
