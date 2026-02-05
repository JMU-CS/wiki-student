# Integrating the VisualVM Profiler with Eclipse

Note: These instructions assume that you have already [downloaded and installed the VisualVM](../java/profiling.md).

## Installing/Configuring the Plugin

1.  Download the .zip file containing the plugin from [the IDE integration page](http://visualvm.github.io/idesupport.html).
2.  Extract the .zip file to an appropriate location.
3.  Start Eclipse.
4.  Click on "Help"+"Install new software".
5.  Click on "Add...", click on "Local..." and navigate to the directory/folder containing the extracted plugin.
6.  Expand the tree and select "Visual VM Launcher Feature".
7.  Click on "Next" and complete the installation.
8.  Click on "Window\>+"Preferences" or "Eclipse\>+"Preferences" (depending on your OS), expand "Run/Debug", expand "Launching", and select "VisualVM Configuration".
9.  Enter the path to the "VisualVM Executable" and, if necessary, the JDK (not the JRE) you are using.
10. Click on "Apply and Close".

## Using the Plugin

To run an application with the VisualVM you need to create a fun configuration for your project.

1.  Select the project.
2.  Click on "Run"+"Run Configurations...".
3.  Select "Java Application" and click on the new configuration button.
4.  Enter an appropriate name (e.g., "Profile MyApplication").
5.  Enter the name of the main class.
6.  Next to the message about "Multiple launchers available", click on "Select one...", select "Use configuration specific settings", select "VisualVM Launcher", and click on "OK".
7.  Click on "Run".

At this point, the application should start executing, the VisualVM should start executing, the appropriate application should be selected, and you should be able to begin profiling. For help, with profiling, see the page on [profiling java programs](../java/profiling.md).
