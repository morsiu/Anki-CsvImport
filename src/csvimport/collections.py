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
