View Switchers
==============

A view switcher is a control that allows switching between a small number of predefined views. For example, a music application could show different views for artists, albums and playlists.

Guidelines
----------

* As a rule of thumb, a view switcher should contain between three and five views. If you have more views, a :doc:`sidebar <sidebars>` might be a more appropriate choice.
* Label views with :ref:`header capitalization <header-capitalization>`, and use nouns rather than verbs, for example *Albums* or *Updates*. Try to give view labels a similar length.
* When used for settings, do not design views such that changing controls on one page affects the controls on any other page. Users are unlikely to discover such dependencies.
* If a control affects every tab, place it outside the tabs.
* Buttons in the view switcher widget can indicate when there is activity in a view.

API reference
-------------

* `HdyViewSwitcherBar <https://gnome.pages.gitlab.gnome.org/libhandy/doc/1-latest/HdyViewSwitcherBar.html>`_