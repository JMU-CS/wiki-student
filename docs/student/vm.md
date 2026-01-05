===== Virtual Machine =====

For several years, the Unix Users Group (UUG) maintained a [[https://en.wikipedia.org/wiki/Virtual_machine|virtual machine]] (VM) that allows you to use a Linux-based operating system regardless of what operating system is on your computer. The virtual machine also came with a utility that automates the installation of software needed for various CS courses.

**The image is no longer actively maintained as of 2021.** The instructions on this page have been retained in case they have value in helping you to get other virtual machines working. If you would like assistance getting a VM working or would like to talk about the options available, please visit the Unix Users Group.

==== VM Instructions ====

First, you will need to download and install [[https://www.virtualbox.org/wiki/Downloads|VirtualBox]] if you do not already have it. Then, download the [[https://w3.cs.jmu.edu/uug/latest.ova|VM image]] (warning: it is a large file!) and double-click it to begin the setup process.

There is a [[https://w3.cs.jmu.edu/cs101/virtual/index.html|CS 101 tutorial]] about the setup process, and the UUG also maintains a [[https://www.jmunixusers.org/presentations/vm/welcome-to-vm.html|getting started guide]] and a [[https://www.jmunixusers.org/presentations/vm/common-troubleshooting.html|troubleshooting common problems guide]]. If you run into other issues or have questions, feel free to attend a UUG meeting (see the [[student:clubs:start|CS clubs page]] for dates and times).

If you are interested in seeing how the VM image is built or if you are interested in contributing, please visit the [[https://github.com/jmunixusers/cs-vm-build|project repository]] on Github.

**Note for M1 "Apple Silicon" Users:** Since these machines use completely different CPUs, they are incapable of running VirtualBox with the Linux Mint image. The UUG is attempting to make a compatible VM, but its a fast moving target that's difficult to fully test. Mint also isn't released for M1, so this VM uses Ubuntu with the same tools, but a different look than the lab machines. If you'd like to try running a Linux VM on your M1, first download a current version of [[https://github.com/utmapp/UTM/releases|UTM]], and then download the [[https://w3.cs.jmu.edu/uug/testing/|VM image]]. Please send any feedback, positive or negative to [[ripleymj@jmu.edu]].