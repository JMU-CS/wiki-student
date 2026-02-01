# Using Git with Eclipse

The Eclipse plugin that integrate Git with Eclipse is called EGit. For more information, see the [Egit User Guide](https://wiki.eclipse.org/EGit/User_Guide).

## Installation

EGit should have been installed when you installed Eclipse. If not, you can install it using any of the methods described on [the EGit downloads page](https://www.eclipse.org/egit/download/).

## Configuration

To configure Git, click on "Window+Preferences". Then, expand "Version Control", expand "Git", and click on "Configuration".

Since many Git servers use your email address for authentication, it is important that the `user.email` key exists and that the value is your email address. It's useful if the "user.name" key exists and that the value is your personal name (e.g., first name) followed by a space and your family name (e.g., last name).

You can edit an existing entry by clicking on it. You can add an entry by clicking on "Add Entry..." and then entering a key and value. Keys are hierarchical, with levels delimited by a `.` character (e.g., `user.email`).

## Opening the Git Perspective

Eclipse enables you to present and interact with the same project in a variety of different ways, each of which is called a "perspective". To enable the Git perspective, click on "Window+Perspective+OpenPerspective" and select "Git" (if it is available) or "Other...+Git".

## Creating a Local Repository

The easiest way to create a local repository is to:

1.  Open the [Git Perspective](#opening-the-git-perspective)
2.  Click on "Create a local Git repository" (or the icon for creating a Git repository).

Note that you should not put the repository under the directory containing the Eclipse workspace.

## Adding a Project to Version Control

A project should be added to version control only once. After that, files in the project can be added to version control individually (or in groups). To add a project to version control:

1.  [Create a local repository](#creating-a-local-repository) (if you have not already done so)
2.  Right-click on the project
3.  Pull down to "Team+Share"
4.  If asked to choose a code management system, click on "Git"
5.  Browse to the local repository to use (or create a local repository in the parent folder of the project)
6.  Click on "Finish"

The name of the local repository you are using for this project will now appear next to the name of the project. In addition, the icons on any directories/files in the project will change to indicate that they have not yet been committed.

If you look at the project directory (outside of Eclipse) you will see that it is now empty, and if you look at the
repository directory (again, outside of Eclipse) you will see that it now contains all of the directories and files that were in the project' directory.

## Ignoring Files

The easiest way to instruct Git to ignore files is to:

1.  Open the [Git Perspective](#opening-the-git-perspective)
2.  Click on the "Git Staging" tab
3.  Right-click on the file/directory
4.  Pull down to "Ignore"

You can also edit the `.gitignore` file (outside of Eclipse).

## Committing Files

The easiest way to instruct Git to commit files to the local repository is:

1.  Open the [Git Perspective](#opening-the-git-perspective)
2.  Click on the "Git Staging" tab
3.  Select the appropriate files in the "Unstaged Changes" list
4.  Click on "+"
5.  Enter a descriptive commit message
6.  Click on "Commit"

## Pushing a Repository for the First Time

The first time you push a local repository, you will be asked to provide several pieces of information.

For most common Git work flows, the "Remote name" should be `origin` (indicating that this is the location from which everyone pulls).

The "URI", "Host", "Protocol", and "Port" will vary with the Git host.

You will also be asked to provide a "User" and "Password" for that host. Because of recent security enhancements, you must enter your "Personal Access Token" in the "Password" field, not your GitHub password. (If you select "Store in Secure Store", Eclipse will save this information for you locally, and you will not need to provide it each time you push. Otherwise, you will need to authenticate yourself each time you push.)

## Cloning a Repository

The easiest way to clone a remote repository is to:

1.  Open the [Git Perspective](#opening-the-git-perspective).
2.  Click on "Clone a Git repository".
3.  Enter the "URI", "Host", "Repository path", and "Protocol".
4.  Enter your authentication information for the Git server. (Because of recent security enhancements, you must enter your "Personal Access Token" in the "Password" field, not your GitHub password.)
5.  Select the appropriate branch (probably the main branch, the name of which may vary but should be apparent from the context) and click on "Next".
6.  Enter the appropriate local directory for the "Destination", the appropriate "Remote name" (probably `origin`), and click "Finish".

At this point, you will have cloned the repository but you will not have any Eclipse projects. To import a project from the repository, while still in the Git Perspective you should:

1.  Right-click on the repository
2.  Select "Import Projects..."
3.  Select on the project(s) of interest
4.  Click on "Finish"

Note: Some versions of Eclipse/Egit have a defect that require you to close Eclipse at this point and re-start it.

## Responding to `non-fast-forward` Messages

If you attempt to push changes that weren't made to the most recent revision (which the system considers the "official revision") the you will receive a `non-fast-forward` message. To remedy the situation, you must retrieve the most recent central revision, resolve any conflicts that arise between it and your local revision, and then push the result (which will succeed because it only involves changes to the most recent revision). This can be accomplished in two different ways, using a merge or using a rebase. A merge is non-destructive (i.e., the existing branches are not changed in any way) whereas a rebase rewrites the project history. Both are started by right-clicking on the project, pulling down to "Team" and selecting "Pull..." (note the ..., there is a "Pull" option and a "Pull..." option, the former uses default settings).

You can then choose the option to use "When pulling", either "Merge", "Rebase", or "Rebase interactively". If you choose to rebase interactively, the system will take you through the conflicts one at a time. Then, if you are uncomfortable with (or don't understand) the textual conflict markers that are inserted into the code, you can right-click on the name of the file containing the conflict and select "Team+Merge tool" to open a side-by-side editor.

When you perform a pull with the rebase option, all of your commits are moved to the tip of the main branch. This eliminates the need for a merge commit every time someone needs to synchronize with the central repository. Hence,
it is often preferred by organizations that use a centralized workflow. When using an alternative workflow, the team should agree on when merges and rebases will be used. Opinions differ on which is better because rebasing keeps the history flat and clean whereas merging keeps everything.

## Icons/Decorations

Egit uses a variety of different icons/decorations to illustrate the state of files. They are described in the
[Egit User's Guide](https://wiki.eclipse.org/EGit/User_Guide/State)

## Summary of Common Git Commands

Most Git documentation assumes that you are issuing `git` commands within a shell. The following table summarizes how to execute these commands using Egit.

| `git` Command | EGit Equivalent                                                                        |
|---------------|----------------------------------------------------------------------------------------|
| `add`         | Right-click on the file and then "Team+Add to Index"                                   |
| `clone`       | Open the Git Perspective and click on ![Clone a Git Repository](eclipse_git-clone.png) |
| `commit`      | Right-click on the project/files and then "Team+Commit..."                             |
| `pull`        | Right-click on the project and then "Team+Pull"                                        |
| `push`        | Right-click on the project and then "Team+Push"                                        |

To add an entry to the `.gitignore` file, right-click on the file and then "Team+Ignore".

For more information, see the [Egit User's Guide](https://wiki.eclipse.org/EGit/User_Guide)

## Troubleshooting

1.  If you get an error related to your HttpConnection when you attempt to clone a repository, it may be because of the HTTP client you are using. To change it, open the Git Preferences dialog and change the HTTP client (e.g., from "Apache HTTP" to "Java Built-in HTTP"
