# wiki-student

The wiki is built using [Zensical](https://zensical.org/), a static site generator.
Deployment to `wiki.cs.jmu.edu` is automated via GitHub actions.

This repository is public, so anyone online can view the wiki source code.
JMU CS faculty and staff have write access and can make edits directly on GitHub.
Students and others who would like to contribute may submit a pull request.

## Authoring

Wiki pages are written in Markdown.
For basic syntax, see the [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/).
For extended features supported by this site, see the [Zensical Docs](https://zensical.org/docs/authoring/markdown/).

## Commands

To install / upgrade to the latest version:
``` sh
pip install --upgrade --force-reinstall zensical
```

To preview the site locally while editing:
``` sh
zensical serve
```
