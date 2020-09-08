# -*- coding: utf-8 -*-
"Package for importing notes from mass files into Anki"
from aqt import mw
import aqt.qt
from .massfiles import *
from .csvfiles import CsvFile
from .collections import AnkiNoteCollection

def note_maps():
    return {
        "jph": NotesMap(
            [NoteMap(
                NoteFieldsMap([
                    NoteFieldMap(u"Front", 1),
                    NoteFieldMap(u"Back", 2)
                ]),
                Deck(u"Japanese::Hiragana"),
                NoteModel(u"Basic (and reversed card)")
            )]
        ),
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
        "dsubsp": NotesMap(
            [NoteMap(
                NoteFieldsMap([
                    NoteFieldMap(u"Artikel", 1),
                    NoteFieldMap(u"Deutsch", 2),
                    NoteFieldMap(u"Deutsch Plural", 3),
                    NoteFieldMap(u"Polski Plural", 4)
                ]),
                Deck(u"Deutsch::Wörter"),
                NoteModel(u"Deutsch Substantiv Plural")
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
            ]),
        "dsatz": NotesMap(
            [NoteMap(
                NoteFieldsMap([
                    NoteFieldMap(u"Text", 1),
                ]),
                Deck(u"Deutsch::Sätze"),
                NoteModel(u"Cloze"))
            ]),
        "ew": NotesMap(
            [NoteMap(
                NoteFieldsMap([
                    NoteFieldMap(u"Word", 1),
                    NoteFieldMap(u"Explanation", 2),
                    NoteFieldMap(u"Pronunciation", 3)
                ]),
                Deck(u"English::Words"),
                NoteModel(u"English Word"))
            ]),
        "epv": NotesMap(
            [NoteMap(
                NoteFieldsMap([
                    NoteFieldMap(u"Text", 1),
                    NoteFieldMap(u"Extra", 2)
                ]),
                Deck(u"English::Words"),
                NoteModel(u"English Phrasal Verb"))
            ]),
        "eph": NotesMap(
            [NoteMap(
                NoteFieldsMap([
                    NoteFieldMap(u"Front", 1),
                    NoteFieldMap(u"Back", 2)
                ]),
                Deck(u"English::Phrases"),
                NoteModel(u"Basic (and reversed card)")
            )])
    }

def mass_import():
    mass_file = \
        MassFile(
            CsvFile(u"C:\\Users\\z6lum\\Desktop\\PRIVATE\\OneDrive\\Projects\\Słówka do Anki\\notes.csv"),
            note_maps())
    collection = AnkiNoteCollection(mw.col)
    for note in mass_file.notes():
        collection.add_note(note)

action = aqt.qt.QAction("Mass import", mw)
action.triggered.connect(mass_import)
mw.form.menuCol.addAction(action)