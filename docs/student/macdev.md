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

### echo $0

> zsh is my shell.<br>
> There are many like it,<br>
> but this one is mine.

macOS started defaulting to zsh in like 10.15, seems fine.

Your shell probably has a few config files.
They are run at different times, and sometimes only some are run for certain kinds of shells.
In general, you most likely want to edit your `.zshrc` when you wish to modify the experience in the shell.
Most often, this is to change the things you can do on the command line, e.g. by adding new entries to your path, defining aliases or functions, adding completion for newly installed programs, or adding/updating environment variables.

Here's a few things in mine that you might like. Add some of your own if you think others could benefit (this is a wiki!)

```zsh
# Preferred editor for remote and local sessions (respectively)
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='vim'
else
  export EDITOR='code --wait' # depends on https://code.visualstudio.com/docs/setup/mac#_launch-vs-code-from-the-command-line
fi


# run browsers from the command line
BROWSER=/Applications/Firefox.app/Contents/MacOS/firefox

google-chrome() {
  open -a "Google Chrome" --args "$@"
}

```

#### Shell config managers

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
- [alt-tab](https://formulae.brew.sh/cask/alt-tab)
- [curl](https://formulae.brew.sh/formula/curl)
- [dbeaver-community](https://formulae.brew.sh/cask/dbeaver-community)
- [imagemagick](https://formulae.brew.sh/formula/imagemagick)
- [git](https://formulae.brew.sh/formula/git)
- [jq](https://formulae.brew.sh/formula/jq)
- [rectangle](https://formulae.brew.sh/cask/rectangle)
- [wget](https://formulae.brew.sh/formula/wget)

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

### Text Navigation

In many apps, [limited emacs hotkeys work](https://jblevins.org/log/kbd).

There's another nice system: consider the following modifier key combos to be of increasing weight:

1. ++option++ + ...
2. ++command++ + ...

Then if you combine them with the arrow keys, then you can move:

1. (no modifier only arrow key): one character horizontally or one line vertically
2. ++option++ + ...: up/down a section or paragraph or horizontally a word at a time
3. ++command++ + ...: beginning or end of the document or line

Then if you hold ++shift++ while navigating any of those, you'll select text.

### macOS

1.  On Windows they only have ++alt++ + ++tab++ (Quick window switcher, add ++shift++ into the mix to cycle in the reverse direction)
    1.  on a mac by default  ++command++ + ++tab++ changes _Apps_ and ++command++ + <kbd>`</kbd> switches between windows within an app
    2.  If you use the Alt-Tab app recommended above, you can control some of this
2.  most apps on a mac have 
    1.  ++command++ + <kbd>?</kbd> (or to be more precise: ++command++ + ++shift++ + <kbd>/</kbd>) mapped to search that app's menu items. it's awesome. it basically means you just made almost all the features of most apps keyboard-accessible!
    2.  the hotkey ++command++ + <kbd>,</kbd> to open its settings/prefs. this was so convenient and following some patterns in other hotkeys,
        1.  Dr. Stewart recommends you set up ++command++ + ++shift++ + <kbd>,</kbd> to open the macOS `System Settings`. to do so:
            1.  click on the apple on the top left of your primary monitor in the Menu Bar and choose `System Settings...`
            2.  scroll to choose `Keyboard`
            3.  find and click the button that says `Keyboard Shortcuts...`
            4.  find the section labeled `App Shortcuts`, click the plus `+` button and enter these values:
                1.  Application: `All Applications`
                2.  Menu title: `System Settings...` (**note**: you must enter the 3 dots)
                3.  Keyboard shortcut: ++command++ + ++shift++ + <kbd>,</kbd>
### vscode

(see more in [the docs](https://go.microsoft.com/fwlink/?linkid=832143))

1. ++command++ + ++shift++ + ++p++: DO EVERYTHING if you learn only one command it should be this bc then you start typing what you need to do and options come up
3. ++command++ + <kbd>/</kbd>: toggle comment for current line (or current selected lines)
2. ++command++ + ++p++: open a file (so like press this command and then just type characters that are anywhere in the filename no matter how deep in the files currently in the explorer of vscode...)
4. ++command++ + ++d++: (first highlight some text) `Add selection to next Find match`
    1.  so like select some word or part of a word or long bunch of syntax, press the shortcut and the next instance of the currently selected text in the document will also be selected, repeat (if there's an odd one that gets added before the next one you wanted, subsequently pressing ++command++ + ++k++, ++command++ + ++d++ will deselect the anomaly and select next [it's called `Move last selection to next Find match])
5. delete current line: ++command++ + ++shift++ + ++k++
    1. [apple symbol](https://unicode-explorer.com/c/F8FF) found accidentally trying to do the above: ++option++ + ++shift++ + ++k++
6. add cursor up/down: ++command++ + ++option++ + ++up++/++down++