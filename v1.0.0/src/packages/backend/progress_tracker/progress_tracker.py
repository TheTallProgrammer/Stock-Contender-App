from PyQt5.QtCore import pyqtSignal, QObject

# This class will be responsible for managing the progress bar and receiving updates from different parts of the application, follows the singleton pattern
class ProgressTracker(QObject):
    _instance = None
    update_progress = pyqtSignal(int)

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super(ProgressTracker, cls).__new__(cls)
            cls._instance.current_progress = 0
        return cls._instance

    def register_task(self): 
        self.current_progress += 1
        self.update_progress.emit(self.current_progress)
        
    def reset(self):
        self.current_progress = 0