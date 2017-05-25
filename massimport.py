#from anki.importing import TextImporter
#from anki import Collection
import os.path
import csv

class MassCsvFile(object):
    "Represents file with mass file lines"
    def __init__(self, filename, masstemplates):
        self.filename = filename
        self.masstemplates = masstemplates

    def export(self, csv_note_file_folder):
        for massline in self.masslines():
            massline.export(csv_note_file_folder)

    def masslines(self):
        for csv_file_line in CsvFile(self.filename).lines():
            yield MassCsvLine(csv_file_line, self.masstemplates)

class MassCsvLine(object):
    "Represents a csv line, containing a mass template's name, and a note's values"
    def __init__(self, csv_file_line, masstemplates):
        self.csv_file_line = csv_file_line
        self.masstemplates = masstemplates

    def export(self, csv_note_file_folder):
        self.massnote().export(csv_note_file_folder)

    def massnote(self):
        return MassNote(
            self.masstemplates.masstemplate(
                self.csv_file_line.first_field()),
            self.csv_file_line.after_first_fields())

class MassNote(object):
    "Represents a note, with its field values, type, and deck"
    def __init__(self, masstemplate, notefields):
        self.masstemplate = masstemplate
        self.notefields = notefields

    def export(self, csv_note_file_folder):
        self.csv_note_file(csv_note_file_folder).append(self.notefields)

    def csv_note_file(self, csv_note_file_folder):
        return csv_note_file_folder.csv_note_file(self.massdeck(), self.massnotetype())

    def massdeck(self):
        return self.masstemplate.massdeck()

    def massnotetype(self):
        return self.masstemplate.massnotetype()

class MassDeck(object):
    "Represents a deck through its name"
    def __init__(self, name):
        self.name_ = name

    def name(self):
        return self.name_

class MassNoteType(object):
    "Represents a note type through its name"
    def __init__(self, name):
        self.name_ = name

    def name(self):
        return self.name_

class MassTemplates(object):
    def __init__(self, templates_by_names):
        self.template_by_names = templates_by_names

    "Represents a collection of mass templates, accessible by their names"
    def masstemplate(self, name):
        if name not in self.template_by_names:
            raise Exception('There is no mass template with name "{0}"'.format(name))
        return self.template_by_names[name]

class MassTemplate(object):
    "Represents a note type and deck; identifiable by name"
    def __init__(self, deck_name, note_type_name):
        self.deck_name = deck_name
        self.note_type_name = note_type_name

    def massdeck(self):
        return MassDeck(self.deck_name)

    def massnotetype(self):
        return MassNoteType(self.note_type_name)

class CsvNoteFileFolder(object):
    "Represents a folder with csv files, one per each deck and note type"
    def __init__(self, folderpath):
        self.folderpath = folderpath

    def csv_note_file(self, massdeck, massnotetype):
        return CsvNoteFile(self.csv_note_file_name(massdeck, massnotetype))

    def csv_note_file_name(self, massdeck, massnotetype):
        return CsvNoteFileName(self.folderpath, massdeck, massnotetype)

class CsvNoteFile(object):
    "Represents a csv file, storing notes of specific type and deck"
    def __init__(self, filename):
        self.filename = filename

    def append(self, notefields):
        CsvFile(str(self.filename)).appendline(notefields)
        pass

class CsvNoteFileName(object):
    "Represents file name of a csv note file, which includes deck and note type names"
    def __init__(self, folderpath, massdeck, massnotetype):
        self.folderpath = folderpath
        self.massdeck = massdeck
        self.massnotetype = massnotetype

    def __str__(self):
        # todo - watch out for invalid file names
        return os.path.join(
            self.folderpath,
            "{0}_{1}.csv".format(
                self.massdeck.name().replace(':', '_'),
                self.massnotetype.name()))

class CsvFile(object):
    "Represents a csv file"
    def __init__(self, filename):
        self.filename = filename

    def lines(self):
        with open(self.filename, 'rb') as file:
            for csv_file_line_fields in csv.reader(file):
                yield CsvFileLine(csv_file_line_fields)

    def appendline(self, fields):
        with open(self.filename, 'a+') as file:
            csv.writer(file).writerow(fields)

class CsvFileLine(object):
    "Represents a line in a csv file"
    def __init__(self, fields):
        self.fields = fields

    def first_field(self):
        return self.fields[0]

    def after_first_fields(self):
        return self.fields[1:len(self.fields)]

def run():
    csv_note_file_folder = CsvNoteFileFolder(".")
    mass_templates = MassTemplates(
        {"da" : MassTemplate("Deutsch::Aussprache", "Deutsch Aussprache")})
    mass_csv_file = MassCsvFile("text.csv", mass_templates)
    mass_csv_file.export(csv_note_file_folder)
