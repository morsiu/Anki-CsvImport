# -*- coding: utf-8 -*-
"Allows reading csv files"
import csv

class CsvFile(object):
    "Represents file containing records, in csv format, consisting of fields"
    def __init__(self, filepath):
        self.filepath = filepath

    def records(self):
        "Returns sequence of records read from the file"
        with open(self.filepath, 'r', encoding='utf_8', newline='') as _file:
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
