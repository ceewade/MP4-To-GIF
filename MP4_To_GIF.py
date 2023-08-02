import tkinter as tk
from tkinter import filedialog, ttk
from moviepy.editor import *


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MP4 To GIF")
        self.geometry('500x500')
        self.resizable(False, False)

        self.main()

    def main(self):
        self.filename = filedialog.askopenfilename(
                                          title = "Select a File",
                                          filetypes = (("MP4 files",
                                                        "*.MP4*"),
                                                       ("all files",
                                                        "*.*")))
        
        self.button = ttk.Button(self, text='Convert To GIF', command=self.convertToGIF)
        self.button.place(relx=.5, rely=.5, anchor='center')

        self.label = ttk.Label(self, text="File Opened: " + self.filename)
        self.label.pack()

        return self.filename

    def convertToGIF(self):
        print(self.filename)
        clip = VideoFileClip(self.filename)
        clip.write_gif("gif.gif")

        self.main()

    

if __name__ == '__main__':
    app = App()
    app.mainloop()
