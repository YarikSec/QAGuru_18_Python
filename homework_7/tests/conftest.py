import os.path
import zipfile
import pytest
from zipfile import ZipFile

PROJECT_PATH_HW7 = "/Users/yarik/PycharmProjects/QAGuru_18_Python/homework_7"
TMP_DIR = os.path.join(PROJECT_PATH_HW7, "tmp")
TESTS_DIR = os.path.join(PROJECT_PATH_HW7, "tests")
print(TESTS_DIR)
RES_DIR = os.path.join(TESTS_DIR, "resources")


@pytest.fixture(scope="function", autouse=True)
def zip_archive_ex():
    if not os.path.exists(RES_DIR):
        os.makedirs(RES_DIR)

    file_dir = os.listdir(TMP_DIR)

    zip_path = os.path.join(RES_DIR, 'test.zip')

    with zipfile.ZipFile(zip_path, mode='w',
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for file in file_dir:
            add_file = os.path.join(TMP_DIR, file)
            zf.write(add_file, arcname=file)

    yield

    if os.path.exists(zip_path):
        os.remove(zip_path)