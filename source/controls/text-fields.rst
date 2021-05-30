Text Fields
===========

.. image:: ../img/screenshots/text-fields.png

Text fields are used for single line text entry and editing. :doc:`Search entries </nav/search>` are a type of text field which have their own dedicated pattern.

Multi-line text editing can be accomplished with a text view.

Guidelines
----------

General guidelines for text fields:

* Give text fields a label using :ref:`header capitalization <header-capitalization>`, and assign an access key to the label, to allow people to focus the control using a keyboard.
* Size text fields according to the likely size of the content they will contain. This gives a useful visual cue to the amount of expected input.
* When a text field contains a property or setting, apply any changes when Return is pressed or when the field loses focus.  

Text fields can often require their content to have a particular format, such as in the case of a URL or hex color value. In these cases, it is important to provide effective feedback as to whether the field is valid or invalid. When doing this:

* It is generally better to show positive feedback when the content is valid, as opposed to showing negative feedback while it is invalid. This avoids distracting and confusing users while they are in the process of editing the field.
* One common pattern for individual text fields is to have a linked action button that becomes sensitive when the field content is valid.
* In general, it is better to show feedback in real time as the field is edited, as opposed to waiting until the field loses focus.
  
Embedding Icons, Buttons & Text
-------------------------------

Additional elements can be embedded in text fields. This can include:

* Buttons, to provide actions, such as clear.
* Icons, to provide additional information, such as a :doc:`progress spinner </feedback/spinners>`.
* Placeholder text, as an alternative to a field label, in situations where there is little available space, or where a label would disrupt the overall visual layout.

These conventions should generally be used with restraint and according to established conventions. Embedded icons should not be relied upon to identify a text field, and should only be used when their meaning is commonly recognized without the need for additional explanation (such as through a tooltip).

Embedded icons should use the :doc:`symbolic style </guidelines/ui-icons>`.

Password Fields
---------------

Password fields are a special type of text field which hide any entered text. They include a  control for revealing hidden content, and indicate if *Caps Lock* is on, and can be used for any potentially sensitive text.

A password field example can be found in the *Entry → Password Entry* demo in the GTK 4 demo app.

Automatic Suggestions
---------------------

If possible, it is helpful to suggest potential text to be entered as the user types into a text field. For example, an address field can show previous locations as the user types. This reduces the amount of work for users and reduces errors.

An example of automatic suggestions can be found in the *Entry → Completion* example in the GTK 4 demo app.

Tags
----

Tags or tokens are a typical convention for some types of text field. For example, the *To* field in an email app will often display each recipient as a tag. This aids readability and makes it easy to remove each item from the field.

Currently, entry tags require a custom implementation. However, the GTK 4 demo application does include an example under *Entry → Tagged Entry*.

API Reference
-------------

* `GTK 4: GtkEntry <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.Entry.html>`_
* `GTK 4: GtkTextView <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.TextView.html>`_
* `GTK 4: GtkPasswordEntry <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.PasswordEntry.html>`_
* `GTK 3: GtkEntry <https://developer.gnome.org/gtk3/stable/GtkEntry.html>`_
* `GTK 3: GtkTextView <https://developer.gnome.org/gtk3/stable/GtkTextView.html>`_
