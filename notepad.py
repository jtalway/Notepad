#!/usr/bin/env python

from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os

class Notepad:
    root = Tk()
    #Win:root.wm_iconbitmap("notepad.ico")
    #Linux:root.wm_iconbitmap("notepad.xbm")
    root.title("Untitled - Notepad")
    root.geometry("700x400")
    TextArea = Text(root, font=("verdana",8))
    menubar = Menu(root)
    FileMenu = Menu(menubar, tearoff=0)
    EditMenu = Menu(menubar, tearoff=0)
    HelpMenu = Menu(menubar, tearoff=0)

    Scrollbar = Scrollbar(TextArea)
    file = None

    def __init__(self):
        # text area resizable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.TextArea.grid(sticky=N+S+E+W)
        # file menu
        self.FileMenu.add_command(label="New", command=self.newFile)
        self.FileMenu.add_command(label="Save", command=self.saveFile)
        self.FileMenu.add_command(label="Open", command=self.openFile)
        self.FileMenu.add_separator()
        self.FileMenu.add_command(label="Exit", activebackground="red", command=self.quitApplication)

        self.menubar.add_cascade(label="File", menu=self.FileMenu)
        # edit menu
        self.EditMenu.add_command(label="Select All   (Ctrl + A)", command=self.selectAll)
        self.EditMenu.add_command(label="Cut             (Ctrl + X)", command=self.cut)
        self.EditMenu.add_command(label="Copy          (Ctrl + C)", command=self.copy)
        self.EditMenu.add_command(label="Paste         (Ctrl + V)", command=self.paste)
        self.menubar.add_cascade(label="Edit", menu=self.EditMenu)
        # help menu
        self.HelpMenu.add_command(label="About Notepad", command=self.showAbout)
        self.menubar.add_cascade(label="Help", menu=self.HelpMenu)

        self.root.config(menu=self.menubar)
        self.Scrollbar.pack(side=RIGHT, fill=Y)

        self.Scrollbar.config(command=self.TextArea.yview)
        self.TextArea.config(yscrollcommand=self.Scrollbar.set)

    def quitApplication(self):
        self.root.destroy()

    def showAbout(self):
        showinfo("Notepad", "This is a simple Notepad application using Python3 and Tkinter library by Jason Alway.")

    def openFile(self):
        self.file = askopenfilename(defaultextension=".txt",
                                    filetypes=[("All files", "*.*"),
                                                ("Text document", "*.txt")])
        if self.file == "":
            self.file = None
        else:
            self.root.title(os.path.basename(self.file)+ " - Notepad")
            self.TextArea.delete(1.0, END)
            file = open(self.file,"r")
            self.TextArea.insert(1.0, file.read())
            file.close()

    def newFile(self):
        self.root.title("Untitled - Notepad")
        self.file = None
        self.TextArea.delete(1.0, END)

    def saveFile(self):
        if self.file == None:
            self.file = asksaveasfilename(initialfile="Untitled.txt",
                                        defaultextension=".txt",
                                        filetypes=[("All files", "*.*"),
                                                    ("text document", "*.txt")])
            if self.file == "":
                self.file = None
            else:
                file = open(self.file, "w")
                file.write(self.TextArea.get(1.0, END))
                file.close()

                self.root.title(os.path.basename(self.file)+ " - Notepad")
        else:
            file = open(self.file, "w")
            file.write(self.TextArea.get(1.0, END))
            file.close()

    def cut(self):
        self.TextArea.event_generate("<<Cut>>")

    def selectAll(self):
        self.TextArea.event_generate("<<SelectAll>>")

    def copy(self):
        self.TextArea.event_generate("<<Copy>>")

    def paste(self):
        self.TextArea.event_generate("<<Paste>>")

    def run(self):
        self.root.mainloop()

notepad = Notepad()
notepad.run()
