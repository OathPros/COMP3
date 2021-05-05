Drop-Down Lists
===============

.. image:: ../img/screenshots/drop-down-list.png

Drop-down lists are used to select from a mutually exclusive set of options.

A drop-down list example can be found in the *Lists → Selections* demo in the GTK 4 demo application.

When to Use
-----------

Drop-down lists are typically appropriate when:

* there is little available space, such as in :doc:`header bars </containers/header-bars>`
* the list of options may be long
* the contents of the hidden part of the menu are obvious from its label and the one selected item. For example, if you have an option menu labelled "Month:" with the item "January" selected, the user might reasonably infer that the menu contains the 12 months of the year without having to look.

If these factors don't apply, a :doc:`radio button <radio-buttons>` might be a better choice, since radio buttons present all the available options without the need to explicitly expose them.

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
