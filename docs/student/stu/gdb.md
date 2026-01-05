====== GDB on stu ======

===== GDB + VS Code configuration =====

Here is a sample ''launch.json'' file. This one is set up for the CS 261 P0, but you can modify it for any C project by changing "''intro''" to the name of your executable. You can also provide command-line arguments using ''args'' (e.g., for CS 261 P1, you might specify ''[ "-H", "tests/inputs/simple.o" ]''.

<code>
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Launch",
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceRoot}/intro",
            "args": [""],
            "cwd": "."
        }
    ]
}
</code>