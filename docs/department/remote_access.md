# Remote Access to JMUCS Departmental Resources

See below for several options for accessing internal JMU and CS resources from off-campus.

## VPN

JMU IT maintains a VPN (virtual private network) that is available to everyone with an eID. This is one of the best options for accessing resources from off-campus, particularly web based resources like library journals and Autolab. Documentation on the Pulse Secure client for Windows and MacOS is available from [JMU IT](https://www.jmu.edu/computing/internet-and-network/pulse-secure.shtml). Instructions for Linux users are available [on the CS Wiki](../student/vpn.md).

## SSH

All JMUCS students have SSH access to our student server, `stu.cs.jmu.edu`. This is useful when you need access to a Linux environment but note that it is entirely command-line based. You can also jump through stu to reach internal Linux hosts like lab machines or the HPC cluster. See the article on [stu](../student/stu/index.md) for more information.

## SSHFS

SSHFS allows you to mount your JMUCS home directory locally on your computer. This is nice because it lets local tools like Eclipse or Visual Studio Code work with your files directly. See the [Mounting a Remote Filesystem Locally](../student/utilities/sshfs.md) article for more information.

## Tunneling traffic through Stu

This is mainly included as an option for when the VPN is overloaded or unavailable. You can forward traffic from your local web browser through stu to reach internal resources. See the article on [ssh port forwarding](../student/utilities/sshportforward.md) for more information.
