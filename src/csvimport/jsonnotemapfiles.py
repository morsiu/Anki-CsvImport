# -*- coding: utf-8 -*-
"Allows reading note maps from JSON files"

from .model import Deck, NoteFieldMap, NoteFieldsMap, NoteMap, NotesMap, NoteModel
import json


class JsonNoteMapFile(object):
    "Represents note maps stored in JSON file"

    def __init__(self, filepath):
        self.filepath = filepath

    def notes_maps(self):
        "Returns note maps read from file"
        with open(self.filepath, 'r', encoding='utf_8') as _file:
            notes_maps_dict = json.load(_file)
            return {key: self.notes_map(note_map_array)
                    for key, note_map_array in notes_maps_dict.items()}

    def notes_map(self, note_map_array):
        "Maps array of note maps to a NotesMap"
        return NotesMap([self.note_map(note_map_dict)
                         for note_map_dict in note_map_array])

    def note_map(self, note_map_dict):
        "Maps note map dict to a NoteMap"
        return NoteMap(
            self.note_fields_map(note_map_dict["fields"]),
            Deck(note_map_dict["deck"]),
            NoteModel(note_map_dict["note_model"])
        )

    def note_fields_map(self, note_field_array):
        "Maps array of note field maps to a NoteFieldsMap"
        return NoteFieldsMap([self.note_field_map(note_field_dict)
                              for note_field_dict in note_field_array])

    def note_field_map(self, note_field_dict):
        "Maps field map to a NoteFieldMap"
        return NoteFieldMap(note_field_dict["name"], note_field_dict["index"])
