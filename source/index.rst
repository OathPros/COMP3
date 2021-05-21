.. image:: img/hig.svg

GNOME User Interface Guidelines
===============================

The GNOME Human Interface Guidelines are the primary design resource for those creating software with the GNOME development platform. They are primarily indended for application designers and developers, but are relevant to anyone wanting to familize themselves with GNOME UX.

Platform Definition
-------------------

The HIG is intended to be used in conjunction with recent versions of the GNOME platform, as provided by the GNOME Flatpak SDK.

Application developers are expected to be using GTK 4 and the Adwaita library, and it is for these libraries that the HIG is primarily indended.

Much of the HIG is also relevant to applications that are using GTK 3 and the associated Handy library.

Content Overview
----------------

:doc:`Design principles <principles>` provides the highest level of guidance and is the best place to start for anyone who is new to the HIG. :doc:`Resources <resources>` is an overview of the tools and assets that are available for GNOME design work.

The :doc:`guidelines section <guidelines>` covers the standard conventions to be used in GNOME UX design, including how to write text, use icons, create app identities, and handle different types of input.

The rest of the HIG provides documentation on the various design patterns and user interface elements that are found in the GNOME platform, including:

* :doc:`Containers <containers>`: the most basic elements, including windows, lists and grids.
* :doc:`Navigation <nav>`: patterns for structure, movement and flow, including views, browsing, tabs.
* :doc:`Feedback <feedback>`: elements for displaying information and soliciting responses from users.
* :doc:`Controls <controls>`: common interactive UI elements, including buttons, menus, switches, and so on.
* :doc:`Reference <reference>`: standard keyboard shortcuts and colors.

Issues & Contributions
----------------------

See the `HIG project <https://gitlab.gnome.org/Teams/Design/hig-www>`_ on GNOME's Gitlab instance for issue reporting and change proposals.

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
