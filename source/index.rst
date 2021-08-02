.. image:: img/hig.svg

GNOME User Interface Guidelines
===============================

The GNOME Human Interface Guidelines are the primary design resource for those creating software with the GNOME development platform. They are primarily intended for application designers and developers, but are relevant to anyone wanting to familiarize themselves with GNOME UX.

Platform Definition
-------------------

The HIG is intended to be used in conjunction with recent versions of the GNOME platform, as provided by the GNOME Flatpak SDK.

Application developers are expected to be using GTK 4 and the Adwaita library, and it is for these libraries that the HIG is primarily intended.

Much of the HIG is also relevant to applications that are using GTK 3 and the associated Handy library.

Content Overview
----------------

The HIG is made up of the following sections:

* :doc:`Design principles <principles>`: basic design rules and goals for the GNOME platform. This is the best place to start for anyone who is new to the HIG or GNOME design.
* :doc:`Resources <resources>`: an overview of the tools and assets that are available for GNOME design work.
* :doc:`Guidelines <guidelines>`: the standard conventions that are used in GNOME UX design, including how to write text, use icons, create app identities, and handle different types of input.
* :doc:`Patterns <patterns>`: covers the elements from which designs can be composed, such as :doc:`windows </patterns/containers/windows>`, :doc:`buttons </patterns/controls/buttons>`, :doc:`notifications </patterns/feedback/notifications>` or :doc:`view switchers </patterns/nav/view-switchers>`. The patterns are organized into four types: :doc:`containers </patterns/containers>`, :doc:`navigation </patterns/nav>`, :doc:`feedback </patterns/feedback>`, and :doc:`controls </patterns/controls>`.
* :doc:`Reference <reference>`: standard keyboard shortcuts and UI colors.

Contribute
----------

See the `HIG project <https://gitlab.gnome.org/Teams/Design/hig-www>`_ on GNOME's Gitlab instance for issue reporting and change proposals.

.. toctree::
   :maxdepth: 1
   :hidden:

   principles
   resources
   guidelines
   patterns
   reference

