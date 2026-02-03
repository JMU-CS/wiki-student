# Developing on a mac

This page is under construction, please feel free to add a relevant section or subpage, For now I just need to mention homebrew because it's the preferred method for getting Meld.

## Command Line Interface

The default app providing a CLI on macOS is Terminal. It's located in `/Applications/Utilities/Terminal.app` if you're looking for it in Finder, but the simplest way to get to it is to:

1.  press "command" + "space"
2.  in the resulting search box, type `Term`
    - you should see the `Terminal` app as a top search result
3.  use the "down arrow" to highlight the `Terminal` search result
4.  press "return"
5.  you should now have a terminal window open

## Shell

1.  iTerm2.app (Dr. Stewart uses this)
2.  honorable mentions
    - Warp
    - Hyper

### Shell config managers

1.  [Oh my ZSH](https://github.com/ohmyzsh/ohmyzsh)

### Shell Themes

1.  [PowerLevel10k](https://github.com/romkatv/powerlevel10k) (Dr. Stewart uses this)

## Homebrew

Homebrew is a package manager for macOS. Pretty much any developer software made for Linux (and much that's not) is available for install via Homebrew, and this installation is typically much simpler than alternatives, especially for developer tools.

Both installing Homebrew itself, as well as afterward using it to install other software are done via the [command line](#command-line-interface).

### Install Homebrew

On the command line, paste the command found at <https://brew.sh/#install> to install homebrew.

### Install other packages via Homebrew

To install a package that's command-line-only, simply run:

1.  `brew install <package>`
    - e.g. `brew install lolcat`

To install a package that has a graphical user interface, simply run:

1.  `brew install --cask <package>`
    - e.g. `brew install --cask meld`

Stewart recommends you consider installing:

- [Trash](https://formulae.brew.sh/formula/trash) to be able to `trash` files and directories from the command line (they'll go to the Trash of filesystem/GUI rather than just gone like with `rm`)

## Window Management

1.  [Rectangle.app](https://rectangleapp.com/)
2.  AltTab.app
3.  else?

## Password Manager

1.  1password (costs \$)
2.  honorable mentions:
    1. [BitWarden](https://bitwarden.com/) free and open source (for "basic")

## Productivity/Else

1.  [Alfred](https://alfred.app/), especially because the (paid) powerpack has clipboard history ([finally a free feature on Windows](https://support.microsoft.com/en-us/windows/clipboard-in-windows-c436501e-985d-1c8d-97ea-fe46ddf338c6))
    - s/o to Carlos on [this cheaper clipboard history app called Clipsy](https://appyogi.com/apps/clipsy-clipboard-manager-for-mac/)
        - FYI: Dr. Stewart who historically recommends the more expensive alfred powerpack for this feature hasn't tried Clipsy yet
    - [Bartender](https://www.macbartender.com/)

## HotKey Index

1.  TODO...
