# Copyright 2023 Logan Falkenberg
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from PyQt5.QtCore import pyqtSignal, QObject

# This class will be responsible for managing the progress bar and receiving updates from different parts of the application, follows the singleton pattern
class ProgressTracker(QObject):
    _instance = None
    update_progress = pyqtSignal(int) # this is essentially a middle-man, it routes an int value, which is whatever iteration is the signal has been called, to whatever slot is connected to it

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super(ProgressTracker, cls).__new__(cls)
            cls._instance.current_progress = 0
        return cls._instance

    def register_task(self): 
        self.current_progress += 1
        self.update_progress.emit(self.current_progress) # emits the new progress value
        
    def reset(self):
        self.current_progress = 0