import tkinter as tk
from tkinter import filedialog, ttk, Menu, messagebox
from moviepy.editor import *
import threading


class App(tk.Tk):
    def __init__(self, master=None):
        super().__init__()
        #Configure App
        self.title("MP4 To GIF")
        self.geometry('500x500')
        self.resizable(False, False)
        self.hasfile = False

        #Configure menu layout
        self.master = master
        menu = Menu(self.master)
        self.config(menu=menu)


        fileMenu = Menu(menu)
        fileMenu.add_command(label="Open File", command=self.main)
        fileMenu.add_command(label="Exit")
        menu.add_cascade(label="File", menu=fileMenu)

        
    def main(self):

        if self.hasfile == False:
            self.filename = filedialog.askopenfilename(
                                          title = "Select a File",
                                          filetypes = (("MP4 files",
                                                        "*.MP4*"),
                                                       ("all files",
                                                        "*.*")))
        
            self.hasfile = True
            self.button = ttk.Button(self, text='Convert To GIF', command=self.buttonPress)
            self.button.place(relx=.5, rely=.5, anchor='center')

            self.label = ttk.Label(self, text="File Opened: " + self.filename)
            self.label.pack()


            return self.filename
        else:
            messagebox.showerror(title="Error", message="A file is already loaded")

    
    def buttonPress(self):
        threading.Thread(target=self.convertToGIF).start()

    def convertToGIF(self):
        print(self.filename)
        clip = VideoFileClip(self.filename)
        clip.write_gif("gif.gif")
        self.gif = VideoFileClip("gif.gif")
        self.label.configure(text="Coverting Complete.")

        self.exportGIF()

        
    def exportGIF(self):
        self.exportFile = filedialog.asksaveasfilename(initialfile=self.filename, 
                                                       defaultextension=".gif",
                                                       filetypes=[("All Files","*.*"),("GIF Files","*.gif")])
        App()
        
        

    

if __name__ == '__main__':

    app = App()
    app.mainloop()
