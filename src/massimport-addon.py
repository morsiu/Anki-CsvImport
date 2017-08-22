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
                    NoteFieldMap(u"Artikel", 1),
                    NoteFieldMap(u"Deutsch", 2),
                    NoteFieldMap(u"Deutsch Plural", 3),
                    NoteFieldMap(u"Polski", 4),
                    NoteFieldMap(u"Polski Plural", 5)
                ]),
                Deck(u"Deutsch::Wörter"),
                NoteModel(u"Deutsch Substantiv")
            )]
        ),
        "da": NotesMap(
            [NoteMap(
                NoteFieldsMap([
                    NoteFieldMap(u"Front", 1),
                    NoteFieldMap(u"Back", 2)
                ]),
                Deck(u"Deutsch::Aussprache"),
                NoteModel(u"Deutsch Aussprache")
            )]
        ),
        "dv": NotesMap(
            [NoteMap(
                NoteFieldsMap([
                    NoteFieldMap(u"Deutsch Infinitiv", 1),
                    NoteFieldMap(u"Polski", 2)
                ]),
                Deck(u"Deutsch::Wörter"),
                NoteModel(u"Deutsch Verb")
            )]
        ),
        "dsv": NotesMap(
            [NoteMap(
                NoteFieldsMap([
                    NoteFieldMap(u"Deutsch Infinitiv", 1),
                    NoteFieldMap(u"Deutsch Präsens", 2),
                    NoteFieldMap(u"Deutsch Präteritum", 3),
                    NoteFieldMap(u"Deutsch Partizip II", 4),
                    NoteFieldMap(u"Polski", 5)
                ]),
                Deck(u"Deutsch::Wörter"),
                NoteModel(u"Deutsch Verb")
            )]
        ),
        "def": NotesMap(
            [NoteMap(
                NoteFieldsMap([
                    NoteFieldMap(u"Deutsch", 1),
                    NoteFieldMap(u"Polski", 2)
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