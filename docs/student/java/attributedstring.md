# Strings with Attributes in Java

Java has an `AttributedString` class that can be used to add attributes (e.g., bold, italics, superscripts) to individual characters in a `String`.

## Constructing an AttributedString

The easiest way to construct an `AttributedString` is to start with a traditional `String` and then add attributes. For example,
the following snippet will create an `AttributedString` in which the characters `in` will be plain and the character `2` will be in the superscript position:

    AttributedString text = new AttributedString("in2");
    text.addAttribute(TextAttribute.SUPERSCRIPT,
                                      TextAttribute.SUPERSCRIPT_SUPER, 2, 3);

## Rendering an AttributedString

Most GUI components do not support the rendering of `AttributedSTring` objects. Fortunately, it is easy to create one that does. For example:

    import java.awt.*;
    import java.text.*;
    import javax.swing.*;


    public class AttributedStringPanel extends JPanel
    {
      private static final long serialVersionUID = 1L;
      private AttributedString text;
      
      public AttributedStringPanel(AttributedString text)
      {
        setText(text);
      }
      
      public void setText(AttributedString text)
      {
        this.text = new AttributedString(text.getIterator());
      }
      
      @Override
      public void paint(Graphics g)
      {
        Graphics2D g2 = (Graphics2D)g;
        g2.drawString(text.getIterator(), 0, getSize().height);
      }

      @Override
      public Dimension getPreferredSize()
      {
        return new Dimension(100, 50);
      }
    }
