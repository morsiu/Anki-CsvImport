# -*- coding: utf-8 -*-
"Package for importing notes from CSV files into Anki"
from aqt import mw
import aqt.qt
from .anki import AnkiNoteCollection
from .csvnotefiles import CsvNoteFile
from .jsonnotemapfiles import JsonNoteMapFile

config = mw.addonManager.getConfig(__name__)


def csv_import():
    note_map_file = JsonNoteMapFile(config["note_maps"])
    note_file = CsvNoteFile(config["notes"], note_map_file.notes_maps())
    collection = AnkiNoteCollection(mw.col)
    for note in note_file.notes():
        collection.add_note(note)


action = aqt.qt.QAction("CSV import", mw)
action.triggered.connect(csv_import)
mw.form.menuCol.addAction(action)
