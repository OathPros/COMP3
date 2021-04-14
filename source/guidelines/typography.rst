Typography
==========

Text is an important part of any user interface. Text size, positioning and weight all contribute to the ability for text to convey information effectively, and also play an important role in creating a beautiful appearance.

Default Fonts
-------------

Wherever possible, use the default system fonts as provided by the distribution or operating system on which your application is running. In GNOME, the default font is Cantarell, which was originally designed and developed by David Crossland.

Standard Font Styles
--------------------

TODO: add details about this.

Variants, Sizes & Weights
-------------------------

Different text weights and colors can and should be used to distinguish different kinds of information. At the same time, too many variants, sizes, and weights can make text harder to read and isn't an efficient or elegant way to convey information. Make an effort to minimize the range of font variants, sizes and weights.

* Use smaller and/or lighter text for less important information, and heavier/darker text to attract attention to important text.
* Avoid the use of italic or oblique faces, as these are visually more complex, and can be distracting.
* Never capitalize every letter in a word or sentence. Shouting at your users isn't nice.
* Do not use graphical backdrops or “watermarks” behind text. These interfere with the contrast between the text and its background.

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
    - "quote"
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
    - ● One
    - \• One
    - U+2022 BULLET
  * - Ranges
    - June-July 1967
    - June–July 1967
    - U+2013 EN DASH

TODO: describe the Typography app and how to get it.