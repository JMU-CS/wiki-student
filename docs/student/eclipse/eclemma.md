# The EclEmma Code Coverage Tool for Eclipse

## Overview

EclEmma is a Java code coverage tool for Eclipse that is based on [JaCoCo](http://www.eclemma.org/jacoco/).

## Launching EclEmma

Eclipse supports a variety of different *launch modes* (e.g., for running applications, for debugging applications, ...). If EclEmma is installed, the workbench should include a button that looks like ![Coverage Mode](eclemma_coverage-mode.gif) for launching in EclEmma coverage mode. (Note: If this button is not visible, click on "Window"-"Perspective"-"CustomizePerspective", expand the "Launch" item, check "Coverage", and click "OK".) Expanding this button allows you to launch EclEmma.

## Selecting the Type of Coverage

To select the type of coverage

1.  Expand the ![Coverage Mode](eclemma_coverage-mode.gif) button and pull down to "Coverage As".
2.  Select the appropriate type of coverage.

## Creating a Coverage Report

Once you have selected the type of coverage, you can create a coverage report by clicking on ![toolbar button](eclemma_coverage-mode.gif). The coverage report will be available in the "Coverage" tab of the Output View. (Note: If there is no "Coverage" tab you can enable it by clicking on "Window"-"Show View".) This report provides a summary of the instructions covered by your tests (which is comparable to statement coverage).

**More importantly**, each source file will be [marked-up](http://www.eclemma.org/userdoc/annotations.html) to indicate which statements, branches, etc... have been covered and which have not. (This is far more valuable and important than the coverage report.)

Note that EclEmma uses the term "branch" differently from the way some other people use the term. In EclEmma, the number of "branches" is the sum of the number of possible Boolean values in an expression. So, a statement like: `if ((x > 0) || (y > 0) || (z > 0))` will have $2 + 2 + 2 = 6$ "branches". Some people say this statement has 2 "branches" (the entire expression is either true or false, leading to 2 edges in the graph), $2 \times 3 = 6$ "conditions", and $2^3 = 8$ "multiple conditions".

## Removing the Highlighting

To remove the highlighting from a coverage report, click on ![Coverage Mode](eclemma_remove-all-sessions.gif) in the "Coverage" view.

## Running an Entire Test Suite

It is generally a good idea to create an individual JUnit tets for each class (and sometimes for individual methods within a class). However, when generating a coverage report you want to run all of the tests in the suite. To do so, click on the triangle on ![Coverage Mode](eclemma_coverage-mode.gif) and pull down to "Coverage configurations...". Then, select a JUnit test and click on "Run all tests in the selected project, package, or folder" and click on "Coverage".

## Different versions of JUnit

It's possible to have different versions of JUnit installed within Eclipse at the same time. To use a particular test runner click on the triangle on ![Coverage Mode](eclemma_coverage-mode.gif) and pull down to "Coverage configurations...". Then, select a "Test runner" and click on "Apply".

Note that your tests must then be consistent with the test runner. So, for example, if you are using Version 4 then: all test classes must be public, all test methods must be public, and you must include the classes in the package `org.junit`.

## Resolving Some Situations that May Arise

EclEmma is very powerful but has some quirks that may lead to reports that confuse you.

### Coverage of Enumerated Types

Because of the way EclEmma works, in order to get 100% coverage of an `enum` you must test the static `valueOf(String)` method. To do so, include a test like the following.

``` java
    @Test
    public void valueOfTest()
    {
     assertSame("valueOf(DECEMBER)", 
       Month.DECEMBER, Month.valueOf("DECEMBER"));
    }
```

### Coverage of Utility Classes

Java adds an automatic constructor to all classes that do not have a constructor, including utility classes. So, unless you go out of your way to do so, your test suite will not cover the automatic constructor which means that the declaration of the class may appear to be uncovered. To get complete coverage you can:

- Construct an instance of the utility class in one of your tests (and, so, cover the automatic constructor); or
- Add a private default constructor to the utility class.

## Accessibility Settings

To change the color settings (for those who have difficulty with red/green colorblindness):

"Window+Preferences+General+Editors+Text Editors+Annotations"

The settings for code coverage highlighting can be found within

1\) Full Coverage

2\) Partial Coverage

3\) No Coverage

## For More Information

EclEmma is very powerful and has a number of capabilities that are not discussed here.

For more information, see the [user guide](http://www.eclemma.org/userdoc/index.html).
