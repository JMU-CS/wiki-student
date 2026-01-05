===== Customizing the Appearance of the GUI =====


==== Overview ====

The appearance of Java GUIs can be customized in a variety of different ways.


==== Setting the Look and Feel ====

The easiest way to customize the appearance is to use an existing "look and feel".

To use the "system" look-and-feel (i.e., the look-and-feel that is most
consistent with the operating system), you can do the following:

<code java>
try
{
    UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
}
catch (Exception e)
{
    // Use the default
}
</code>

To use the "Nimbus" look-and-feel you can do the following:
 
<code java>
try
{
    UIManager.setLookAndFeel("com.sun.java.swing.plaf.nimbus.NimbusLookAndFeel");
}
catch (Exception e)
{
    // Use the default
}
</code>

Other L&Fs are also available, some that are distributed with the VM and some that are available from third parties.
