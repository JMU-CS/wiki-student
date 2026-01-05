# CS 149 Startup

This document will help you get your computer ready to go for CS 149. Setting up your own personal development environment and getting comfortable with all the tools you will use as a programmer takes time and experience. This document will walk you through the various tools you need and why you need them.

## Code Editor

The first thing you need for CS 149 is a Java code editor. Think of this as Microsoft Word for Java code. All sections of CS 149 in fall 2021 are using the jGRASP IDE. IDE stands for integrated development environment and is just a fancy term for a code editor (with a few extra bells and whistles).

jGRASP is very easy to download, install, and set-up (see how quickly [Dr. Bowers does it in this YouTube playlist](https://youtube.com/playlist?list=PLv0EaZTS9xfkQ-WqFGcO8zGgIs-2KThBY)). So that you do not also need to separately install a Java installation, we recommend you install the version of jGRASP that comes bundled with OpenJDK, which is the open source version of the Java development kit, as well as the Checkstyle and JUnit tools.

To download the jGRASP installer, navigate to [http://jgrasp.org](https://jgrasp.org), click the "Download" link on the left-hand menu, and scroll down until you see the gray box that begins with "jGRASP" followed by the version with the words "Bundled with OpenJDK" below it. There are three green buttons below this, "jGRASP Bundled exe", "jGRASP Bundled pkg", and "jGRASP Bundled zip". If you are using Windows, select the "exe" button. If you are on a Mac, select the "pkg" button. This will start the download for the proper installer.

Once the installer has completed downloading, run the installer and keep clicking "Next" until you are presented with a "Finish" button.

If you are on Windows you should now have a "jGRASP" shortcut on your desktop. If you are on a Mac, you will have the jGRASP app installed to your /Applications/ folder, which you can access from the Finder.

## Shell

The second thing you will need is access to a shell. If you've ever seen an old hacker movie from the '80s and seen the hacker hacking away at a black screen with green text, that's the shell. It's the old school text-based way of interacting with software on the computer. You may be surprised to learn that even now programmers use the shell! This is because text based control of the computer is often more convenient and more powerful (once you have learned how to use it), especially for lots of programming related tasks.

The good news is that you don't need to do anything to install a shell. Your computer already has one built in.

If you are on Windows, there are actually two that come pre-installed, but the one you should use is called the "Windows PowerShell". If you simply type "powershell" into the search bar on the start menu the Windows PowerShell app should be the Best Match.

If you are on the Mac, the shell can be used from within the Terminal app. This is stored in the /Applications/Utilities/ folder. You should also be able to find it quickly by typing "Terminal" into spotlight.

### Using the shell to access Autolab

Autolab is the software you will use to submit your code for programming assignments in CS 149. If you are on campus, or on the campus network, you simply go to <https://autolab.cs.jmu.edu> and log in with your EID.

Guides on using Autolab can be found [here](autolab/index.md).

Direct access to Autolab is blocked from off campus for security reasons. In order to access Autolab from off campus you must either [install and run the VPN](vpn.md) or you must create an SSH tunnel through the shell. This sounds really complicated and fancy, but is actually fairly straightforward. To do this simply run the following command in your shell but make sure to replace "your-username" with your actual username:

`ssh -L 4443:autolab.cs.jmu.edu:443 your-username@stu.cs.jmu.edu`

Then log in using your EID password. This establishes what is called an SSH tunnel that routes traffic through your computer to our Autolab server through a connection to stu.cs.jmu.edu, which is the student server for computer science students.

Once you have done this, you can access Autolab by visiting <https://localhost:4443/> in a browser. Your browser will give you security warnings about this, because it will recognize that you are trying to connect to cs.autolab.jmu.edu but have in fact connected to localhost. In this case, this is ok, since localhost is just the name of your own computer and you are using the SSH tunnel you yourself have set up.
