.. image:: img/hig.svg

GNOME User Interface Guidelines
===============================

Whether you are a developer or a designer, these guidelines contain essential information for designing fantastic applications using the GNOME platform.

Content Overview
----------------

If you are new to the HIG, it is recommended that you start with :doc:`the vision <vision>`, which outlines the principles and goals behind the HIG and GNOME platform.

The next section contains :doc:`common guidelines <guidelines>` which apply throughout GNOME design. This covers standard conventions for writing text, icon usage, creating app identity, and responding to input using different devices.

The rest of the HIG covers each of the various design patterns and UI elements that you might want to use. These are broken down into sections

* :doc:`Containers <containers>`: the main widgets for containing controls and content
* :doc:`Navigation <nav>`: design patterns for moving around an app and its content
* :doc:`Feedback <feedback>`: widgets for displaying information
* :doc:`Controls <controls>`: the most common interactive UI elements
* :doc:`Reference <reference>`: keyboard shortcuts and touch gestures

Platform Scope
--------------

The HIG provides documentation for applications created using GTK4 and LibAdwaita, along with accompanying GNOME libraries. If you are using the GNOME Flatpak SDK, it will provide everything you need to use the design patterns found in this guide.

Where possible, the design guidance in the HIG is also relevant to those using GTK3 and LibHandy. However, not every design pattern is supported by these libraries.

.. toctree::
   :maxdepth: 2
   :hidden:

   vision
   guidelines
   containers
   nav
   feedback
   controls
   reference