# Rsync

## Setup

If you aren't on windows, you probably have `rsync` installed already (or if it isn't, you can use your OS's package manager \[or homebrew on macOS\] to install it).

### Windows

If you are running Windows, `rsync` is likely not installed.
Follow these steps to get `rsync` working in Git Bash (without having to install and configure a bunch of other tools):

!!! info git bash prerequisite
    If you don't already have git and git bash installed, [get it first](./beginner.md#prerequisites).

!!! example "Watch Dr. Stewart do all this..."

    [On a really slow Windows laptop though 😬.](https://youtu.be/vzJyP6hbkCE)

1. Download and open the latest [rsync package][R] from MSYS2.
2. Copy the `usr` folder (from `rsync...tar.zst`) into `C:\Program Files\Git`.
    * This should merge the files into the existing `C:\Program Files\Git\usr` folder.
3. Download the latest [libxxhash package][X] from MSYS2.
4. Copy the `usr` folder (from `libxxhash...tar.zst`) into `C:\Program Files\Git`.
    * This should merge the files into the existing `C:\Program Files\Git\usr` folder.
5. You should now be able to type `rsync` in Git Bash and see the usage message.

[R]: https://repo.msys2.org/msys/x86_64/rsync-3.4.1-1-x86_64.pkg.tar.zst
[X]: https://repo.msys2.org/msys/x86_64/libxxhash-0.8.3-1-x86_64.pkg.tar.zst
