from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import pyqtSlot as pyQtSlot
from packages.backend.user_options.option_one_driver import user_option_one_driver
from packages.backend.progress_tracker.global_instance import progress_tracker


# seperates backend operations from frontend operations to prevent unresponsive app
class Worker(QThread):
    update_progress_bar = pyqtSignal(int)
    taskFinished = pyqtSignal(str)  # Signal when the task is done
    taskFailed = pyqtSignal(str)  # Signal when the task fails
    def __init__(self):
        super().__init__()
        self.progress_tracker = progress_tracker
        self.progress_tracker.update_progress.connect(self.update_progress)

    def run(self):
        try:
            response = user_option_one_driver()  # long running task
            # Ensure progress_tracker.register_task() updates the progress value and emits a signal
            progress_tracker.register_task()
            self.taskFinished.emit(response)
        except Exception as e:
            self.taskFailed.emit(str(e))  # emit the error message if an exception occurs
    
    @pyQtSlot(int)
    def update_progress(self, progress):
        self.update_progress_bar.emit(progress)