===== Web Browsers =====

Modern web browsers write a lock file to your home directory when launched to prevent multiple instances from running concurrently. These lock files can get left behind if a browser or computer is not shut down cleanly. When this happens the browser will report that it can't launch because another instance is already running. The fix is to remove the lock files from your home directory.

==== Lock File Locations ====

=== Firefox ===
  * ~/.mozilla/firefox/<profile_name>/lock
  * ~/.mozilla/firefox/<profile_name>/.parentlock

Where <profile_name> is a random 8 character string, usually ending in .default.

=== Chrome ===
  * ~/.config/google-chrome/default/SingletonLock