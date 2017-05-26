"Mass note import addon to Anki"
# -*- coding: utf-8 -*-
from aqt import mw
import aqt.qt
from massfiles import *

def note_maps():
    return {
        "dsubs": NotesMap(
            [NoteMap(
                NoteFieldsMap([
                    NoteFieldMap(u"Polski", 1),
                    NoteFieldMap(u"Polski Plural", 2),
                    NoteFieldMap(u"Artikel", 3),
                    NoteFieldMap(u"Deutsch", 4),
                    NoteFieldMap(u"Deutsch Plural", 5)
                ]),
                Deck(u"Deutsch::Wörter"),
                NoteModel(u"Deutsch Substantiv"))
            ]),
        "da": NotesMap(
            [NoteMap(
                NoteFieldsMap([
                    NoteFieldMap(u"Front", 1),
                    NoteFieldMap(u"Back", 2)
                ]),
                Deck(u"Deutsch::Aussprache"),
                NoteModel(u"Deutsch Aussprache")
            )]
        )
    }

def mass_import():
    anki_collection = mw.col
    mass_file = MassFile(u"C:\\users\\morsk\\Documents\\Słówka\\notes.csv", note_maps())
    for note in mass_file.notes():
        note.add_to_anki_collection(anki_collection)

action = aqt.qt.QAction("Mass import", mw)
action.triggered.connect(mass_import)
mw.form.menuCol.addAction(action)