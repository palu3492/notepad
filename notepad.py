

import tkinter as tk
import tkinter.scrolledtext as ScrolledText

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        textArea = ScrolledText.ScrolledText(self, width=100, height=100)
        textArea.pack()
        self.pack()

# create the application
notepad = App()

#
# here are method calls to the window manager class
#
notepad.master.title(" Notepad")
notepad.master.maxsize(400, 400)

# start the program
notepad.mainloop()