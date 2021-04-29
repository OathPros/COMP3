Drop-Down Lists
===============

.. image:: ../img/screenshots/drop-down-list.png

Drop-down lists are used to select from a mutually exclusive set of options.

:doc:`Radio buttons <radio-buttons>` are generally preferable to drop-down lists, as they present all the available options without the need for interaction. However, drop-down lists may be preferable when:

* there is little available space
* the list of options may be long or change over time
* the contents of the hidden part of the menu are obvious from its label and the one selected item. For example, if you have an option menu labelled "Month:" with the item "January" selected, the user might reasonably infer that the menu contains the 12 months of the year without having to look.

Drop-down lists can also be useful in :doc:`header bars </containers/header-bars>`.

A drop-down list example can be found in the *Lists → Selections* demo in the GTK 4 demo application.

Guidelines
----------

* Do not use drop-down lists with fewer than three items. To offer a choice of two options, use :doc:`radio <radio-buttons>` or :ref:`toggle <toggle-buttons>` buttons.
* Label drop-down lists using :ref:`sentence capitalization <sentence-capitalization>`. Provide an access key in the label that allows the user to focus the drop-down list.
* Use :ref:`sentence capitalization <sentence-capitalization>` for drop-down list items.
* Assign an access key to every drop-down list item. Ensure each access key is unique within the enclosing window or dialog, not just within the menu.

API Reference
-------------

* `GtkDropDown <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.DropDown.html>`_ (GTK 4)
* `GtkComboBox <https://developer.gnome.org/gtk3/stable/GtkComboBox.html>`_ (GTK 3)
