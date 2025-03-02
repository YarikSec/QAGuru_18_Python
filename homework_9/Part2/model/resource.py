import os
import homework_9.Part2.tests as tests


def path(file_name):
    return os.path.abspath(
        os.path.join(os.path.dirname(tests.__file__), f'../resources/{file_name}')
    )