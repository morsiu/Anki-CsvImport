# -*- coding: utf-8 -*-
"Allows adding notes stored in mass files to Anki collections"

class MassFile(object):
    "Represents file containing notes, of many decks and note types"
    def __init__(self, file_, note_maps_by_names):
        self.file = file_
        self.note_maps_by_names = note_maps_by_names

    def notes(self):
        "Returns sequence of notes read from the file"
        for record in self.file.records():
            for note in MassRecord(record, self.note_maps_by_names).notes():
                yield note

class MassRecord(object):
    "Represents a record in mass file, containing multiple notes"
    def __init__(self, record, note_maps_by_names):
        self.record = record
        self.note_maps_by_names = note_maps_by_names

    def notes(self):
        "Returns notes contained within the record"
        return self.note_map().notes(self.record.fields())

    def note_map(self):
        "Returns note map assigned to this record"
        return self.note_maps_by_names[self.record.fields()[0].value()]

class NotesMap(object):
    "Represents a mapping from record fields to notes"
    def __init__(self, note_maps):
        self.note_maps = note_maps

    def notes(self, record_fields):
        "Returns notes contained within the record"
        return [note_map.note(record_fields) for note_map in self.note_maps]

class NoteMap(object):
    "Represents a mapping from record fields to note"
    def __init__(self, fields_map, deck, model):
        self.fields_map = fields_map
        self.deck = deck
        self.model = model

    def note(self, record_fields):
        "Returns note obtained from record fields"
        return Note(
            self.fields_map.note_fields(record_fields),
            self.deck,
            self.model)

class NoteFieldsMap(object):
    "Represent a mapping from record fields to fields of a note"
    def __init__(self, note_field_maps):
        self.note_field_maps = note_field_maps

    def note_fields(self, record_fields):
        "Returns field values of note, keyed by field names"
        return [
            note_field_map.note_field(record_fields)
            for note_field_map
            in self.note_field_maps]

class NoteFieldMap(object):
    "Represents a map of record field value to note field value"
    def __init__(self, name, value_index_in_record_fields):
        self.name = name
        self.value_index_in_record_fields = value_index_in_record_fields

    def note_field(self, record_fields):
        "Returns a note field obtained from record fields"
        return NoteField(self.name, record_fields[self.value_index_in_record_fields].value())

class Deck(object):
    "Represents a deck"
    def __init__(self, name):
        self.name_ = name

    def name(self):
        "Returns name of the deck"
        return self.name_

class NoteModel(object):
    "Represents a note model (type)"
    def __init__(self, name):
        self.name_ = name

    def name(self):
        "Returns name of the model"
        return self.name_

class Note(object):
    "Represents a note"
    def __init__(self, fields, deck, model):
        self.fields = fields
        self.deck = deck
        self.model = model

    def add_to_anki_collection(self, anki_collection):
        "Adds note to the anki collection"
        anki_deck_id = anki_collection.decks.id(self.deck.name(), False)
        anki_collection.decks.select(anki_deck_id)
        anki_model = anki_collection.models.byName(self.model.name())
        anki_collection.models.setCurrent(anki_model)
        anki_note = anki_collection.newNote()
        for field in self.fields:
            field.fill(anki_note)
        anki_collection.addNote(anki_note)

class NoteField(object):
    "Represent a note field, with name and value"
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def fill(self, mapping):
        "Stores the field name and value in a mapping"
        mapping[self.name] = self.value

