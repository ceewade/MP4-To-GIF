from tkinter import *
from tkinter import filedialog
from moviepy.editor import *
import os



class Window(Frame):

    def __init__(self, master=None): 
        Frame.__init__(self, master)                   
        self.master = master
        self.init_window()

    def init_window(self):
        #Configure Window and Menu
        self.master.title("MP4 To GUI")
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Open File", command=self.client_open_file)
        menu.add_cascade(label="File", menu=file)
        edit = Menu(menu)


    
    def client_open_file(self):
        #Browse for MP4
        filename = filedialog.askopenfilename(
                                          title = "Select a File",
                                          filetypes = (("MP4 files",
                                                        "*.MP4*"),
                                                       ("all files",
                                                        "*.*")))
        
        #Update GUI file path and button
        self.convert_button = Button(master=root, text="Convert MP4", command=self.convert_File)
        self.convert_button.pack()

        self.label_file_explorer = Label(master=root,
                            text = "File Opened: " + filename,
                            width = 100, height = 4,)
        self.label_file_explorer.pack()

        return filename
    


    def convert_File(self):
        print("Hello World")



        
        



root = Tk()
root.geometry("400x400")
app = Window(root)
root.mainloop() 