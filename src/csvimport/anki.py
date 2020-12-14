# -*- coding: utf-8 -*-
"Allows addition of notes to an Anki collection"


class AnkiNoteCollection(object):
    "Represents an Anki note collection"

    def __init__(self, anki_collection):
        self.anki_collection = anki_collection

    def add_note(self, note):
        "Adds note to the anki collection"
        anki_deck_id = self.anki_collection.decks.id(note.deck().name(), False)
        if anki_deck_id is None:
            raise Exception(
                "Could not find deck with name {0}".format(note.deck().name()))
        anki_model = self.anki_collection.models.byName(note.model().name())
        if anki_model is None:
            raise Exception(
                "Could not find note type with name {0}".format(note.model().name()))
        anki_model['did'] = anki_deck_id
        self.anki_collection.models.setCurrent(anki_model)
        anki_note = self.anki_collection.newNote(False)
        if anki_note is None:
            raise Exception("Could not create note for deck {0} and note type {1}"
                            .format(note.deck().name(), note.model().name()))
        for field in note.fields():
            anki_note[field.name()] = field.value()
        if anki_note.dupeOrEmpty() == 0:
            self.anki_collection.addNote(anki_note)


class AnkiDeck(object):
    "Represents an Anki deck"

    def __init__(self, name):
        self.name_ = name

    def name(self):
        "Returns name of the deck"
        return self.name_


class AnkiNoteModel(object):
    "Represents an Anki note model (type)"

    def __init__(self, name):
        self.name_ = name

    def name(self):
        "Returns name of the model"
        return self.name_


class AnkiNote(object):
    "Represents an Anki note"

    def __init__(self, fields, deck, model):
        self.fields_ = fields
        self.deck_ = deck
        self.model_ = model

    def fields(self):
        "Returns fields of the note"
        return self.fields_

    def deck(self):
        "Returns deck to which the note belongs"
        return self.deck_

    def model(self):
        "Returns model of the note"
        return self.model_


class AnkiNoteField(object):
    "Represent an Anki note field, with name and value"

    def __init__(self, name, value):
        self.name_ = name
        self.value_ = value

    def name(self):
        "Returns name of the field"
        return self.name_

    def value(self):
        "Returns value of the field"
        return self.value_
