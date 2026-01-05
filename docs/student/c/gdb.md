# gdb Quick Reference

## What is gdb

According to [GNU](https://www.gnu.org/software/gdb/),
GDB, the GNU Project debugger, allows you to see what is going on "inside" another program while it executes - or what another program was doing at the moment it crashed.

## Compiling For gdb

gdb needs information that is not ordinarily provided by the compiler. So, if you want to use gdb you need to include the `-g` switch when compiling. For example:

``` bash
g++ -c -g Driver.cpp
```

## Starting gdb

To start gdb, simply enter the gdb command in a terminal window. It has one paramter, the name of the executable. For example:

    gdb Driver

## Basic gdb Commands

The following commands are listed in alphabetical order:

| Command                           | Purpose                                                         |
|-----------------------------------|-----------------------------------------------------------------|
| *Enter*                           | Re-execute the previous gdb command                             |
| break *xx*                        | Set a breakpoint at line *xx* in the current file               |
| break *functionname*              | Set a breakpoint at the start of *functionname*                 |
| break *classname*::*functionname* | Set a breakpoint at the start of a method                       |
| break *filename*:*xx*             | Set a breakpoint at line *xx* in a specified file               |
| continue                          | Resume running/executing the program                            |
| disable *xx*                      | Disable breakpoint number *xx*                                  |
| enable *xx*                       | Enable breakpoint number *xx*                                   |
| help                              | Display a list of gdb commands                                  |
| help *command*                    | Get help on a specific command                                  |
| info break                        | List all breakpoints                                            |
| info source                       | Show the name of the current source file                        |
| info sources                      | List the name of all source files in use                        |
| list                              | List the next source lines                                      |
| list *xx*                         | List source lines starting at line *xx*                         |
| list *xx*,*yy*                    | List sources lines from *xx* to *yy*                            |
| list *filename*:*xx*              | List source lines in the specified file starting at line *xx*   |
| next                              | Execute the current statement and then stop                     |
| print *variable*                  | Print the value of a variable                                   |
| quit                              | Quit gdb                                                        |
| run                               | Run/execute the program starting from the beginning             |
| set *variable* = *value*          | Assign a new value to a variable                                |
| step                              | Execute the current statement (entering a function if possible) |

## A Sample Session

A small sample session of gdb (with an executable named `Driver`) might look something like the following \[where \$ is the shell prompt and (gdb) is the gdb prompt\]:

``` bash
$ gdb Driver
(gdb) break 1
(gdb) run
(gdb) next
(gdb) print i
(gdb) next
(gdb) print i
(gdb) quit
```
