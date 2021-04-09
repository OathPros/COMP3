Lists
=====

Lists can be used to present content items and controls. Examples include a list of recently opened documents, or a set a preferences.

:doc:`Tree views<tree-views>` provide an alternative to the standard list pattern, for particular use cases.

General guidelines
------------------

* List rows typically contain between one and three elements. Different text elements can be differentiated using :doc:`text size and color </guidelines/typography>`. 
* Ensure that lists are ordered to be helpful to those who are using them. Recent documents might be more useful than alphabetically ordered documents, or contacts that are online might be more interesting than those who are offline, for example.
* If you use icons in your list, use :doc:`symbolic icons </guidelines/icons>`. The lower visual footprint of these icons will mean that they do not visually overload or dominate your list.
* If the list is long, make it possible to search it using the standard :doc:`search design pattern </nav/search>`.
  
Editable lists
--------------

Editable lists allow a user to add or remove items from the list (for this reason, they are sometimes known as add/remove lists).

Each row contains a remove button. If the number of items is short, the final list row should be used as an add button.

API reference
-------------

* `GtkListBox <https://developer.gnome.org/gtk3/stable/GtkListBox.html>`_