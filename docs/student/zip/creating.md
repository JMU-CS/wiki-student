# Creating a .zip File

## Using Linux

To create a `.zip` file from the File manager:

1.  Navigate to the appropriate directory/folder.
2.  Click on the first file or directory/folder to select it.
3.  Control-click on any other files or directories/folders to select them.
4.  Right-click on one of the selected files and pull down to "Compress...".
5.  Enter a filename (and location).
6.  Select ".zip".
7.  Click on "Create".

To create a `.zip` file from the command shell, you can use the following command:

<code>
zip *archive*.zip *file* \[*file*\]...
</code>

## Using MS Windows

To create a `.zip` file from the File Explorer:

1.  Navigate to the appropriate directory/folder.
2.  Click on the first file to or directory/folder to select it.
3.  Control-click on any other files or directories/folders to select them.
4.  Right-click on one of the selected files and pull down to "Send To" and pull down to "Compressed (zipped) Folder".

If the Java Development Kit is installed and in your PATH, you can also create a `.zip` file from the command shell using the following command:

<code>
jar -cvf *archive*.zip *file* \[*file*\]...
</code>

## Using OS X

To create a `.zip` file from the Finder:

1.  Navigate to the appropriate folder.
2.  Click on the first file or directory/folder to select it.
3.  Command-click on any other files or directories/folders to select them.
4.  Right-click (i.e., Ctrl-click) on one of the selected files and pull down to "Compress ... Items".

To create a `.zip` file from the command shell, you can use the following command:

<code>
zip *archive*.zip *file* \[*file*\]...
</code>

If the Java Development Kit is installed and in your PATH, you can also create a `.zip` file from the command shell using the following command:

<code>
jar -cvf *archive*.zip *file* \[*file*\]...
</code>

Note that if you use the GUI-based approach, the resulting `.zip` file will contain OSX-specific files (like `.DS_STORE`) and directories (like `__MACOSX`) that can cause problems in some situations. You can exclude files when working from the command line using the `-x` option. For example:

<code>
zip -r dir.zip . -x .* -x __MACOSX
</code>

will create a `dir.zip` that contains all of the directories below the current directory, but will exclude all files that start with a `.` and the `__MACOSX` directory.
