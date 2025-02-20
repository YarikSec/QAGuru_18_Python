import os
from zipfile import ZipFile
import pytest
from pypdf import PdfReader
from xlrd import open_workbook # Для xls
from openpyxl import load_workbook # Для xlsx

from homework_7.tests.conftest import RES_DIR

# TODO: задание 7 урока
"""
 – Запаковать кодом в zip архив несколько разных файлов: pdf, xlsx, csv;

 – Положить его в ресурсы;

 – Реализовать чтение и проверку содержимого каждого файла из архива не распаковывая сам архив
"""

def test_read_all_files_zip():
    zip_path = os.path.join(RES_DIR, 'test.zip')

    with ZipFile(zip_path) as zip_file:

        csv = zip_file.read("file_example_XLS.csv").decode("utf-8")
        assert "First Name" in csv

        xls_content = zip_file.read("file_example_XLS_10.xls")
        xls_workbook = open_workbook(file_contents=xls_content)
        assert xls_workbook is not None

        with zip_file.open("file_example_XLSX_50.xlsx") as xlsx:
            xlsx_workbook = load_workbook(xlsx)
            assert xlsx_workbook is not None

        with zip_file.open("Python Testing with Pytest (Brian Okken).pdf") as pdf:
            reader = PdfReader(pdf)
            # assert "Simple, Rapid, Effective, and Scalable" in reader.pages[0].extract_text()
            assert len(reader.pages) == 256

        # xlsx_content = zip_file.read("file_example_XLSX_50.xlsx")
        # xlsx_workbook = load_workbook(xlsx_content)
        # assert xlsx_workbook is not None
        #
        # pdf = zip_file.read("Python Testing with Pytest (Brian Okken).pdf")
        # reader = PdfReader(pdf)
        # assert "Simple, Rapid, Effective, and Scalable" in reader.page[0]



    