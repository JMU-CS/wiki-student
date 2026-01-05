# Using Subversion with Eclipse

There are two different Eclipse plugin that integrate Subversion (SVN)
with Eclipse, Subversive and Subclipse. They are very similar in many ways.

## Installation

There are two different ways to start the process of installing Subversive or Subclipse.

However, before you start note that **it may be difficult to install the SVN Connector on Windows machines running Eclipse Oxygen**. If this is your current environment then you have two options - install Eclipse Neon instead or figure out how to install the connector (which is available from Polarion.com) manually. (Bug report [518033](https://bugs.eclipse.org/bugs/show_bug.cgi?id=518033) may prove useful in this regard.)

### Starting the Process with the Eclipse Marketplace

To start the installation using the Eclipse Marketplace you should:

1.  Start Eclipse.
2.  Click on "Help"-"Eclipse Marketplace".
3.  Enter `Subversive` or `Subclipse` in the "Find:" textfield and click on the magnifying glass.
4.  Click on "Install".

### Starting the Process with the Installer

To start the installation using the installer you should:

1.  Start Eclipse.
2.  Click on "Help"-"Install New Software".
3.  In the "Work with" list, select the appropriate version of Eclipse.
4.  Expand the "Collaboration" node, and select the latest version of the "Subversive" or "Subclipse".
5.  Click on "Next" twice.

### After the Process is Completed

Regardless of how you start the process, after it is completed you should restart Eclipse.

If you are installing Subclipse, you may be prompted to install the SVN Connectors in a dialog box. **IF NOT AND YOU ARE USING SUBCLIPSE, YOU MUST FORCE THIS PROCESS MANUALLY AS FOLLOWS:** Click on "Preferences" (which may be under "Windows" or the main "Eclipse" menu), expand "Team", and click on "SVN". This should open the dialog box. If not, click on the "SVN Connector" tab, and click on "Get Connectors...". Then:

1.  Select an appropriate connector -- SVN Kit can be used on all platforms; Native JavaHL can only be used on Windows machines that have an `ssh` client. So, you should probably use SVN Kit. (Note: `stu` currently supports SVN 1.9.3, so any connector for 1.9.3 or lower should work, but you should probably use the most recent version lower than or equal to 1.9.3.)
2.  Click on "Finish".
3.  When the the next dialog box appears click on "Next".
4.  When the next dialog box appears click on "Next".
5.  When the next dialog appears check "I accept..." and click on "Finish". You may get a warning that says you are "installing software that contains unsigned content". You can ignore it and click "OK".
6.  Restart Eclipse.

You can change the SVN interface by clicking on "Preferences"-"Team"-"SVN" and selecting the "SVN interface" from the "Client:" drop-down list.

## Connecting to Subversion on stu

### Protocol

Some Subversions Repository Servers use `http` (or `https`) as the communications protocol. `stu` uses `ssh`.

### Identifying a Repository

1.  Learn the URL for the repository. (It is likely to be something like `%%svn+ssh://stu.cs.jmu.edu/cs/students/csXXX/SSYY/teamNN '' where XXX corresponds to the course number, SS corresponds to the semester [either fa or sp], YY corresponds to the year, and NN corresponds to the team number). **Note:** If you are using a computer (e.g., your personal computer) in which your username is not your JMU eID, you should insert ''eID@'' between ''//'' and ''stu%%` (where eID denotes your JMU eID).
2.  If you are not already, use the SVN perspective by clicking on "Window"-"Perspective"-"Open Perspective"-"Other", selecting "SVN Repository Exploring", and clicking on "OK".
3.  Click on ![toolbar button](eclipse_new-repository-location.gif).
4.  After the dialog box opens, enter the URL in the "URL:" field.
5.  Complete the process.

### Authentication

The plugin will need to authenticate with `stu` every time an operation is performed, and this can be quite inconvenient. There are two ways around this.

- You may (it varies with the plugin) be given the opportunity to "Save authentication" information in which case you will not be prompted for it in the future. In this case, you will be asked to create a central Eclipse password if you have not done so already.

- You can create an [SSH Key Pair](../utilities/start/keypairs.md) to avoid having to repeatedly enter authentication information. In this case, you will need to tell Eclipse to use your private key by clicking on "Preferences"-"General"-"Network Connections"-"SSH2" and entering the path and file name on the `General` tab.

In either case, **should not save your authentication information on a "public" machine**.

## Using the Plugin

The Subversive and Subclipse plugins enable you to execute SVN commands from within
Eclipse.

In general, you should use the *Language* (e.g., Java)
Browsing Perspective when working on
a project. The SVN Repository Exploring Perspective and Team
Synchronizing Perspective, while useful, can be confusing because
they provide information about the repository not about the (local
copy of the) project which is your real concern.

Also, remember that adding a file to a project does not necessarily
add the file to version control. That is, you sometimes want to add
files to a project and not put them in the repository. Hence, when you
add a file to a project, if you want it to be under version control
you will need to manually add it to version control (see below). The
*Language* Perspective will put a ? icon on files that aren't under version
control and a cylinder icon on files that are. A file that has been
changed (and saved) locally but not committed will have a \> character to the
left of its name. A file that has been changed but not saved locally will have
an \* character before it's name in the file tab (there will be no indicator
in the *Language* Perspective/Package Explorer).

### Add a Project to an Existing Repository

To add a project to an existing repository:

1.  Right-click on the appropriate project.
2.  Pull down to "Team" and over to "Share Project...".
3.  When the dialog box appears, select the appropriate repository type (i.e., SVN) and click on "Next".
4.  When the next dialog box appears, check "Use existing repository location", select the appropriate location, and click "Next".
5.  If prompted to choose a mode, select "Simple Mode". (Note: This will make it harder to create branches but easier to use the trunk.)
6.  Click on "Finish".

When the SVN window appears, enter a commit comment (like "Initial Commit") and click "OK".

### Add a File to Version Control

To add a file to version control:

1.  Right-click on the appropriate file.
2.  Pull down to "Team", over to "Add to Version Control" and click "OK".

### Check-Out

**Assuming you have already added one or more repository locations to
Subversive**, you can check-out a repository for the first time and
create a local/working copy in a few ways. One way is to:

1.  If you are not already, use the SVN perspective by clicking on "Window"-"Open Perspective"-"Other", selecting "SVN Repository Exploring", and clicking on "OK".
2.  Expand the appropriate repository.
3.  Right-click on the appropriate project.
4.  Pull down to "Check Out".

Another way is to:

1.  Click on "File"-"Import"-"SVN"-"Project From SVN".
2.  Select "Use existing repository", select the appropriate repository from the list, and click "Next".
3.  Add the project name to the end of the URL (since there may be more than one project in the repository) and click "Finish".
4.  Check "Check out as a project with the name specified", fill in the project name, and click "Finish".

### Update

To update your local working copy (from the repository):

1.  Right-click on the appropriate folder/file.
2.  Pull down to "Team" and then to "Update" or "Update to HEAD"

### Viewing/Resolving Conflicts

If you have any conflicts, when you perform an update
you will get a message like "One or more selected resources have
unresolved conflicts". You can see the conflicts in several different ways:

- Look at the text included in the working copy.
- Compare "Base from Working Copy".
- Use the "Team Synchronizing" perspective.

After you make the appropriate changes and save the file(s):

1.  Right-click on the file(s).
2.  Pull down to "Team" and then to "Mark as Merged" or "Mark as resolved" (to inform Eclipse to remove the conflict icon and to inform Subversive that it should allow the commit.
3.  Perform the commit.

You might also be interested in the video at
<https://www.youtube.com/watch?v=7MB6T9ewidI>

### Editing Conflicts

If you have any conflicts after you perform an update, you can edit them
as follows:

1.  Right-click on the file(s).
2.  Pull down to "Team" and then to "Edit Conflicts".
3.  Use the icons to move between conflicts and accept particular edits.

### Commit

To commit changes (to the repository):

1.  Right-click on the appropriate folder/file.
2.  Pull down to "Team" and then to "Commit".
3.  In the "Commit" window, Enter a descriptive comment and click "OK".

Note: Remember to follow the appropriate process when committing changes.
That is, perform an update before the commit (and resolve any conflicts,
if necessary).

### Other SVN Commands

To execute other SVN commands:

1.  Right-click on the appropriate folder/file.
2.  Pull down "Team" and then to the command of interest.

### Compare Versions of a File

To compare different versions of the same file:

1.  Right-click on the appropriate file.
2.  Pull down to "Compare with..." and over to the appropriate version.

For example, to see if anybody else has committed changes to
a file you are working on choose "Latest from repository".

You can then use the toolbar above the diff window to do many useful things.
You can use the buttons with left/right-arrow icons
to "Copy All from Left to Right",
"Copy All Non-Conflicting Changes from Right to Left",
"Copy Current Change from Left to Right",
"Copy Current Change from Right to Left", and move between
differences and changes. You can use the buttons with up/down-arrow
icons to move between the differences.

### Overwriting a Previously Committed Change

Sometimes two people have made conflicting changes to the same
file and the second person to commit needs to overwrite all of the
changes that were made by the first person to commit. Obviously,
the second person should carefully compare the two versions before
taking this action, but if it is necessary, the second person can:

1.  Right-click on the appropriate folder/file.
2.  Pull down to "Team" and then to "Mark as Merged" or "Mark as Resolved".

and then commit the folder/file.

### Add SVN Buttons to the Java Perspective

If you are issuing SVN commands frequently, you may want to add
buttons to the toolbar. To do so:

1.  Click on "Window"-"Perspective"-"Customize Perspective".
2.  Select the "Action Set Availability" tab and select "SVN".
3.  Click on the "Tool Bar Availability" tab and select "SVN" (and everything underneath it, if necessary).
4.  Click "OK".

### The Synchronize Perspective

In addition to the other perspectives, Eclipse has a
Synchronize Team Perspective that allows you to highlight and work
with the files that have been changed since your last update. To
access it click on
"Window"-"Open Perspective" and then find the
"Team Synchronizing" perspective (which may be under
"Other...".

Right-clicking on a folder/file in this perspective will give
you access to many common SVN commands.

### Commands in Subversion vs. Subversive

The following Subversion commands would normally be preceded by
`svn` and the plug-in commands would be initiated by
right-clicking on the file/folder.

| SVN Command | Plugin                                               |
|-------------|------------------------------------------------------|
| `add`       | "Team"-"Add to version Control..."                   |
| `checkout`  | "Import"                                             |
| `commit`    | "Team"-"Commit"                                      |
| `delete`    | "Delete"                                             |
| `diff`      | "Compare With"                                       |
| `resolve`   | "Team"-"Mark as Merged" or "Team"-"Mark as Resolved" |
| `propset`   | "Team"-"Set Property..."                             |
| `revert`    | "Team"-"Revert"                                      |
| `update`    | "Team"-"Update" or "Team"-"Update to HEAD"           |
