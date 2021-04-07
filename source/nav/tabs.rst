Tabs
====

Tabs provide a way to break down a window into a series of views. They come in two primary forms: fixed and dynamic.

Fixed tabs provide an immutable set of predefined views, and are primarily used in dialog windows. Dynamic tabs allow a window to contain mutable selection of content items, such as pages, documents or images. They are primarily used within :doc:`/containers/primary windows </containers/primary-windows>`, as a part of editor or browser applications.

When to use
-----------

Use fixed tabs when a :doc:`dialog window </containers/dialogs>` contains too many controls (or too much information) to be comfortably presented at once.

Dynamic tabs are primarily useful for browser or editor applications, where a user might want to use several locations or content items simultaneously.

Fixed tabs
----------

* Do not use too many tabs. If you cannot see all the tabs without scrolling or splitting them into multiple rows, you are probably using too many and should use a list control instead.
* Label tabs with :ref:`header capitalization <header-capitalization>`, and use nouns rather than verbs, for example *Font* or *Alignment*. Try to give tab labels a similar length.
* Do not design tabs such that changing controls on one page affects the controls on any other page. Users are unlikely to discover such dependencies.
* If a control affects every tab, place it outside the tabs.
* With fixed tabs, make the width of each tab proportional to the width of its label. Don’t just set all the tabs to the same width, as this makes them harder to scan visually, and limits the number of tabs you can display without scrolling.

Dynamic tabs
------------

* Tabs often have a constrained width, so ensure that tab labels are short and concise, and that the most useful part of the label is displayed first. This ensures that the label continues to be useful even when ellipsized.
* If the content of a tab changes or requires attention, a visual hint can be displayed.
* Provide a context menu on each tab. This menu should only include actions for manipulating the tab itself, such as *Move Left*, *Move Right*, *Move to New Window*, and *Close*.
* If tabs are an important part of the application, a new tab button can be placed in the header bar or toolbar. Do not show a new tab button in applications where tabs will not always be used — keyboard shortcuts and/or menu items are sufficient in these cases.

Standard Keyboard Shortcuts
---------------------------

When using dynamic tabs, ensure that the standard keyboard shortcuts are supported.

.. list-table::
  :widths: 30 70
  :header-rows: 0

  * - Ctrl+T
    - Create a new tab
  * - Ctrl+W
    - Close the current tab
  * - Ctrl+Page Up
    - Switch to the next tab
  * - Ctrl+PageDown
    - Switch to the previous tab

API reference

* `GtkNoteBook <https://developer.gnome.org/gtk3/stable/GtkNotebook.html">`_