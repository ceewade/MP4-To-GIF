from tkinter import *
from tkinter import filedialog
from moviepy.editor import *
import os



root = Tk()
root.geometry("400x400")

def convertGIF():
    print(filename)
    clip = VideoFileClip(filename)
    clip.write_gif("new_gif.gif")


filename = filedialog.askopenfilename(
                                          title = "Select a File",
                                          filetypes = (("MP4 files",
                                                        "*.MP4*"),
                                                       ("all files",
                                                        "*.*")))

convert_button = Button(master=root, text="Convert MP4", command=convertGIF)
convert_button.pack()

label_file_explorer = Label(master=root,
                            text = "File Opened: " + filename,
                            width = 100, height = 4,)
label_file_explorer.pack() 



root.mainloop()