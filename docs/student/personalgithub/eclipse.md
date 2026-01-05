# GitHub for Personal Use with Eclipse

This page describes one way to use GitHub for personal use (whether you are working alone or with someone else) under Eclipse. It uses a different repository for each course.

**Note that individual courses that require the use of Git (e.g., CS345) may specify a different process and/or may not use GitHub.**

## For Each Course

For each course you must create a repository on GitHub using one machine. Then you must create the necessary directories/folders on each machine and clone the GitHub repository.

### Create a GitHub Repository From One Machine

- Open a WWW browser.
- Login to GitHub.
- Create a new repository for the course (e.g., with a repository name of ''cs999'').
- Click on ".gitignore template" and select "None".
- Click on "Create repository".
- Click on ".gitignore" in the Quick setup area to create such a file.
- Add the following to the file:

    # Byte Code #
    *.class

    # Eclipse #
    .settings/
    bin/
    tmp/
    .metadata
    .classpath
    .project
    *.tmp
    *.bak
    *.swp
    *~.nib
    local.properties
    .loadpath
    .factorypath
    .checkstyle

    # Log Files #
    *.log

    # OS X #
    .DS_Store

    # Package Files #
    *.jar
    *.war
    *.nar
    *.ear
    *.zip
    *.tar.gz
    *.rar

    # Virtual Machine Crash Logs (see http://www.java.com/en/download/help/error_hotspot.xml) #
    hs_err_pid*

Then, click on \[Commit new file\].

At this point you should also create a Personal Access Token (see `https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token`).

### Create the Necessary Directories/Folders on Each Machine

1.  Open a file explorer/finder/terminal.
2.  Create a directory/folder for the course (e.g., `/home/bernstdh/cs999`).
3.  Create a directory/folder for the Eclipse workspace for the course (e.g., `/home/bernstdh/cs999/eclipse`). **Don't use the course directory/folder**, create a sub directory/folder in the course directory/folder.
4.  Create a directory/folder for the Git repository for the course (e.g., `/home/bernstdh/cs999/git`). Again, **don't use the course directory/folder** (create a sub directory/folder in the course directory/folder), **don't use the workspace folder**, and **don't put the repository folder inside of the workspace folder**.

### Clone the GitHub Repository on Each Machine

1.  Start Eclipse. When asked for the workspace to use, browse to the directory/folder you just created for this purpose (e.g., `/home/bernstdh/cs999/eclipse`).
2.  Setup the workspace as needed (e.g., add a Checkstyle checks file, add a formatter).
3.  Open the Git Perspective.
4.  Click on "Clone a Git repository". When asked for the "Repository directory" to use, browse to the directory/folder you created for this purpose (e.g., `/home/bernstdh/cs999/git`).
5.  Enter the GitHub URI (e.g., `https://github.com/bernstdh/cs999`) in the "URI:" field.
6.  Enter your GitHub user name in the "User:" field.
7.  Enter your Personal Access Token in the "Password" field.
8.  Click on "Next\>".
9.  Select "main" if it isn't already.
10. Click on "Next\>".
11. Enter the name of the the directory/folder you created for the Git repository for this course (e.g.,`/home/bernstdh/cs999/git`) in the "Directory:" field. (Note: Be careful if you use the \[Browse\] button as it will add additional subdirectories. They won't break anything but they will make the directory structure more confusing.)
12. Make sure the "Remote name:" is origin.
13. Click in "Finish".

## For Each Eclipse Project in Each Course

For each Eclipse project in a course, you will create the project on one machine and push it to GitHub. The, you will import the project on every other machine.

### Create the Project On One Machine

1.  Start Eclipse.
2.  Open the "Java Perspective".
3.  Create the new project.
4.  Add the project to source control by right-clicking on the package name, pulling down to \[Team\] and across to \[Share project\]. Note: At this point, a directory/folder with the name of the project will be added to the workspace.
5.  Click on the "Repository:" dropdown and select the Git repository for this course (e.g., `/home/bernstdh/cs999/git`).
6.  Click on "Finish". Note: At this point, the directory/folder for the project will be moved from the worskapce directory/folder to the Git respoitory folder/directory.
7.  Commit and push.

### Import the Project On Other Machine(s)

1.  Start Eclipse.
2.  Open the Git Perspective.
3.  Expand the repository (e.g., `git`).
4.  Expand the "Working Tree".
5.  Right-click on the directory/folder icon for the project.
6.  Pull-down to "Import Projects...".
7.  Click on "Finish".
