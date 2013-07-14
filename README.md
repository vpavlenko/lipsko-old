lipsko
======

lipsko is a Django-based web application which provides a pastebin-like service to prepare and share interlinear texts.  It's mainly designed for linguists and other people interested in foreign languages to help sharing glossed texts with colleagues and friends.

The application is being deployed to Heroku: http://lipsko.herokuapp.com/
Suggested first release should be in the end of July or in August.


Project plan
============

The platform stores Texts.  Every Text has a Title, a Description and Lines.  Every Line belongs to some Layer.  
Every Text also has a Config which specifies
- a number of Lines in the Text,
- every possible Layer for the Text.

A Layer is just a type of a Line. Every Layer has its name, its language and its type.
Suggested names are "lyrics source", "google translation" or "manual glosses".  
The platform will be developed to support the following types of layers in its first version:
- source,
- translation (liberal),
- word-for-word translation,
- morphemes (partitioning of source words),
- gloss (aligned with morpheme partitioning),
- notes.

Information stores as simply as possible.  Morphemes are stored as plain text, duplicating the source.  No pointers, positions of gloss hyphens in source or whatsoever.

In the first release no linking between layer content will be supported.  I.e. no relations like those that Google translation generates.  The only stored connections between data are
- lines of one layer are meant to be of one layer (surely we're joking),
- lines with the same serial number are meant to describe the same stuff,
- two words occupying the same places of lines with the same serial number are meant to be connected if the are from layers of types source/morphemes/word-for-word translation/gloss.

Functionality includes editing, adding new layers and new multilayer lines, publication, fork mechanism.

We wish to have very light server schema and very little backend source.  We really want to store the whole data of one text json-encoded and saved in a single Django TextField.
