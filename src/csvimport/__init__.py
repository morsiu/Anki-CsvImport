# -*- coding: utf-8 -*-
"Package for importing notes from CSV files into Anki"
from aqt import mw
import aqt.qt
from .massfiles import *
from .csvfiles import CsvFile
from .collections import AnkiNoteCollection
from .notemapfiles import NoteMapJsonFile

config = mw.addonManager.getConfig(__name__)


def notes_maps():
    file = NoteMapJsonFile(config["note_maps"])
    return file.notes_maps()


def csv_import():
    csv_file = MassFile(CsvFile(config["notes"]), notes_maps())
    collection = AnkiNoteCollection(mw.col)
    for note in csv_file.notes():
        collection.add_note(note)


action = aqt.qt.QAction("CSV import", mw)
action.triggered.connect(csv_import)
mw.form.menuCol.addAction(action)
