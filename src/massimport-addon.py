# -*- coding: utf-8 -*-
"Mass note import addon to Anki"
from aqt import mw
import aqt.qt
from massimport.massfiles import *
from massimport.csvfiles import CsvFile
from massimport.collections import AnkiNoteCollection

def note_maps():
    return {
        "dsubs": NotesMap(
            [NoteMap(
                NoteFieldsMap([
                    NoteFieldMap("Artikel", 1),
                    NoteFieldMap("Deutsch", 2),
                    NoteFieldMap("Deutsch Plural", 3),
                    NoteFieldMap("Polski", 4),
                    NoteFieldMap("Polski Plural", 5)
                ]),
                Deck(u"Deutsch::Wörter"),
                NoteModel(u"Deutsch Substantiv"))
            ]),
        "da": NotesMap(
            [NoteMap(
                NoteFieldsMap([
                    NoteFieldMap("Front", 1),
                    NoteFieldMap("Back", 2)
                ]),
                Deck(u"Deutsch::Aussprache"),
                NoteModel(u"Deutsch Aussprache"))
            ]),
        "def": NotesMap(
            [NoteMap(
                NoteFieldsMap([
                    NoteFieldMap("Deutsch", 1),
                    NoteFieldMap("Polski", 2)
                ]),
                Deck(u"Deutsch::Wörter"),
                NoteModel(u"Deutsch Einfach"))
            ])
    }

def mass_import():
    mass_file = \
        MassFile(
            CsvFile(u"C:\\users\\morsk\\Documents\\Projects\\Słówka do Anki\\notes.csv"),
            note_maps())
    collection = AnkiNoteCollection(mw.col)
    for note in mass_file.notes():
        collection.add_note(note)

action = aqt.qt.QAction("Mass import", mw)
action.triggered.connect(mass_import)
mw.form.menuCol.addAction(action)