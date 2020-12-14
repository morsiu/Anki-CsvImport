# -*- coding: utf-8 -*-
"Allows mapping of records, consisting of fields, to multiple notes"


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
        return NoteField(
            self.name,
            record_fields[self.value_index_in_record_fields].value())


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


class NoteField(object):
    "Represent a note field, with name and value"

    def __init__(self, name, value):
        self.name_ = name
        self.value_ = value

    def name(self):
        "Returns name of the field"
        return self.name_

    def value(self):
        "Returns value of the field"
        return self.value_
