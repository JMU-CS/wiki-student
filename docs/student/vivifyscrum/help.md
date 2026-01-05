===== Help Using the Scrum Board in VivifyScrum =====

This page contains information about how to use the Scrum board in VivifyScru,.


==== Configuring the Scrum Board ====

To configure the Scrum Board, click on {{student:vivifyscrum:vivifyscrum_configure.png}} on the left-side menu.


==== Working with the Backlog Items ====


=== Adding a Product Backlog Item ===

The product backlog will typically be the left-most column of the board and will be labeled "Backlog". To add a product backlog item (PBI):

  - Hover the mouse over the bottom of the "Backlog" title bar until a <key>+</key> appears.
  - Click on the <key>+</key>.
  - Enter a title for the item.
  - Click on <key>SAVE</key>.

After you have added the item you should set its type by clicking on the the drop-down menu on the top left of the card.
    
=== Entering Value and Effort Estimates ===  

To provide an effort estimate for a backlog item:

  - Click on {{student:vivifyscrum:vivifyscrum_effort.png}} at the bottom of the PBI.
  - Select a estimate of business value value from the "Value" dropdown.
  - Select an estimate of effort (measured in story points) from the "Points" dropdown.

Depending on how the board is configured, it will either display just the effort estimate or the ratio of value to effort.

=== Adding Subitems ===

To add a subitem to an item (e.g., a task to a story):

  - Click on {{student:vivifyscrum:vivifyscrum_subitem.png}} at the bottom of the item.
  - Pull down to "Create Subitem".
  - Enter a title.
  - Click on <key>SAVE</key>.

Subitems will have a {{student:vivifyscrum:vivifyscrum_parentitem.png}} icon that you can click on to go to the associated parent item.

=== Adding Checklists ===

To add a checklist to an item (of any kind):

  - Click on {{student:vivifyscrum:vivifyscrum_checklist.png}} at the bottom of the item.
  - Pull down to "+ Add Checklist".
  - Enter a description of the checklist item.
  - Press <key>Enter</key>.
  - Continue until all of the checklist items have been entered.

Note that VivifyScrum allows an item to have multiple checklists though it is not [[ student:vivifyscrum:practices | standard practice ]] to do so.

=== Adding Assignees and Reviewers ===

To add assignees and/or reviewers to an item (of any kind):

  - Click on {{student:vivifyscrum:vivifyscrum_manageperformers.png}} at the top of the item.
  - Select the appropriate tab.
  - Search for the appropriate individual.

Note that VivifyScrum allows story to have assignees and a task to have reviewers though it is not [[ student:vivifyscrum:practices | standard practice ]] to do so.



==== Sprint Planning ====

Sprint Planning involves the following steps.
  - On the right side of the board (midway down the board), click on <key>+</key> (and name it Sprint #, where # is replaced by the appropriate number).
  - Chose which PBIs you want to do in this sprint and drag them from the PBI column to the Sprint # column (i.e., to the sprint backlog).
  - Add a checklist to each feature (sprintable story) in the sprint backlog that contains the acceptance criteria.
  - Decompose each feature (sprintable story) in the sprint backlog into subitems, where each subitem corresponds to a task. You can name tasks with phrases and they do not need to be user stories. You should mark subitems as tasks using the drop-down menu on the top left of the card.
  - Enter an effort estimate for each task. While it is a good idea to estimate stories in story points and tasks in hours, this isn't possible in Vivify Scrum, so you will have to use story points for task estimates as well. Note that when you associate items with subitems, the parent item shows how many story points there are in the subitems along with the estimate for the item. When you make all the subitems for an item, these numbers should match. If they  don't. then change the item or subitem estimates until they do. The idea is to use the tasks, which are smaller and hence easier to estimate, to improve your estimates for features and so to ensure that you have a reasonable collection of items in the sprint backlog.
  - Add items, such as overhead items, to the sprint backlog.  Pay specific attention to overhead items that are not associated with a particular PBI (e.g., grooming the product backlog).
  - Have team members take responsibility for tasks (and record the information in the tasks by editing the "assignees").
  - When the team is happy with the stories and tasks in the sprint backlog, click on the menu drop-down to the right of the sprint name and choose <key>Start Sprint</key>. Note: Make sure the dates are correct. This will add a <key>Sprint Backlog</key> item to the left-side menu (that can be used to go to the task board).
      
It is often useful to filter both the product backlog and the sprint backlog
while planning. You can filter based on assignee, type, priority, etc...
using the {{student:vivifyscrum:vivifyscrum_filter.png}} button.
  

==== Sprinting ====

As the sprint progresses, each team member should move their assigned tasks through the task board as they go. If a team member decides to work on an unassigned task, he or she should assign themselves to it - must be no tasks in the in-progress or done columns of the task board that do not have someone assigned to them.

  
When a feature is complete, a reviewer should go through its checklist and make sure that all the completion criteria are satisfied (this could be part of some other task or a task on its own).
  

==== Deleting a Board ====

Only the Owner can delete a board. To do so, first Archive it. Then, on "My Boards", click on <key>Delete</key>.
  