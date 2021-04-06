# Human Interface Guidelines

This is a development space for a new version of the GNOME Human Interface Guidelines. The current stable version is hosted on library.gnome.org and stored as part of gnome-devel-docs.

The new version is written in reStructuredText, generated using Sphinx, and hosted using Gitlab pages. It can be viewed online at .

## How to build and edit locally

You can use Sphinx to build the static html locally, for testing.

### Install dependencies

On Fedora, run:

```
dnf install -y python3-sphinx python3-pip
pip3 install --upgrade furo
```

### Make changes

VS Code is a good choice for this, as it is able to preview the source files as rendered HTML.

### Build

Building the docs checks for errors, as well as producing local static HTML of the HIG website.

To build, run `00localbuild.sh` from the project root. The build output can then be found in ``/build``.

## Deploying changes

Changes to master are automatically deployed to the site using CI.