# -*- coding: utf-8 -*-
"Package for importing notes from mass files into Anki"
from aqt import mw
import aqt.qt
from .massfiles import *
from .csvfiles import CsvFile
from .collections import AnkiNoteCollection
from .notemapfiles import NoteMapJsonFile


def notes_maps():
    file = NoteMapJsonFile(
        u"C:\\Users\\morsk\\OneDrive\\Projects\\Słówka do Anki\\note_maps.json")
    return file.notes_maps()


def mass_import():
    mass_file = \
        MassFile(
            CsvFile(
                u"C:\\Users\\morsk\\OneDrive\\Projects\\Słówka do Anki\\notes.csv"),
            notes_maps())
    collection = AnkiNoteCollection(mw.col)
    for note in mass_file.notes():
        collection.add_note(note)


action = aqt.qt.QAction("Mass import", mw)
action.triggered.connect(mass_import)
mw.form.menuCol.addAction(action)
