===== Submitting Assignments Using Web-CAT =====

==== About Web-CAT ====

Web-CAT is an acronym for "Web-based Center for Automated Testing". It  is used at a number of universities for the electronic submission  and grading of programming assignments. It was developed at Virginia Tech.


==== Overview of the Submission Process ====

To submit as assignment using Web-CAT you must:

  - Compile your code off-line to ensure that it is syntactically correct.
  - Test your code off-line to try and ensure that it executes correctly.     (This is especially important if the number of submissions is limited     and/or penalties are imposed for "excessive" submissions.)  
  - Create a ''%%.zip%%'' file containing the source files (i.e., the ''%%.java%%'' files) to  be submitted.  
  - Open the [[ https://webcat.cs.jmu.edu/ | JMU CS Web-CAT ]] home page.  (Note: You may be re-directed to another page.)  
  - Login to Web-CAT (using your JMU eID and password).
  - Click on the appropriate <key>Submit</key> button (i.e.,  the <key>Submit</key> button for the assignment you are  submitting).
  - Browse to the ''%%.zip%%'' file that contains your source files  and click on <key>Upload Submission</key>.
  - Confirm that the correct files were uploaded and click on  <key>Confirm</key>.
  - Wait for the "Submission Results" report.
  - Review results and re-submit if necessary.
  - Logout.
Additional details are provided below.


==== Understanding Web-CAT Reports ====


Web-CAT analyzes your code in several different ways and provdes a "score"  for each. Do not confuse Web-CAT's score with your grade -- make sure you  read the course "Policies" page and understand how programming assignments  are graded.



=== Style/Coding ===

The Style/Coding score is based on your adherance to the course   style guide. The "Full Printable Report" contains detailed   information about the Style/Coding defects in your submission. In   general, each "Error Box" contains an "Expected" line that   describes the defect.

Note that you must include a blank line at the end of all of your   .java files so that Web-CAT is able to insert information about   Style/Coding defects.


=== Correctness/Testing ===


The Correctness/Testing score is based on the results of a suite   of unit tests. The summary page contains an "Estimate of Problem   Coverage". It is the percentage of unit tests that your submission   performed correctly on. In general, since the definition of a   unit test is somewhat arbitrary, the percentage itself is   difficult to interpret. In addition, this number does not   provide any information about the number of faults in your code,   just the number of trigger conditions that led to   failures. 


For some assignments, the bottom of the report may include hints   that can help you locate the faults. However, you should not   expect hints. If your code contains faults its is your   responsibility to test your code, identify the faults, and correct   them.


==== Interpreting Web-CAT Hints ====


The hints provided by Web-CAT are sometimes quite detailed and  clear, but this is not always the case, sometimes intentionally  (e.g., when it is your responsibility to test) and sometimes not  (e.g., because of limitations in HTML). Of coruse, tests that you  create and run locally will always provide you with much more  informative than Web-CAT hints.



=== Differences in White Space ===


Because Web-CAT uses HTML and HTML does not preserve white   space, some of the hints may be a little misleading. In other words,   a hint may provide you with an expected ''%%String%%'' and an   actual ''%%String%%'' that it claims (and, in fact) are different   but appear to be the same. In such cases, the defect is probably related to   white space (though it may be something else as well).


=== Expected Exceptions ===


When Web-CAT expects a method to throw an exception and it doesn't,   the hint will start with something like ''%%Expected exception: %%'',   will list the exception, and will list the number of occurrences.   In such cases, you will need to validate your code (i.e., check to make   sure that it satisfies all such specifications).
