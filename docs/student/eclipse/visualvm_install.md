====== Integrating the VisualVM Profiler with Eclipse ======

Note: These instructions assume that you have already [[student:java:profiling|downloaded and installed the VisualVM]].

===== Installing/Configuring the Plugin =====

  - Download the %%.zip%% file containing the plugin from [[http://visualvm.github.io/idesupport.html|the IDE integration page]].
  - Extract the %%.zip%% file to an appropriate location.
  - Start Eclipse.
  - Click on <key>Help</key>+<key>Install new software</key>.
  - Click on <key>Add...</key>, click on <key>Local...</key> and navigate to the directory/folder containing the extracted plugin.
  - Expand the tree and select "Visual VM Launcher Feature".
  - Click on <key>Next</key> and complete the installation.
  - Click on <key>Window>+<key>Preferences</key> or <key>Eclipse>+<key>Preferences</key> (depending on your OS), expand "Run/Debug", expand "Launching", and select "VisualVM Configuration".
  - Enter the path to the "VisualVM Executable" and, if necessary, the JDK (not the JRE) you are using.
  - Click on <key>Apply and Close</key>.


===== Using the Plugin =====

To run an application with the VisualVM you need to create a fun configuration for your project.

  - Select the project.
  - Click on <key>Run</key>+<key>Run Configurations...</key>.
  - Select "Java Application" and click on the new configuration button.
  - Enter an appropriate name (e.g., "Profile MyApplication").
  - Enter the name of the main class.
  - Next to the message about "Multiple launchers available", click on "Select one...", select "Use configuration specific settings", select "VisualVM Launcher", and click on <key>OK</key>.
  - Click on <key>Run</key>.

At this point, the application should start executing, the VisualVM should start executing, the appropriate application should be selected, and you should be able to begin profiling. For help, with profiling, see the page on [[student:java:profiling|profiling java programs]].