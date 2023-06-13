from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5 .QtCore import *
import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from packages.backend.user_options.user_options import user_options
from packages.backend.user_options.option_one_driver import user_option_one_driver
from packages.backend.gpt_driver.gpt_driver import validate_api_key
from packages.frontend.classes.worker import Worker
from packages.frontend.classes.scroll_label import ScrollLabel
from packages.frontend.resources import resources_rc
from packages.backend.progress_tracker.global_instance import progress_tracker
from PyQt5.QtCore import pyqtSlot as pyQtSlot
from packages.backend.gpt_driver import gpt_driver
import qdarktheme


class Ui_MainWindow_Functions:
    # =================================
    # Backend Communications Functions
    def press_it(self, input):
        if input == 1:
            self.option_1.setEnabled(False)  # Disable the option_1 button
            self.update_output("Contending Stocks...")
            self.worker.start() # starts the worker thread

    def handle_task_finished(self, message):
        self.update_output(message)
        # Always enable the reset button when the task is finished, regardless of the progress value
        self.reset_button.setEnabled(True)

    def handle_task_failed(self, message):
        self.update_output(f"Error: {message}")  # display the error message
        self.option_1.setEnabled(True)  # re-enable the option_1 button
        self.reset_button.setEnabled(False)  # disable the reset button
        
    # Updates the progress bar visual
    @pyQtSlot(int)
    def update_progress(self, value):
        self.progressBar.setValue(value)
    # =================================

    # =================================
    # Output Text Functions

    def update_output(self, message):
        self.output_label.setText(message)

    def activate_button_clicked(self):
        org_id = self.api_key
        try:
            if validate_api_key(org_id): 
                self.option_picker_widget.show()
                self.activate_button.hide()  # Hide the button
                    
                # Get the current sizes
                lineEdit_width = self.api_key_input.width()
                activate_button_width = self.activate_button.width()
                    
                # Calculate new width and set it
                new_width = lineEdit_width + activate_button_width
                self.api_key_input.setFixedWidth(new_width)
                self.api_key_input.setReadOnly(True)
                self.api_key_label.setFixedWidth(new_width)
                    
                # Replace the QLineEdit text with asterisks of the same length as the API key
                self.api_key_input.setText('*' * len(org_id))
                    
                _translate = QtCore.QCoreApplication.translate
                self.api_key_label.setText(_translate("MainWindow", "API KEY accepted"))
                self.update_output("Waiting for option selection...")
        except Exception as e:
            self.api_key = ""  # Clear the api_key
            self.api_key_input.setText("")  # Clear the QLineEdit
            self.update_output(str(e))
                

    def handle_text_changed(self, text):
        if not self.api_key_entry_in_progress:
            if len(text) > len(self.api_key):  # Detects input or paste
                added_text = text[len(self.api_key):]  # Captures new input
                self.api_key += added_text  # Updates api_key
                self.api_key_entry_in_progress = True
                self.api_key_input.setText('*'*(len(text)-1) + text[-1]) # Updates display
                self.api_key_input.setCursorPosition(len(self.api_key))
                self.api_key_entry_in_progress = False
            elif len(self.api_key) > len(text):  # Detects backspace
                self.api_key = self.api_key[:len(text)]  # Trims api_key
                self.api_key_input.setText('*' * len(self.api_key))  # Updates display
                self.api_key_input.setCursorPosition(len(self.api_key))
                
    # This should be added where the reset button event is handled
    def reset_button_clicked(self):
        self.progressBar.setValue(0)  # Reset the progress bar
        self.output_label.setText('Waitng for option...')  # Clear the output
        self.option_1.setEnabled(True)  # Enable the option_1 button
        self.reset_button.setEnabled(False)
        gpt_driver.messages.clear()  # Clear the message history
            # Disconnect the signals
        self.worker.taskFinished.disconnect()
        self.worker.quit()
        self.worker.wait()

        # Create a new instance
        self.worker = Worker()

        # Reconnect the signals
        self.worker.taskFinished.connect(self.update_output)
        self.worker.taskFinished.connect(self.handle_task_finished)
        self.progress_tracker.reset()
    # =================================