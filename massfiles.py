"Allows adding notes stored in mass files to Anki collections"
import csv

class MassFile(object):
    "Represents file containing notes, of many decks and note types"
    def __init__(self, filepath, note_maps_by_names, anki_collection):
        self.filepath = filepath
        self.note_maps_by_names = note_maps_by_names
        self.anki_collection = anki_collection

    def notes(self):
        "Returns sequence of notes read from the file"
        for record in CsvFile(str(self.filepath)).records():
            for note in MassRecord(record, self.note_maps_by_names, self.anki_collection).notes():
                yield note

class MassRecord(object):
    "Represents a record in mass file, containing multiple notes"
    def __init__(self, record, note_maps_by_names, anki_collection):
        self.record = record
        self.note_maps_by_names = note_maps_by_names
        self.anki_collection = anki_collection

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
    def __init__(self, fields_map, deck, model, anki_collection):
        self.fields_map = fields_map
        self.deck = deck
        self.model = model
        self.anki_collection = anki_collection

    def note(self, record_fields):
        "Returns note obtained from record fields"
        return Note(
            self.fields_map.note_fields(record_fields),
            self.deck,
            self.model,
            self.anki_collection)

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
        return NoteField(self.name, record_fields[self.value_index_in_record_fields])

class Deck(object):
    "Represents a deck"
    def __init__(self, name, anki_collection):
        self.name = name
        self.anki_collection = anki_collection

    def anki_deck(self):
        "Returns an anki deck for this deck"
        return self.anki_collection.decks.byName(self.name)

class NoteModel(object):
    "Represents a note model (type)"
    def __init__(self, name, anki_collection):
        self.name = name
        self.anki_collection = anki_collection

    def anki_model(self):
        "Returns an anki model for this model"
        return self.anki_collection.models.byName(self.name)

class Note(object):
    "Represents a note"
    def __init__(self, fields, deck, model, anki_collection):
        self.fields = fields
        self.deck = deck
        self.model = model
        self.anki_collection = anki_collection

    def add_to_anki_collection(self):
        "Adds note to the anki collection"
        anki_deck = self.deck.anki_deck()
        anki_model = self.model.anki_model()
        self.anki_collection.models.setCurrent(anki_model)
        anki_note = anki_deck.newNote()
        self.fields.fill(anki_note)
        anki_deck.addNote(anki_note)

class NoteField(object):
    "Represent a note field, with name and value"
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def fill(self, mapping):
        "Stores the field name and value in a mapping"
        mapping[self.name] = self.value

class CsvFile(object):
    "Represents file containing records, in csv format, consisting of fields"
    def __init__(self, filepath):
        self.filepath = filepath

    def records(self):
        "Returns sequence of records read from the file"
        with open(str(self.filepath), 'rb') as _file:
            for fields in csv.reader(_file):
                yield CsvRecord([CsvField(field) for field in fields])

class CsvRecord(object):
    "Represents a csv record, consisting of fields"
    def __init__(self, fields):
        self._fields = fields

    def fields(self):
        "Returns fields contained in the record"
        return self._fields

class CsvField(object):
    "Represents a csv field, containing a value"
    def __init__(self, value):
        self._value = value

    def value(self):
        "Returns value contained within the field"
        return self._value
