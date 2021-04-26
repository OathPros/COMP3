Typography
==========

Text is an important part of any user interface. Text size, positioning and weight all contribute to the ability for text to convey information effectively, and also play an important role in creating a beautiful appearance.

Default Fonts
-------------

Wherever possible, use the default system fonts as provided by the distribution or operating system on which your application is running. In GNOME, the default font is Cantarell, which was originally designed and developed by David Crossland.

Variants, Sizes & Weights
-------------------------

Different text weights and colors can and should be used to distinguish different kinds of information. At the same time, too many variants, sizes, and weights can make text harder to read and isn't an efficient or elegant way to convey information. Make an effort to minimize the range of font variants, sizes and weights.

* Use smaller and/or lighter text for less important information, and heavier/darker text to attract attention to important text.
* Avoid the use of italic or oblique faces, as these are visually more complex, and can be distracting.
* Do not capitalize every letter in a word or sentence. Shouting at your users isn't nice.
* Do not use graphical backdrops or “watermarks” behind text. These interfere with the contrast between the text and its background.

Standard Font Styles
--------------------

GNOME has a set of standard font styles which are recommended for use in apps. These can be found in the `Typography <https://flathub.org/apps/details/org.gnome.design.Typography>`_ app, which displays the styles and indicates the corresponding CSS style classes.

.. list-table::
  :widths: 15 15 70
  :header-rows: 1

  * - Style Name
    - CSS Class
    - Guidance
  * - Body
    - ``body``
    - The default text style, which is used for control labels and descriptive UI text.
  * - Heading
    - ``heading``
    - The standard style for UI headings, such as window titles, and headings for groups of controls.
  * - Caption & Caption Heading
    - ``caption`` & ``caption-heading``
    - Small text styles, generally used to differentiate sub-text which accompanies text in the regular ``body`` style.
  * - Title
    - ``large-title``
    - The largest style, infrequently used for display headings in greeters or assistants. Should only be used in conjunction with large amounts of white space.
  * - Title 1–4
    - ``title-1``–``title-4``
    - A range of heading styles, which can be used for display, including placeholder and welcome graphics.

Note: these standard font styles are available in GTK 4 and not GTK 3.

Take Advantage of Unicode
-------------------------

Unicode provides a wide variety of characters which, when used correctly, can dramatically improve the impression given by your application. The following Unicode characters are recommended:

.. list-table::
  :widths: 20 20 20 40
  :header-rows: 1
  
  * - Usage
    - Incorrect
    - Correct
    - Unicode to use
  * - Quotation
    - \"quote\"
    - “quote”
    - U+201C LEFT DOUBLE QUOTATION MARK, U+201D RIGHT DOUBLE QUOTATION MARK
  * - Time
    - 4:20
    - 4∶20
    - U+2236 RATIO
  * - Multiplication
    - 1024x768
    - 1024×768
    - U+00D7 MULTIPLICATION SIGN
  * - Ellipsis
    - Introducing...
    - Introducing…
    - U+2026 HORIZONTAL ELLIPSIS
  * - Apostrophe
    - The user's preferences
    - The user’s preferences
    - U+2019 RIGHT SINGLE QUOTATION MARK
  * - Bullet list
    - \* One
    - \• One
    - U+2022 BULLET
  * - Ranges
    - June-July 1967
    - June–July 1967
    - U+2013 EN DASH

The `Typography <https://flathub.org/apps/details/org.gnome.design.Typography>`_ app provides a convenient way to copy these recommended characters.