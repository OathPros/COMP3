Placeholders
============

Initial state placeholders
--------------------------

An initial state placeholder is an image and text which fills the space in an application that has never contained any content.

When to use
~~~~~~~~~~~

In some cases an application might be empty until a user adds some content to it. In these scenarios, an initial state can be used to provide a rich and inviting experience. This helps to avoid the first use of the application being downbeat and unwelcoming.

An initial state placeholder should only be used when an application is going to be unavoidably empty. In many cases it is often better to pre-populate the application.

Guidelines
~~~~~~~~~~

* Follow the standard layout for the size and placement of the image and labels, so that your application is consistent with other GNOME 3 applications.
* The imagery used should be rich and colorful.
* The text that accompanies the image should be positive and upbeat. This is a moment where you can sell your application and establish a positive identity for it. It can also be an opportunity to strike up a relationship with the user by addressing them directly.
* If there are controls that allow items to be added, it can be appropriate to highlight them using a suggested style (see :ref:`button-styles`) while the list/grid is empty.
* While an application is initially empty, some controls don't serve a purpose (such as those for browsing content, changing view, or searching). Making these controls insensitive will help to avoid the user being disappointed, or trying features that won't work.
* An initial state should persevere until content is added to the application, after which it should not be seen again. If the application becomes empty subsequently, an empty state can be used

Empty placeholders
------------------

An empty placeholder is an image and text which fills the space in an empty list or grid.

When to use
~~~~~~~~~~~

Empty placeholders perform a number of important functions: they prevent confusion and guide the user, and they make your interface look better and more cohesive. They are also one of those nice touches which helps to communicate an attention to detail.

An empty placeholder should be displayed whenever a list or grid is empty.

Empty placeholders should not be displayed when an application is being run for the first time. In these situations an empty state is too negative and a richer, more characterful and positive experience is better.

Guidelines
~~~~~~~~~~

* Follow the standard layout for the size and placement of the image and labels, so that your application is consistent with other GNOME 3 applications.
* For the image, use a symbolic icon that either represents your application, or the type of content that would ordinarily appear in the grid or list.
* An empty placeholder should always include a label which communicates the empty state. It is often appropriate to include a smaller subtext which provides additional guidance (such as how to add items). However, this should only be included if there is additional information that it is useful to provide.
* If there are controls that allow items to be added, it can be appropriate to highlight them using a suggested style (see :ref:`button-styles`) while the list/grid is empty.