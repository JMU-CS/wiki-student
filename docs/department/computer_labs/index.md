# Computer Labs

The Computer Science department maintains multiple computer labs running Ubuntu
Linux 26.04. Desktop machines may be accessed over the network. See the article
on [stu](../../reference/stu/basics.md) for more information. You are free to
use these labs whenever there is no class scheduled there. These labs are
located in:

1.  King 248 (where [TA Hours](../cs-success.md) are held)
2.  King 250
4.  EnGeo 2204

## Lab Hardware

| Location   | Type    | Qty | Description                                                                             |
|:-----------|:--------|-----|-----------------------------------------------------------------------------------------|
| King 224   | Laptop  | 22  | Dell Precision 5290, Intel Core Ultra 5 125H, 16GB RAM                                  |
| King 248   | Desktop | 31  | Dell Precision Workstation 3640, Intel Core i9-13900, 32GB RAM                          |
| King 250   | Desktop | 31  | Dell Precision Workstation 3660, Intel Core i9-12900, 32GB RAM, Nvidia RTX A2000 (12GB) |
| EnGeo 2204 | Desktop | 32  | Dell Precision Workstation 3460, Intel Core i9-12900, 32GB RAM                          |

## Lab Software

All labs have the same software, including but not limited to the following:

- Kernel 7.0.0
- Arduino IDE 2.3.10
- CUDA 13.2 / Nvidia 595 (King 250 only)
- Eclipse 2026-06
- Emacs 30.2
- GCC 15.2.0
- GHC 9.10.3
- Git 2.53.0
- Go 1.26.0
- IntelliJ IDEA 2026.1.3
- Java 25.0.3 (OpenJDK)
- Meld 3.22.3
- Mercurial 7.2
- Pandoc 3.7.0.2
- Processing 4.5.2-1313
- Prolog SWI-Prolog 9.2.9
- Python 3.14.4
- Ruby 3.3.8
- Rust 1.97.1 (Stu only)
- Sagemath 10.4 (Stu only)
- Sqlite 3.46.1
- Subversion 1.15.5
- Tcl/Tk 8.6.16
- Texlive 2025.20260124
- Thonny 4.1.7
- Vim 9.1
- Visual Paradigm 18.1
- Visual Studio Code 1.128.0
- VMware Workstation 26.0.0 (Desktops only)
- Zoom 7.1.0.3715

## Known Hosts

See below for the current `known_hosts` file for all JMUCS lab machines. You'll need to replace or merge it with your existing `~/.ssh/known_hosts`, removing any duplicate hosts.

[jmucs-known_hosts.txt](jmucs-known_hosts.txt) Last updated: 2026-08-11

## Student Account Home Directory

The `student` user's home directory is wiped at logout. The last 10 directories are archived locally on each machine at `/opt/student_homes/<YYYYMMDD_HH-MM-SS>.tar.gz`. Faculty can extract these archives by running `tar -xzvf <archive>`. Files can be copied to `/tmp` where students should be able to access them. You can also contact `cs-sysadmin@jmu.edu` for assistance. Please provide the hostname and approximate timestamp that you need recovered.

## Screen Recording for Demo Purposes

From the Linux Mint menu, launch `'Webcamoid`' to create a screen recording. Maybe the details in this wiki are correct for how to use the app: <https://github.com/webcamoid/webcamoid/wiki/Recording-videos>
