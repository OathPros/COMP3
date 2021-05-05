.. image:: img/hig.svg

GNOME User Interface Guidelines
===============================

Whether you are a developer or a designer, these guidelines contain essential information for designing fantastic applications using the GNOME platform.

The GNOME Human Interface Guidelines are the primary design resource for those creating software for the GNOME platform. They are primarily indended for application designers and developers, but are relevant to anyone wanting to familize themselves with the GNOME platform.

Platform Definition
-------------------

The HIG is intended to be used in reference to recent versions of the GNOME platform, as provided by the GNOME Flatpak SDK.

Application developers are expected to be using GTK 4 and the Adwaita library, and it is for these libraries that the HIG is primarily indended.

Much of the HIG is also relevant to applications that are using GTK 3 and the associated Handy library.

Content Overview
----------------

:doc:`Guidelines <guidelines>` covers the standard conventions to be used throughout designs, including how to write text, use icons, create app identities, and handle different types of input.

The rest of the HIG provides documentation on the various design patterns and user interface elements that are found in the GNOME platform, including:

* :doc:`Containers <containers>`: the most basic elements, including windows, lists and grids.
* :doc:`Navigation <nav>`: patterns for structure, movement and flow, including views, browsing, tabs.
* :doc:`Feedback <feedback>`: elements for displaying information and soliciting responses from users.
* :doc:`Controls <controls>`: common interactive UI elements.
* :doc:`Reference <reference>`: keyboard shortcuts and touch gestures.

.. toctree::
   :maxdepth: 1
   :hidden:

   principles
   resources
   guidelines
   containers
   nav
   feedback
   controls
   reference
