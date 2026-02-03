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

## Redirects

Before pushing changes, please make sure you perform these steps:

1. Execute `/redirects.py`
2. Copy the output of that file to your clipboard.
3. Inside `/docs/.htaccess` paste the output to replace all lines in the file **except the first redirect line.**
4. Make sure to remove '+' from each line before committing and pushing.

## Attributions

<a href="https://www.flaticon.com/free-icons/working-hours" title="working hours icons">Working hours icons created by Uniconlabs - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/discussion" title="discussion icons">Discussion icons created by Freepik - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/schedule" title="schedule icons">Schedule icons created by Freepik - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/advise" title="advise icons">Advise icons created by juicy_fish - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/time-and-date" title="time and date icons">Time and date icons created by Rooman12 - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/government" title="government icons">Government icons created by Eucalyp - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/1st" title="1st icons">1st icons created by Freepik - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/graduation-cap" title="graduation cap icons">Graduation cap icons created by Freepik - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/technical-support" title="technical Support icons">Technical Support icons created by Freepik - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/teacher" title="teacher icons">Teacher icons created by adityayoga - Flaticon</a>
