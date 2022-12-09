View Switchers
==============

.. image:: /img/adw-screenshots/view-switcher-title.png
   :class: light
.. image:: /img/adw-screenshots/view-switcher-title-dark.png
   :class: dark

A view switcher is a control that allows switching between a small number of predefined views. For example, a music app could show different views for artists, albums and playlists.

Guidelines
----------

* As a rule of thumb, a view switcher should contain between three and five views. If you have more views, a :doc:`sidebar <sidebars>` might be a more appropriate choice.
* Label views with :ref:`header capitalization <header-capitalization>`, and use nouns rather than verbs, for example *Albums* or *Updates*. Try to give view labels a similar length.
* When used for preferences, do not design views whose controls affect the controls in other views. Users are unlikely to discover such dependencies.
* View switcher buttons can indicate when there is activity in a view. For example, this could indicate if there is new content available.
* View switchers should switch to the bottom window edge if the window becomes too narrow for them to fit in the header bar. This can be done with the ``ViewSwitcherTitle`` and ``ViewSwitcherBar`` widgets.

API Reference
-------------

* Adwaita:
   * `AdwViewSwitcher <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/class.ViewSwitcher.html>`_
   * `AdwViewSwitcherTitle <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/class.ViewSwitcherTitle.html>`_
   * `AdwViewSwitcherBar <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/class.ViewSwitcherBar.html>`_
* Handy:
   * `HdyViewSwitcher <https://gnome.pages.gitlab.gnome.org/libhandy/doc/1-latest/class.ViewSwitcher.html>`_
   * `HdyViewSwitcherTitle <https://gnome.pages.gitlab.gnome.org/libhandy/doc/1-latest/class.ViewSwitcherTitle.html>`_
   * `HdyViewSwitcherBar <https://gnome.pages.gitlab.gnome.org/libhandy/doc/1-latest/class.ViewSwitcherBar.html>`_
