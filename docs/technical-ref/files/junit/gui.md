# Testing Graphical User Interfaces with JUnit

There are some very sophisticated tools that can be used to test Java graphical user interfaces. However, one can accomplish a lot using JUnit and a few "tricks".

## Mouse and Keyboard (Low-Level) Events

Low-level mouse and keyboard events can be generated using a `java.awt.Robot()` object. Note that the component must be visible to use a `Robot`. Hence, it must be added to a top-level container that is, itself, visible. There are some important consequences of this:

1.  The testing must **not** be done in a "headless" environment (i.e., the testing must be conducted on a device that has a display and keyboard) or a virtual display and keyboard must be available (e.g., using 'Xvfb and the `run-xvfb` command in Unix).
2.  The top-level container must be disposed of (using `dispose()`) after the tests have been run (so that the event dispatch thread terminates).

Also, remember not to manually move the mouse or use the keyboard while the tests are being run!

## Button Presses

The `javax.swing.AbstractButton` class (which is specialized by the `javax.swing.JButton`, `javax.swing.JToggleButton`, and `Javax.swing.JMenuItem` classes) has a `doClick()` method that programmatically generates a button press.

## Text Events

Text components can be tested both directly and indirectly.

To test them directly, one can use a `Robot` object to move the cursor to the component, click the mouse (i.e., invoke `mousePress()` and `mouseRelease()` without moving the mouse in-between) to give the component the focus, and then invoke `keyPress()` and `keyRelease()`. One can move the cursor to the component using the information available from its `getBounds()` method (which returns relative coordinates) and converting them to screen coordinates using the `SwingUtilities.convertRectangle()` method.

To test them indirectly, one can use the `Document` object (the model in the sense of the model-view-controller pattern) associated with the text component, or the `setText()` method in the component itself.

## Other Components

Most other components can also be tested directly (using the techniques described in the section on text events) or indirectly (using the model associated with the component).

## An Example

This section contains an example of using JUnit to test a GUI component that responds to mouse events and button events.

### The GUI Component

``` java
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class ClickPanel extends JPanel implements ActionListener, MouseListener
{
  JButton resetButton;
  private int count;
  
  public ClickPanel()
  {
    super();
    reset();
    addMouseListener(this);
    
    resetButton = new JButton("Reset");
    resetButton.addActionListener(this);
    setLayout(new BorderLayout());
    add(resetButton, BorderLayout.SOUTH);
  }
  
  public void actionPerformed(ActionEvent e)
  {
    if (e.getActionCommand().equals("Reset")) reset();
  }
  
  public int getCount()
  {
    return count;
  }

  public void mouseClicked(MouseEvent e)
  {
    count++;
  }
  
  public void reset()
  {
    count = 0;
  }

  public void mouseEntered(MouseEvent e){ }
  public void mouseExited(MouseEvent e){ }
  public void mousePressed(MouseEvent e){ }
  public void mouseReleased(MouseEvent e){ }
}
```

### The JUnit Test

``` java
import static org.junit.jupiter.api.Assertions.*;

import java.awt.*;
import java.awt.event.InputEvent;

import javax.swing.*;
import org.junit.jupiter.api.Test;

class ClickPanelTest
{
  @Test
  void test() throws AWTException
  {
    ClickPanel panel = new ClickPanel();
    
    // Use a JWindow (rather than a JFrame) because it is unadorned
    JWindow window = new JWindow();
    JPanel contentPane = (JPanel)window.getContentPane();
    contentPane.setLayout(new BorderLayout());
    contentPane.add(panel, BorderLayout.CENTER);
    window.setSize(400, 400);
    window.setLocation(200, 200);
    window.setVisible(true);
    
    // Test mouse handling
    Robot robot = new Robot();
    robot.setAutoDelay(100);
    robot.setAutoWaitForIdle(true);
    
    robot.mouseMove(300, 300); // Absolute screen coordinates
    robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);
    assertEquals(0, panel.getCount());
    robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
    assertEquals(1, panel.getCount());
    
    robot.mouseMove(400, 400);
    robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);
    robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
    assertEquals(2, panel.getCount());

    robot.waitForIdle();
    
    // Test button handling
    panel.resetButton.doClick();
    assertEquals(0, panel.getCount());
    
    
    window.setVisible(false);
    window.dispose(); // So the event dispatch thread terminates
  }

}
```
