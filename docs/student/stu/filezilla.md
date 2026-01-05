# Transferring Files from Your JMU CS Account with FileZilla

1.  Install the [FileZilla client](https://filezilla-project.org/download.php?type=client)
2.  Open FileZilla
3.  If the Site Manager doesn't automatically open, click the icon in the top left of the FileZilla window (see \#1 in image) to open it
    - Main FileZilla Window
      ![Screenshot of FileZilla with circles around areas 1, 2, and 3](filezilla_-_main_window.png){width="800"}
        1. Site Manager button
        2. the files on the computer you're currently using (i.e. your laptop, called the "local" computer)
        3. the files on "stu" the JMU CS server that hosts your account (the computer that you're not currently using, but have connected to is the "remote" computer)
4. In the Site Manager window, click the New site button (annotated with the ellipse in the figure)
    * FileZilla Site Manager without info
      ![Site Manager dialog with "New Site" button circled](filezilla_-_site_manager_-_init.png){width="800"}
5. Name the site something that makes sense to you, while the server is named "stu" (an abbreviation for its fill name for "Student Bizzy Werkinit III"), perhaps that name doesn't mean much to you, so you can name it "jmucs" or "DoD" or whatever you want idc 💁
6. With your newly named site selected, make the following selections/entries for the fields in the right half of the Site Manager window:
    - Protocol: SFTP
    - Host: stu.cs.jmu.edu
    - Port: it's fine to leave this blank, probably it's 22 if you're just curious
    - Logon Type: Ask for Password
    - User: your EID (not capitalized, without the @dukes)
    - Your password will be the same as your EID passwords.
7. Confirm that your settings look like this, but with a different <del>crime against humanity! computers don't name people</del> EID
    * FileZilla Site Manager cheatsheet
      ![Site Manager dialog with protocol set to SFTP, host set to stu.cs.jmu.edu, and user set](filezilla_-_site_manager_-_configured.png){width="800"}
8. Click Connect
9. Now you can simply (?):
    * drag files from the left side of the screen to the right to "upload" ⬆️☁️ them from your laptop to "stu" 💻➡️☁️
    * drag files from the right half of the screen to the left to "download" ⬇️💻 them to your laptop from stu 💻⬅️☁️
