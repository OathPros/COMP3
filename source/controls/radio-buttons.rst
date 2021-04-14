Radio Buttons
=============

Radio buttons allow a selection to be made from a set of options. 

When to use
-----------

Radio buttons are similar to :doc:`checkboxes <checkboxes>`, :doc:`switches <switches>` and :doc:`drop-down lists <drop-downs>`. However, radio buttons have crucial differences from these other controls:

* Unlike checkboxes and switches, radio buttons allow each option to be individually labelled. This is important when the options are not obviously mutually exclusive. For example, an option to sort by author or by date.
* Unlike drop-down lists, radio buttons display all options without the need for disclosure. This has the advantage of not requiring work on the user's part to discover the range of options that are available. As a result, they are preferable for small sets of options, but inappropriate for longer option lists.

Guidelines
----------

* One button in the set should be selected at all times. (The only exception is when the group is showing the properties of a multiple selection, when one or more of the buttons may be in their mixed state.)
* Use :ref:`sentence capitalization<sentence-capitalization>` for radio button labels. For example, *Single click to open*.
* If the radio button represents a property of multiple items, and that property is present for some items and non-present for others, show the radio button in its mixed state.

API Reference
-------------

* GTK 4: `GtkCheckButton <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.CheckButton.html>`_
* GTK 3: `GtkRadioButton <https://developer.gnome.org/gtk3/stable/GtkRadioButton.html>`_