"""
pip install bibtexparser

Picks a .bib file and strips the fields in FIELDS_TO_REMOVE.
If DOT_BIB_DIR_INPUT points to an invalid file, a file with DOT_BIB_DIR_DEFAULT is created with default bib content and gets inputted instead.
Either way, result gets saved into DOT_BIB_DIR_OUTPUT.
"""

from typing import Iterable
import bibtexparser as btp
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

# PARAMETERS
DOT_BIB_DIR_INPUT = 'refs.bib'
DOT_BIB_DIR_OUTPUT = 'edited_refs.bib'
FIELDS_TO_REMOVE = {'abstract', 'keywords', 'file'}
DOT_BIB_DIR_DEFAULT = 'default.bib'

def generate_default_bib () -> None:
    bibtex = """@ARTICLE{Doe2000,
 author = {John Doe},
 title = {This is a title},
 year = {2000},
 month = {jan},
 volume = {2},
 pages = {1--99},
 journal = {Scientific Journal of Science},
 abstract = {abstract which should be removed},
 keywords = {useless keyword1, useless keyword2},
 file = {:D$\\backslash$:/Documents/Title.pdf:pdf}
}
    """

    with open(DOT_BIB_DIR_DEFAULT, 'w') as bibfile:
        bibfile.write(bibtex)

def load_database_from_bib (dir : str) -> BibDatabase:
    dir += '' if dir.endswith('.bib') else '.bib'
    try:
        with open(dir) as refs:
            database = btp.load(refs)
    except FileNotFoundError:
        generate_default_bib()
        database = load_database_from_bib(DOT_BIB_DIR_DEFAULT)

    return database

def save_database_to_bib (database : BibDatabase, dir : str) -> None:
    dir += '' if dir.endswith('.bib') else '.bib'
    writer = BibTexWriter()
    with open(dir, 'w') as bibfile:
        bibfile.write(writer.write(database))

def remove_fields (database : BibDatabase, fields_to_remove : Iterable) -> None:
    for entry in database.entries:
        for field in fields_to_remove:
            try:
                entry.pop(field)
            except KeyError:
                pass

if __name__ == '__main__':
    print(f"Loading '{DOT_BIB_DIR_INPUT}' into database...")
    database = load_database_from_bib(DOT_BIB_DIR_INPUT)
    print("Removing fields: ", *["'"+i+"'" for i in FIELDS_TO_REMOVE],"...")
    remove_fields(database, FIELDS_TO_REMOVE)
    print(f"Saving database into '{DOT_BIB_DIR_OUTPUT}'...")
    save_database_to_bib(database, DOT_BIB_DIR_OUTPUT)