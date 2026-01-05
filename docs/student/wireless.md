===== JMU-Official-Wireless =====

JMU IT has instructions for connecting to the ''JMU-Official-Wireless'' network from macOS and Windows here:

[[https://www.jmu.edu/computing/internet-and-network/official-wireless.shtml]]

If you're running Linux then use the following settings:

  * **SSID:** JMU-Official-Wireless
  * **Wireless security:** WPA & WPA2 Enterprise
  * **Authentication:** Protected EAP (PEAP)
  * **Anonymous identity:** <leave blank>
  * **Domain:** <leave blank>
  * **CA certificate:** /etc/ssl/certs/ca-certificates.crt
  * **PEAP version:** Version 0
  * **Inner authentication:** MSCHAPv2
  * **Username:** <your JMU e-ID>
  * **Password:** <your JMU password>

This should work on most Linux distributions though the path to the CA certificate file could be different or you may need to use a different one altogether.

===== eduroam =====

For a more automated connection setup, you can use the ''eduroam'' SSID and the [[https://cat.eduroam.org|eduroam CAT tool]]. Read the [[http://www.jmu.edu/computing/network/eduroam.shtml|JMU IT webpage]] for eduroam. 

  - Go to [[https://cat.eduroam.org]]
  - Choose 'James Madison University'
  - Download the Linux Installer
  - Run the Python script that you receive
  - Click **Ok**
  - Click **Yes**
  - Enter ''eID@jmu.edu'' where ''eID'' is your JMU e-ID.
  - Enter your JMU e-ID password
  - You may need to tell Mint to attempt to connect to eduroam

You will need to re-run this every time your password updates. 

=== Android Access to JMU wifi ===

Note: some of these settings may differ slightly on different Android devices
		
  - Click the Settings icon on your Android device
  - Click Connections and click to turn on WiFi
  - Go back to your Home screen and you will see Wi-Fi network available, click to Open Wi-Fi network available
  - Select JMU-Official-Wireless and set the following settings:
    - EAP Method: PEAP
    - Identity: type in your eID
    - Password: enter your password
    - CA Certificate: Use System Certificates 
    - Online Certificate Status: leave this as Don't Validate
    - Domain: jmu.edu
  - Click Connect
