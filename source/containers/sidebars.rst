Sidebars
========

A sidebar list allows different views to be switched between. Those views can contain groups of content items, single content items, or sets of controls. The sidebar divides the window in two, with content being shown on the opposite pane to the sidebar.

Sidebar lists can be used in primary windows, either as a permanent fixture or an element that is shown on demand. They can also be used in dialog windows.

Sidebar lists can be used in conjunction with the :doc:`search </nav/search>` and selection mode design patterns.

When to use
-----------

Use a sidebar list when it is necessary to expose a larger number of views than can be accommodated by a standard :doc:`view switcher </nav/view-switchers>`.

Sidebar lists also provide a possible alternative to browser-style navigation. They have a number of advantages here:

* When content items have a narrow width, and don’t require an immersive experience. A sidebar would be inappropriate for browsing videos for this reason, but is well-suited to contacts.
* When content items are dynamic. For messaging applications, where new content items appear or old ones are updated, a sidebar list provides the ability for someone to view one item while simultaneously being aware of updates to the overall message list.
* When it is possible to filter a collection of content, and there are a large number of filters.

Temporary sidebar lists can also be displayed for particular views in your application.

Guidelines
----------

* Order the list according to what is most useful for the users of your application. It is often best to place recently updated items at the top of the list.
* Header bar controls which affect the sidebar list should be placed within the list pane section of the header bar. Controls for search and selection should be found above the list.
* Each list row can include multiple lines of text, as well as images. However, be careful to ensure that the most important information is not lost, and work to ensure a clean and attractive appearance.

API reference
-------------

* `GtkListBox <https://developer.gnome.org/gtk3/stable/GtkListBox.html>`_
* `GtkScrolledWindow <https://developer.gnome.org/gtk3/stable/GtkScrolledWindow.html>`_
* `GtkStackSidebar <shttps://developer.gnome.org/gtk3/stable/GtkStackSidebar.html>`_