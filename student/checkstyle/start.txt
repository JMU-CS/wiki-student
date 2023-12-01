===== Checkstyle =====

  - [[ student:checkstyle:configuration-files | Configuration Files ]]
  - [[ student:checkstyle:common-defects | Common Defects ]]

===== Running Checkstyle from the Command Line =====

Checkstyle is a Java program contained in the Checkstyle JAR file. To run it on a single java file, use the following command format: 

<code>
java -jar <PATH TO CHECKSTYLE JAR> -c <PATH TO CHECKSTYLE CONFIGURATION XML> <PATH TO JAVA FILE>
</code>

For example, if using the ''checkstyle-9.1-all.jar'' version of Checkstyle on the Google configuration file ''google_checks.xml'' on the Java file ''HashTable.java'' all stored in current working directory, you would run: 

<code>
java -jar checkstyle-9.1-all.jar -c google_checks.xml HashTable.java
</code>