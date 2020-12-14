# -*- coding: utf-8 -*-
"Allows reading notes from CSV files"
import csv


class CsvNoteFile(object):
    "Represents file containing records, in CSV format, each consisting of fields"

    def __init__(self, filepath, note_maps_by_names):
        self.filepath = filepath
        self.note_maps_by_names = note_maps_by_names

    def notes(self):
        "Returns sequence of notes read from the CSV file"
        with open(self.filepath, 'r', encoding='utf-8-sig', newline='') as _file:
            for fields_of_line in csv.reader(_file):
                for note in CsvNoteRecord([CsvNoteField(field) for field in fields_of_line], self.note_maps_by_names).notes():
                    yield note


class CsvNoteRecord(object):
    "Represents a record, mapped from fields in a CSV line"

    def __init__(self, fields, note_maps_by_names):
        self.fields = fields
        self.note_maps_by_names = note_maps_by_names

    def notes(self):
        "Returns notes contained within the record"
        return self.note_map().notes(self.fields)

    def note_map(self):
        "Returns note map assigned to this record"
        return self.note_maps_by_names[self.fields[0].value()]


class CsvNoteField(object):
    "Represents a CSV field, containing a value"

    def __init__(self, value):
        self._value = value

    def value(self):
        "Returns value contained within the field"
        return self._value
