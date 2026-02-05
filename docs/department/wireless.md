# JMU-Official-Wireless

JMU IT has instructions for connecting to the `JMU-Official-Wireless` network from macOS and Windows here:

<https://www.jmu.edu/computing/internet-and-network/official-wireless.shtml>

If you're running Linux then use the following settings:

- **SSID:** JMU-Official-Wireless
- **Wireless security:** WPA & WPA2 Enterprise
- **Authentication:** Protected EAP (PEAP)
- **Anonymous identity:** \<leave blank\>
- **Domain:** \<leave blank\>
- **CA certificate:** /etc/ssl/certs/ca-certificates.crt
- **PEAP version:** Version 0
- **Inner authentication:** MSCHAPv2
- **Username:** \<your JMU e-ID\>
- **Password:** \<your JMU password\>

This should work on most Linux distributions though the path to the CA certificate file could be different or you may need to use a different one altogether.

## eduroam

For a more automated connection setup, you can use the `eduroam` SSID and the [eduroam CAT tool](https://cat.eduroam.org). Read the [JMU IT webpage](http://www.jmu.edu/computing/network/eduroam.shtml) for eduroam.

1.  Go to <https://cat.eduroam.org>
2.  Choose 'James Madison University'
3.  Download the Linux Installer
4.  Run the Python script that you receive
5.  Click **Ok**
6.  Click **Yes**
7.  Enter `eID@jmu.edu` where `eID` is your JMU e-ID.
8.  Enter your JMU e-ID password
9.  You may need to tell Mint to attempt to connect to eduroam

You will need to re-run this every time your password updates.

#### Android Access to JMU wifi

Note: some of these settings may differ slightly on different Android devices

1.  Click the Settings icon on your Android device
2.  Click Connections and click to turn on WiFi
3.  Go back to your Home screen and you will see Wi-Fi network available, click to Open Wi-Fi network available
4.  Select JMU-Official-Wireless and set the following settings:
    1.  EAP Method: PEAP
    2.  Identity: type in your eID
    3.  Password: enter your password
    4.  CA Certificate: Use System Certificates
    5.  Online Certificate Status: leave this as Don't Validate
    6.  Domain: jmu.edu
5.  Click Connect
