Shortcut Windows
================

.. image:: /img/adw-screenshots/shortcuts-dialog.png
   :class: only-light
.. image:: /img/adw-screenshots/shortcuts-dialog-dark.png
   :class: only-dark

Shortcut windows allow someone to look up a keyboard shortcut for a specific action, as well as to learn and discover the available shortcuts in an app.

When to Use
-----------

Every app that has keyboard shortcuts should include a shortcut window.

Guidelines
----------

General guidelines:

* Follow the general :ref:`guidelines for assigning keyboard shortcuts <shortcut-keys>`.
* Include every keyboard shortcut in your app. However, do not include shortcuts if they are:

  * generic and not a crucial part of your app (for example, Cut/Copy/Paste in an app where these actions are not essential), or
  * historical artifacts which no longer form an important part of your application's functionality.

* Shortcut labels should use imperative verbs, using :ref:`header capitalization <header-capitalization>`. For example, Save or Update. (This is the the same format as button labels.)

Use groups to make the shortcuts window easy to navigate:

* Group shortcuts logically, with functionally and conceptually similar shortcuts in the same group.
* As a rule of thumb, groups should contain between two and ten items. While groups containing two or three items are acceptable, try to keep the number of such groups low (if the majority of the shortcuts are in small groups, the window will be difficult to navigate).
* Place the groups containing the most useful information first. This will typically be the groups containing the most frequently-used shortcuts.
* Group headings should either be imperative verbs or singular nouns, using header capitalization. For example: Edit, Search, Document, Tab.

API Reference
-------------

* `Libadwaita: ShortcutsDialog <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/1-latest/class.ShortcutsDialog.html>`_
