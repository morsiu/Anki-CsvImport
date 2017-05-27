# -*- coding: utf-8 -*-
"Mass note import addon to Anki"
from aqt import mw
import aqt.qt
from massimport.csvfiles import CsvFile
from massimport.massfiles import MassFile
from massimport.massfiles import NotesMap, NoteMap, NoteFieldsMap, NoteFieldMap
from massimport.massfiles import Deck, NoteModel

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
    anki_collection = mw.col
    mass_file = MassFile(CsvFile(u"C:\\users\\morsk\\Documents\\Słówka\\notes.csv"), note_maps())
    for note in mass_file.notes():
        note.add_to_anki_collection(anki_collection)

action = aqt.qt.QAction("Mass import", mw)
action.triggered.connect(mass_import)
mw.form.menuCol.addAction(action)