Search
======

Search allows content items to be located by filtering content that is displayed on screen. It is distinct from find, which involves moving or highlighting the content that is being searched for, rather than filtering.

Examples of search can be found in the *Search Entry* and *Type to Search* demos in the GTK 4 demo app.

When to use
-----------

Provide search whenever a large collection of content is presented, and those content items have a textual component. This could be a collection of actual content items, such as documents, contacts or videos, or a list of options.

Search is a great way to make it easy for users to find what it is they are looking for, and its consistent availability means that users can rely on and expect it to be present.

However, while search can be highly effective, and some users will use it, others will not. Therefore, try to supplement other means for finding content items with search, rather than relying on it exclusively.

The search bar
--------------

The standard pattern for search in GNOME utilizes a special search bar which slides down from beneath the header bar.

In primary windows, the search bar is typically hidden until it is activated by the user. There are three common ways to activate search in this context:

* Typing when a text entry field is not focused should activate search, and the entered text should be added to the search field. This is called “type to search”.
* The keyboard shortcut for search (Ctrl+F).
* A search button in the header bar should allow the search bar to be displayed (the search button should toggle).

If search is a primary method for finding content in your application, you can make the search bar permanently visible, or visible when the application is first started.

Search results
--------------

* Search should be “live” wherever possible — the content view should update to display search results as they are entered.
* In order to be effective, it is important that search results are quickly returned.
* If a search term does not return any results, ensure that feedback is given in the content view. Often a simple “No results” label is sufficient.

Additional Guidance
-------------------

* Be tolerant of mistakes in search terms. Matching misspellings or incorrect terminology is one way to do this. Presenting suggestions for similar matches or related content is another.
* Permit a broad range of matching search terms. This helps people who are unsure of the exact term they require but who do know characteristics associated with the item they want to find. A list of cities could return matches for country or region, for example.
* Results should be ordered in a way that ensures that the most relevant items are displayed first.

API reference
-------------

* GtkSearchBar: `GTK 4 <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.SearchBar.html>`_, `GTK 3 <https://developer.gnome.org/gtk3/stable/GtkSearchBar.html>`_
* GtkSearchEntry: `GTK 4 <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.SearchEntry.html>`_, `GTK 3 <https://developer.gnome.org/gtk3/stable/GtkSearchEntry.html>`_