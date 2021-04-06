Writing Style
=============

Text plays an important role in user interfaces. Take the time to ensure that any text you use is clearly written and easy to understand.

Guidelines
##########

Your main goal should be to ensure that text is easy to understand and quick to read.

* Keep text short and to the point. This improves speed of comprehension for the user. It also reduces the expansion of text when translated (remember that translated English text can expand up to 30% in some languages).
* Do not shorten your text to the point of losing meaning. A three-word label that provides clear information is better than a one-word label that is ambiguous or vague. Try to find the fewest possible words to satisfactorily convey the meaning of your label.
* Use words, phrases, and concepts that are familiar to the people who will be using your application, rather than terms from the underlying system. This may mean using terms that are associated with the tasks your application supports. For example, in medicine, the paper folder that contains patient information is called a “chart”. Hence, a medical application might refer to a patient record as a “chart” rather than as a “patient database record”.
* Text should adopt a neutral tone and speak from the point of view of the product. Pronouns like “you” or “my” should therefore be avoided wherever possible. However, if they are unavoidable “your” is preferable to “my”.
* Use the standard GNOME terms when referring to parts of the user interface, such as “pointer” and “window”. The HIG can be used as a reference in this regard.
* Avoid repetition where possible.
* Sentences should not be constructed from text in several controls, and each label should be treated as being self-contained. Sentences that run from one control to another will often not make sense when translated into other languages.
* Latin abbreviations such as “i.e.” or “e.g.” should be avoided, since they can't always be easily translated and can be unintelligible when read by screen readers. Instead, use full words like “for example”.

Capitalization
##############

Two styles of capitalization are used in GNOME user interfaces: header capitalization and sentence capitalization.

.. _header-capitalization:

Header capitalization
*********************

Header capitalization should be used for any headings, including header bar headings and page, tab and menu titles. It should also be used for short control labels that do not normally form proper sentences, such as button labels, switch labels and menu items.

Capitalize the first letter of:

* All words with four or more letters.
* Verbs of any length, such as “Be”, “Are”, “Is”, “See” and “Add”.
* The first and last word.
* Hyphenated words; for example: “Self-Test” or “Post-Install”.

For example: “Create a Document”, “Find and Replace”, “Document Cannot Be Found”.

Sentence capitalization
***********************

Sentence capitalization should be used for labels that form sentences or that run on to other text, including labels for check boxes, radio buttons, sliders, text entry boxes, field labels and combobox labels. It should also be used for explanatory or body text, such as in dialogs or notifications.

Capitalize the first letter of:

* The first word.
* Any words normally capitalized in sentences, such as proper nouns.

For example: “The document cannot be found in this location.” “Finding results for London.”

.. _ellipses:

Ellipses (…)
############

Use an ellipsis (…) at the end of a label if further input or confirmation is required from the user before the action can be carried out. For example, *Save As…*, *Find…* or *Delete…*.

Do not add an ellipsis to labels such as *Properties* or *Preferences*. While these commands open windows that can incorporate further functionality, the label does not specify an action, and therefore does not need to communicate that further input or confirmation is required.
