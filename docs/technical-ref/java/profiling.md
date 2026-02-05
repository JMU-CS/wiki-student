# Profiling Java Programs

## Overview

The performance (both CPU usage and memory usage) of Java programs can be monitored using a tool called the VisualVM. It can identify programs running in a Java virtual machine, use various technologies to collect data about those programs, and provide visualizations of those data. This document is concerned with using the VisualVM for profiling/sampling.

## Steps in the Process

To use the VisualVM for profiling/sampling:

1.  Start the VisualVM (see below).
2.  Execute your program (see below).
3.  In the "Applications" pane, double-click on your program.
4.  Click on either "Sampler" tab or the "Profiler" tab (see below).
5.  Click on "CPU" to start collecting data about CPU usage or "Memory" to start collecting data about memory usage (see below).
6.  Use your program as appropriate.
7.  Click on "Stop" to stop collecting data.

## Details of the Process

This section provides more information about some of the steps in the process.

### Starting the VisualVM

Depending on your operating system and the JDK, the VisualVM can be started from the command line by executing the program `visualvm` or `jvisualvm` from the directory/folder in which it was installed.

### Executing Your Program

In principal, the VisualVM can be used with programs that are executed inside of an IDE (e.g., it can be [integrated with Eclipse](../eclipse/visualvm_install.md)), however, subtle issues often arise. So, if you have problems attempting to profile your program when you run it inside of your IDE you will need to run it outside of your IDE. The two easiest ways to do this are to: (1) execute the program from the command line or (2) use an [executable/runnable JAR file](jar.md).

### Sampling vs. Profiling

There are two different ways to collect performance data about code while it executes.

In an *event-based* approach the code is instrumented so that each time a method is entered and exited an event is generated. The times of the events can then be used to generate detailed reports about performance. This approach is very accurate but is both time-consuming (because all of the events must be processed) and changes the code (meaning the behavior of the code could change, especially for sections that depend on timing). In the VisualVM this approach is called "profiling".

In a *time-based* approach the performance of the code is investigated at regular intervals (e.g., by using thread dumps). This approach is much less accurate (indeed, methods that execute very quickly relative to the size of the intervals may be missed entirely) but is much less time-consuming and tends to have fewer impacts on the behavior of the code. In the VisualVM this approach is called "Sampling".

### CPU Usage vs. Memory Usage

As everyone who has studied data structures and algorithms knows, when writing code one can often trade-off memory performance for processor performance and vice versa. Hence, the VisualVM allows you to measure either CPU usage or memory usage.

### Selecting the Classes to Profile

On both the "Profiler" tab and the "Sampler" tab there is a "Settings" checkbox. When checked a "CPU settings" tab appears that allows you to select either which classes to include or which classes to exclude. By default, classes that are part of the Java library are excluded.

## For More Information

The VisualVM is very powerful and has a number of capabilities that are not discussed here. For more information, see the [current developer documentation](https://visualvm.github.io/documentation.html) or the [original Oracle documentation](https://docs.oracle.com/javase/8/docs/technotes/guides/visualvm/index.html).
