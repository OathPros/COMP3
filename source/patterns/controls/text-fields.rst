Text Fields
===========

.. image:: /img/screenshots/text-fields.png

Text fields are used for single line text entry and editing.

Guidelines
----------

General guidelines for text fields:

* Give text fields a label using :ref:`header capitalization <header-capitalization>`, and assign an access key to the label, to allow people to focus the control using a keyboard.
* If there is a little available space, or a label would disrupt the overall visual layout, placeholder text can be shown inside the field instead of using a label.
* Size text fields according to the likely size of the content they will contain. This gives a useful visual cue to the amount of expected input.
* When a text field contains a property or setting, apply any changes when Return is pressed or when the field loses focus.
* Buttons and icons can be embedded inside text fields. This can be helpful to provide feedback (for example, a spinner to indicate progress) or common actions (for example, a clear button). Embedded buttons and icons should use the :doc:`symbolic style </guidelines/ui-icons>`.

Text Validation
---------------

Text fields can often require their content to have a particular format, such as in the case of a URL or hex color value. In these cases, it is important to provide effective feedback.

When doing this, it is generally better to show positive feedback when the content is valid, as opposed to showing negative feedback while it is invalid. This avoids distracting and confusing users while they are in the process of editing the field.

It is often better to show feedback in real time as the field is edited, as opposed to waiting until the field loses focus.
  
Password Fields
---------------

Password fields are a special type of text field for which GNOME provides `a dedicated control <https://docs.gtk.org/gtk4/class.PasswordEntry.html>`_. This hides entered text, which can be revealed with a button, and can be used for any potentially sensitive text.

A password field example can be found in the *Entry → Password Entry* demo in the GTK 4 demo app.

Automatic Suggestions
---------------------

It is often helpful to suggest potential text to be entered as the user types into a text field. For example, an address field can show previous locations as the user types. This reduces the amount of work for users and reduces errors.

An example of automatic suggestions can be found in the *Entry → Completion* example in the GTK 4 demo app.

Tags
----

Tags or tokens are a typical convention for some types of text field. For example, the *To* field in an email app will often display each recipient as a tag. This aids readability and makes it easy to remove each item from the field.

Currently, entry tags require a custom implementation. However, the GTK 4 demo application does include an example under *Entry → Tagged Entry*.

API Reference
-------------

* `GTK 4: GtkEntry <https://docs.gtk.org/gtk4/class.Entry.html>`_
* `GTK 4: GtkTextView <https://docs.gtk.org/gtk4/class.TextView.html>`_
* `GTK 4: GtkPasswordEntry <https://docs.gtk.org/gtk4/class.PasswordEntry.html>`_
* `GTK 3: GtkEntry <https://docs.gtk.org/gtk3/class.Entry.html>`_
* `GTK 3: GtkTextView <https://docs.gtk.org/gtk3/class.TextView.html>`_
