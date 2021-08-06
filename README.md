# Human Interface Guidelines

The GNOME Human Interface Guidelines are the primary source of UX design documentation for GNOME.

This version replaces the previous version which was hosted as part of the [gnome-devel-docs](https://gitlab.gnome.org/GNOME/gnome-devel-docs/) module.

The HIG is written in [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html), generated using [Sphinx](https://www.sphinx-doc.org/en/master/index.html), and hosted using [GitLab pages](https://docs.gitlab.com/ee/user/project/pages/). It can be viewed online [here](https://developer.gnome.org/hig/).

## Goals for the HIG

Goals:

 - App designers and developers are the primary audiences
 - Document the most important and commond design patterns
 - Be easy to digest: don't be too long or verbose
 - Use examples and demos as much as possible 

Non-goals:

 - Not a generic guide to UX design, and shouldn't try to fill in basic design knowledge, but should be accessible to those with relatively little design expertise
 - Don't document every design pattern or possible variation
 - Don't be prescriptive: allow designers to make their own choices, and give them the space to be creative

## How to build and edit

Sphinx can be used to build and preview the static html site locally, either with the browser or VS Code.

### 1. Install dependencies

On Fedora, run:

```
dnf install -y python3-sphinx python3-pip
pip3 install --upgrade furo
```

### 2. Make changes

VS Code is a good choice for this, as it is able to preview the source files as rendered HTML.

### 3. Build

Building the docs checks for errors, as well as producing local static HTML of the HIG website.

To build, run `00localbuild.sh` from the project root. The build output can then be found in ``/build``.

### 4. Deploy changes

Changes to master are automatically deployed to the site using CI.

