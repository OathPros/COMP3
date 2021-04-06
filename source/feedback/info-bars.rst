Info Bars
=========

An info bar is a strip that is placed above a content view, directly below the header bar or tool bar. It contains text, and can also include controls. Info bars persist: they can be permanent, or they can be dismissed by the user.

When to use
-----------

Info bars can be used to communicate a particular state about a particular content item or location. For example, an info bar could indicate that a document is out of date or being edited by others, or that a service relating to a location is not operating. In some situations, they can also be used to present supplementary information, such as user guidance.

Since info bars are persistent, they are generally more appropriate for communicating ongoing states rather than events (:doc:`notifications <notifications>` are more appropriate here).

Info bars primarily communicate by using text, and have the advantage that they can include both a heading and a longer explanation. However, they also take up space and attract attention. If the state you want to communicate is not critical, or can be communicated through a simple string or icon, you might want to consider alternative approaches: text or icons can be added elsewhere in your interface, or the appearance of navigation controls (such as :doc:`view switchers </nav/view-switchers>`) can be changed.

Guidelines
----------

* Beware of info bar overuse: they should be an exceptional presence in your interface.
* Only one info bar should be visible at any one time.
* Only include a longer explanation if it is really needed: a simple heading can often be sufficient.
* Generally speaking, info bars do not require an icon.

API reference
-------------

* `GtkInfoBar <https://developer.gnome.org/gtk3/stable/GtkInfoBar.html>`_