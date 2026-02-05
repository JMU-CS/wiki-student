# JMU VPN

The JMU VPN endpoint is changing to Palo Alto GlobalProtect on January 6 2025. The existing Ivanti Secure Access client will stop working at that time.

## Windows and Mac

Download the VPN client from <https://gp.jmu.edu/>
Full documentation is available from the [IT Knowledge Base](https://jamesmadisonuniversity.rightanswers.com/portal/app/portlets/results/viewsolution.jsp?solutionid=241205140417860).

## Linux

Install the OpenConnect client from your distribution's repository then launch it from the terminal as root. For example in Mint or Ubuntu:

    # apt install openconnect
    # openconnect --protocol=gp gp.jmu.edu

Your distribution may have a package that integrates the VPN into your network management software. Search your OS repositories for openconnect related packages.

## Chrome OS

You can launch the VPN client for Chrome OS (i.e., Chromebooks **not** the Chrome browser) from the chrome web store at <https://chromewebstore.google.com/detail/globalprotect/nicidmbokaedpmoegdbcebhnchpegcdc>

Set the portal to `gp.jmu.edu`
