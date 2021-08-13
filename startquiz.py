import json
import os
from tkinter import *
from tkinter import messagebox as mb
from QuizEngine.Quiz  import Quiz
from QuizEngine.parsers.HTML.htmlmodule import htmlmodule

# Create a GUI Window
gui = Tk()

# set the size of the GUI Window
gui.geometry("800x450")

# set the title of the Window
gui.title("Security+ Quiz")
cwd = os.getcwd()
with open('data.json', 'w') as f:
	json.dump(htmlmodule("Percipio", os.path.join(cwd, "PhysicalSecurity.html")), fp)

# # get the data from the json file
# with open('data.json') as f:
# 	data = json.load(f)

# # set the question, options, and answer
# questions = (data['question'])
# options = (data['options'])
# answers = (data[ 'answer'])

# quiz_Tuple = (questions, options, answers)

# # create an object of the Quiz Class.
# quiz = Quiz(quiz_Tuple, gui)

# # Start the GUI
# gui.mainloop()

# # END OF THE PROGRAM
