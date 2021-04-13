Info Bars
=========

Info bars can be used to communicate the state of an app, content item or location. Examples include an app being offline or a document being read-only. In some situations, they can also be used to present supplementary information, such as user guidance.

When to use
-----------

Info bars are persistent: they are permanently visible until the state they are communicating has ended or, until they are dismissed by the user. This is one reason why they are more appropriate for communicating ongoing states, as opposed to events.

In contrast to :doc:`notifications <notifications>`, info bars are only shown in an application window. They are therefore an appropriate choice when the information to be communicated is only relevant while using the app.

Info bars take up space and can be distracting. If the state you want to communicate is not critical, or can be communicated through a less disruptive string or icon, you might want to consider alternative ways to communicate the state in question.

Guidelines
----------

* Beware of info bar overuse: they should be an exceptional presence in your interface.
* Only one info bar should be visible at any one time.
* Info bars should always have a heading.
* Only include a longer explanation if it is really needed: a simple heading can often be sufficient.
* Generally speaking, info bars do not require an icon.
* If an info bar is dismissable, use a close button using the ``window-close-symbolic`` icon.
* Info bars can include buttons to provide additional actions relating to the state they describe. They should typically have no more than two of these.

API reference
-------------

* GtkInfoBar: `GTK 4 <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.InfoBar.html>`_, `GTK 3 <https://developer.gnome.org/gtk3/stable/GtkInfoBar.html>`_