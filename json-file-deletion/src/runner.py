import os
import sys
import datetime
import traceback

from qt_core import *
from test import division_by_zero

PATH = os.getcwd()

def _run() -> None:
    import model


def run() -> None:
    try:
        _run()
    except Exception as err:
        traceback_exc = sys.exc_info()[2].tb_frame.__str__()
        index_start = traceback_exc.index("\'") + 1
        index_end = traceback_exc.rindex("\'")
        path_to_file = traceback_exc[index_start:index_end]
        path_for_remove = path_to_file.removesuffix(os.path.basename(__file__))
        path_for_remove = path_for_remove.replace('\\\\', '\\')

        datetime_str = f'\n{datetime.datetime.now()}\n'

        with open(os.path.join(PATH, 'stderr.log'), 'a') as log_file:
            log_file.writelines(datetime_str)
            exception_info = traceback.format_exc().replace(path_for_remove, "")
            log_file.write(exception_info)
            log_file.writelines("\n")

        QMessageBox.critical(
            None,
            "Startup Error",
            f"Please notify support of this error:\n\n{traceback.format_exc()}",
        )

if __name__ == "__main__":
    run()
