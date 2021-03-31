# HIG Playground

This is a test bed for the new HIG. Goals:

  * Simple markdown based workflow. Using Apostrophe for authoring is a plus (with image preview).
  * Simple and elegant stylesheet
  * More sophisticated media (animated svgs, inline video).
  * Simple to maintain/update tooling with small dependency tree.


Sphinx/rtd
  - markdown only a 2nd class citizen
  - default themes suck
  + commonly used

  now lives in `master`

Mkdocs
  + markdown based
  + straight forward
  
  now lives in `mkdocs-material` branch
  
## How to build locally

You can use Sphinx to build the static html locally, for testing.

### Install dependencies

On Fedora, run:


```
dnf install -y python3-sphinx python3-pip
pip3 install --upgrade furo
pip3 install --upgrade recommonmark
```

### Build

From the project root, run the `00localbuild.sh` script. The build output can 
then be found in `/build`.
