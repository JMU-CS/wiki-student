# Visual Paradigm for UML

## Colors, Fonts, etc...

The format of an individual element can be changed by right-clicking on the element and pulling down to "Styles and Formatting...".

After selecting particular values you can either:

- Change only the selected object by clicking on "OK".
- Change the class of objects by clicking on "Set as Default" and pulling down to "Set as Default for *Class*".
- Change all objects by clicking on "Set as Default" and pulling down to "Set as Default for all Shapes".

If you change a default, you will be asked whether you want this to be the default for current diagram or the whole project.

Be careful when setting defaults for all shapes. For example, if you set the background color of all shapes to white, initial nodes/states will be completely white.

## Changing Presented Information

To change the information that is included/presenetd in a diagram, right-click on the diagram then pull down to "Presentation Options" and over to the options you want to change.

## Finding Icons

Visual Paradigm "stacks" icons on top of each. If there is a small triangle on the bottom corner of an icon it means that icon can be "expanded" to see other similar icons. For example, in activity diagrams, the icons for merge, decision, fork and join are "stacked". As another example, in class diagrams, the icons for specialization and realization are "stacked".

## Finding Tabs

Visual Paradigm does not always show all of the tabs (presumably to reduce clutter). In such situations, you can click on an expansion icon to see a complete list.

## Exporting Diagrams

You may need to "export" diagrams from Visual Paradigm for many reasons and there are several ways to do so.

If you have a "PDF Printer Driver" installed then you can simply use it to print to a `.pdf` file (from the "Project" menu).

You can export an image file by clicking on "Export"-"Active Diagram as Image" and entering the name and type (e.g., `.jpg`, `.pdf`, `.png`).

If all else fails, you can use a screen capture utility and then either save the captured image or paste it into a word processing document.

## Activity Diagrams

### Activity Input/Output Parameters

The easiest way to add an input or output parameter to an activity, is to click on the Activity, move the mouse over to the icons that appear, and hover over the icons to get a description of what they do. One will allow you to add an output parameter and another will allow you to add an input parameter. Click on the appropriate one.

### Pins

To add a pin to an action, hover over the action -- this will cause icons to appear on the edge of the action. The pin icon is a small square with an arrow. Hover over the icon and a second icon will appear (one for adding an input pin and one for adding an output pin). Click on the appropriate icon to add the pin.

### Object/Data States

To add state information to an object node or pin, right-click on it and pull down to "Open Specification...". Then, click on the "InStates" tab and enter the relevant information.

Note that, depending on your presentation options, the states may or may not be displayed. See the discussion of "Changing Presented Information".

### Sub-Activities

To make a sub-activity (i.e., associate an action with a more detailed activity) right-click on an action and pull down to "Open Specification...". In the "Type:" field enter `Call Behavior Action`. Next to the "Behavior:" field enter, click on "...", select "Activity" and click on "New" or expand "Activity" and choose an existing activity diagram.

### Decision Nodes and Guards

To place a Guard on a Control Flow associated with a Decision node, right-click on the Control Flow and pull-down to "Guard".

### Fork and Join Nodes

To change the orientation of a fork/join node, right click on the node and pull down to "Orientation".

To change the colors of a fork/join node (e.g., to give it a solid background), right-click on the node, pull down to "Styles and Formatting" and then over to "Format".

## Class Diagrams

### Modifiers

Modifiers (e.g., `abstract`, visibility, `static`) can be set by right-clicking on the member and pulling down to "Open Specification...". Then, click on the "General" tab and enter the required information.

To make something `static`, set the "Scope:" to `classifier`.

### Raised Exceptions

To include thrown exceptions, right-click on the method and pull down to "Open Specification...". Then, select the "Raised Exceptions" tab and click on "Add". If the class of the exception is included in the model, select "Model..." otherwise select "Text...". Then enter the required information and click "OK". (Note: You may need to change the presentation options for the exceptions to be visible.)

### Fully Qualified Names

To display fully-qualified names (e.g. `java.lang.String` rather than `String`), right-click on the diagram, pull down to "Presentation Options", and over to "Type".

### The final Modifier

To indicate that a class is final, open the specification for the class and select "Leaf".

To indicate that an attribute is final, open the specification for the attribute and select "Read only". Then, open the presentation options for the class, click on "Attributes"+"Show Property Modifiers" and select "Yes".

## Sequence Diagrams

To change the information that is included in a Sequence Diagram, right-click on the diagram and pull down to "Presentation Options" and over to the appropriate item (e.g., "Lifeline", "Message", or "Activation").

To make a message asynchronous, right-click on the message, pull down to "Open Specification" and check "Asynchronous" on the "General" tab.

Sequence numbers can either be automated or entered manually. Simialrly, they can be hierarchical or not. To change the default, right-click on the diagram and pull down to "Sequence Numbers". If the sequence numbers get out of order they can be fixed (sometimes) by right-clicking on the diagram, pulling down to "Recalculate", and over to "Sequence Numbers".

To create a Combined Fragment, select the messages to cover, right-click on the selection, pull down to "Create Combined Fragment", and pull over to the type.

## Deployment Diagrams

To change the way an artifact is displayed, right-click on it, pull down to "Presentation Options" and over to the "ShowArtifactOption".

## Requirement Diagrams

### Editing Multi-line Text Fields

One way to edit multi-line text fields is to slect the field, right-click on the field, pull down to "Open Specification", and click on "..." next to the "Value" field.

### Customization

Requirement elements can be customized in a variety of different ways. To get started, click on the "Windows" menu, and then click on "Configuation" and pull-down to "Configure Requirements".

To edit an existing Requirement element, select it and change its attributes as appropriate.

To add a Requirement element (e.g., to allow for the creations of Stories in Scrum), click on the "Add" button that is underneath the list of Requirements and then enter an appropriate Name (e.g., Story). Then, click on the "Add" button underneath the attributes area to add an attribute.
