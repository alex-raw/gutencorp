import shutil
from typing import Generator
# from rdflib import Graph
import tarfile
import re
import urllib.request
from pathlib import Path
from tempfile import NamedTemporaryFile, TemporaryDirectory

URL = 'https://www.gutenberg.org/cache/epub/feeds/rdf-files.tar.bz2'
CACHE_FILE   = 'gutenbergindex.db'
UNPACK_DIR   = Path('cache', 'epub') # subdirs of unpacked rdf archive
CACHE_FOLDER = 'texts'


def get_cache(keep_rdf: bool) -> None:
    with TemporaryDirectory(dir=".") as dir:
        path = Path(dir) / Path(URL).name
        urllib.request.urlretrieve(URL, path)
        shutil.unpack_archive(path)
        if keep_rdf:
            path.rename(Path().cwd() / path.name)  # move file to cwd


# def create() -> Generator:
#     """Downloads the metadata archive from Project Gutenberg and returns a file
#     pointer to the individual rdf-files with metadata
#     """
#     pg_rdf_regex = re.compile(r'pg\d+.rdf$')
#     with NamedTemporaryFile(dir=".") as metadata_archive:
#         shutil.copyfileobj(urllib.request.urlopen(URL), metadata_archive)
#         with tarfile.open(metadata_archive.name) as metadata_tar:
#             for item in metadata_tar:
#                 if pg_rdf_regex.search(item.name):
#                     parse_rdf(metadata_tar.extractfile(item))


def parse_rdf(rdf_file):
    pass


# def _iter_metadata_triples(metadata_archive_path):
#         """Yields all meta-data of Project Gutenberg texts contained in the
#         catalog dump.
#         """
#         pg_rdf_regex = re.compile(r'pg\d+.rdf$')
#         with tarfile.open(metadata_archive_path) as metadata_archive:
#             for item in metadata_archive:
#                 if pg_rdf_regex.search(item.name):
#                     extracted = metadata_archive.extractfile(item)
#                     graph = Graph().parse(extracted)
#                     for fact in graph:
#                         if _metadata_is_invalid(fact):
#                             logging.info('skipping invalid triple %s', fact)
#                         else:
#                             yield fact


get_cache(keep_rdf=True)




# # results = OldRdf().do()
# # fields1 = [getattr(results.books[666], a) for a in dir(results.books[666]) if not a.startswith('__')]
# # print(fields1)
# #
# results = parse_rdf(UNPACK_DIR)
# fields2 = [getattr(results.books[666], a) for a in dir(results.books[666]) if not a.startswith('__')]
# # print(fields2)
#
# # print(fields1 == fields2)
# #
# #
# print("running 2")
# SQLiteCache().create_cache(results)
#
# print("running 1")
# OldSQLite().create_cache(results)
