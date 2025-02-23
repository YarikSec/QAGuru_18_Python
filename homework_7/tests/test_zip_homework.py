from zipfile import ZipFile
import pytest
from pypdf import PdfReader
from xlrd import open_workbook # Для xls
from openpyxl import load_workbook # Для xlsx

from homework_7.tests.conftest import ZIP_PATH



def test_read_csv_file_zip():
    with ZipFile(ZIP_PATH) as zip_file:
        csv = zip_file.read("file_example_XLS.csv").decode("utf-8")
        assert "First Name" in csv

def test_read_xls_file_zip():
    with ZipFile(ZIP_PATH) as zip_file:
        xls_content = zip_file.read("file_example_XLS_10.xls")
        xls_workbook = open_workbook(file_contents=xls_content)
        assert xls_workbook is not None


def test_read_xlsx_file_zip():
    with ZipFile(ZIP_PATH) as zip_file:
        with zip_file.open("file_example_XLSX_50.xlsx") as xlsx:
            xlsx_workbook = load_workbook(xlsx)
            assert xlsx_workbook is not None

def test_read_pdf_file_zip():
    with ZipFile(ZIP_PATH) as zip_file:
        with zip_file.open("Python Testing with Pytest (Brian Okken).pdf") as pdf:
            reader = PdfReader(pdf)
            # assert "Simple, Rapid, Effective, and Scalable" in reader.pages[0].extract_text()
            assert len(reader.pages) == 256