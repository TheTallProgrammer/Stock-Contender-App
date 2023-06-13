from packages.frontend.main_ui import init_window

def main():
    init_window()

if __name__ == "__main__":
    main()
    
    
# TO DO
# Whenever the user clicks one of the option buttons, they all turn unclickable until the result is completed. Once the result is completed, destroy that instance of the gpt model and allow the buttons to be clicked again.  re-run the new model with the already inserted api key when another option is clicked.

# Work on implementing the progress bar