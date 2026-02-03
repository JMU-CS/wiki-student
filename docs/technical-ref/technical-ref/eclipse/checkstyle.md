# The Checkstyle Plugin for Eclipse

[Checkstyle](../checkstyle/index.md) is a static analysis tool. The Checkstyle plugin for Eclipse enables the use of Checkstyle from within [Eclipse](index.md).

## Installation

There are three different ways to install the Eclipse Checkstyle Plugin. They are described at the [Checkstyle Plugin site](http://eclipse-cs.sourceforge.net/#!/install). At the moment, the "Marketplace" seems to be the most reliable approach.

If none of the normal methods work, you may want to consider installing the plugin manually.
((The normal Checkstyle installation process was not working reliably at the start of the Fall 2018 semester. However, it was possible to install version 8.11 "manually". So, if you have problems with the normal installation process, you may want to try this.

In a WWW browser, go to:

[v8.11 Download Site](https://bintray.com/eclipse-cs/eclipse-cs/update-site-archive/8.11.0)

then right-click on the link named `net.sf.eclipsecs-updatesite_8.11.0.201807281521.zip` (underneath the word "Downloads") and save the `.zip` file to a convenient location.

Now start Eclipse and click on "Help"+"Install New Software". When the dialog box opens, click on "Add...". When the new dialog box opens, click on "Archive...", navigate to the `.zip` file that you saved earlier, and click on "OK". Then click on "Add" on the previous dialog.

To actually start the installation process, on the previous dialog select Checkstyle and click on "Next" or "Finish".))

## Enabling the Checkstyle Plugin

To enable the Checkstyle plugin for a particular project:

1.  Right-click on the project.
2.  Click on "Checkstyle" and "Activate Checkstyle". (Or, if there is no "Checkstyle" entry, click on "Properties" and then select "Checkstyle", check "Checkstyle active..." and click on "OK".)

## Loading a Checks File (Configuration File)

You can set the checks file for all of the projects in a workspace or for each project individually.
If you have a different workspace for each course then you should probably use the first approach,
which is described in the [page on installing Eclipse](install.md#install-and-use-a-custom-checks-configuration-file). If you use one workspace for all of your courses then you should probably use the second approach as follows:

1.  Download the file to an appropriate location on your local file system.
2.  In Eclipse, right-click on the project, and pull down to "Properties".
3.  Select "Checkstyle" and click on the "Local Check Configurations" tab.
4.  Click on "New".
5.  Select "External Configuration File", enter a "Name:" and the "Location:" of the file, and click "OK".
6.  Select the "Main" tab.
7.  Select the appropriate configuration file from the drop-down list.
8.  Click on "OK".
9.  When the "Rebuild suggested" dialog appears, click on "Yes".
