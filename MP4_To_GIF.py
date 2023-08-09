import tkinter as tk
import customtkinter 
from tkinter import filedialog, ttk, Menu, messagebox
from tkVideoPlayer import TkinterVideo
from moviepy.editor import *
import threading




class App(customtkinter.CTk):
    def __init__(self, master=None):
        super().__init__()
        customtkinter.set_appearance_mode('dark')
        self.title('MP4 To GIF')
        self.geometry('1000x800')
        self.minsize(800, 500)
        self.OpenFile()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


    def OpenFile(self):
        
        self.filebutton = customtkinter.CTkButton(self, text='Open File', command=self.Main)
        self.filebutton.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        return self.filebutton

    def Main(self):
        self.padding = 5
        self.filebutton.place_forget()

        self.filename = filedialog.askopenfilename(
                                          title = "Select a File",
                                          filetypes = (("MP4 files",
                                                        "*.MP4*"),
                                                       ("all files",
                                                        "*.*")))

        self.sideBarFrame = customtkinter.CTkFrame(self, corner_radius=0)
        self.sideBarFrame.grid(row=0, column=0, sticky='nsew')
        self.sideBarFrame.grid_rowconfigure(4, weight=1)

        self.videoFrame = customtkinter.CTkFrame(self, corner_radius=20, fg_color=self._fg_color)
        self.videoFrame.grid(row=0, column=1, padx=5, pady=5, rowspan=5, sticky='nsew')

        self.videoplayer = TkinterVideo(self.videoFrame, scaled=True)
        self.videoplayer.load(self.filename)
        self.videoplayer.pack(padx=20, pady=20, expand=True, fill="both")
        self.videoplayer.play()

        self.appLabel = customtkinter.CTkLabel(self.sideBarFrame, text='MP4 TO GIF', font=('Arial', 20))
        self.appLabel.grid(row=0, column=0, padx=20, pady=30)

        #self.fileLabel = customtkinter.CTkLabel(self.sideBarFrame, text='File Opened: ' + self.filename)
        #self.fileLabel.grid(row=1, column=0)

        
        #Fps label configuration
        self.fpsLabel = customtkinter.CTkLabel(self.sideBarFrame, text='Enter FPS: ')
        self.fpsLabel.grid(row=1, column=0, pady=5)
        self.fpsInt = customtkinter.CTkEntry(self.sideBarFrame, placeholder_text='Enter FPS')
        self.fpsInt.grid(row=1, column=1, pady=5, padx=10)

        #GIF Start Second Entry
        self.startSecond = customtkinter.CTkLabel(self.sideBarFrame, text='Enter Starting Second')
        self.startSecond.grid(row=2, column=0, pady=5)
        self.startSecondEntry = customtkinter.CTkEntry(self.sideBarFrame, placeholder_text='Enter Starting Second')
        self.startSecondEntry.grid(row=2, column=1, pady=5, padx=10)

        #GIF Ending Second Entry
        self.endingSecond = customtkinter.CTkLabel(self.sideBarFrame, text='Enter Ending Second')
        self.endingSecond.grid(row=3, column=0, pady=5)
        self.endingSecondEntry = customtkinter.CTkEntry(self.sideBarFrame, placeholder_text='Enter Ending Second')
        self.endingSecondEntry.grid(row=3, column=1, pady=5, padx=10)

        self.gifNameLabel = customtkinter.CTkLabel(self.sideBarFrame, text='Enter New File Name')
        self.gifNameLabel.place(relx=.25, rely=.85, anchor='s')
        self.gifNameEntry = customtkinter.CTkEntry(self.sideBarFrame, placeholder_text='Enter New File Name')
        self.gifNameEntry.place(relx=.7, rely=.85, anchor='s')
        self.convertGifButton = customtkinter.CTkButton(self.sideBarFrame, text='Convert To GIF', command=self.MultiThread)
        self.convertGifButton.place(relx=.5, rely=.9, anchor='s')


        return self.filename, self.fpsInt, self.startSecondEntry, self.endingSecondEntry

    def MultiThread(self):
        threading.Thread(target=self.ConvertFile).start()

    def ConvertFile(self):
        #Getting input values
        #self.gifName = 'new_gif'
        self.progressBar = customtkinter.CTkProgressBar(self.sideBarFrame)
        self.progressBar.place(relx=.5, rely=.95, anchor='s')
        self.progressBar.configure(determinate_speed=1, mode='indeterminate')
        self.progressBar.start()

        self.getFPS = int(self.fpsInt.get())
        self.getStart = int(self.startSecondEntry.get())
        self.getEnd = int(self.endingSecondEntry.get())
        self.getNewFileName = str(self.gifNameEntry.get())
        if self.getNewFileName == str(''):
            self.gifName = 'new_gif'
        else:
            self.gifName = str(self.gifNameEntry.get())

        #converting mp4 to gif
        clip = VideoFileClip(self.filename)
        clip = clip.subclip(self.getStart, self.getEnd)
        clipResize = clip.resize(height=300)
        clipResize.write_gif(f'{self.gifName}.gif', fps=self.getFPS, program= 'ffmpeg',  opt='OptimizeTransparency', logger=None)
        self.gif = VideoFileClip(f"{self.gifName}.gif")
        messagebox.showinfo(title="Complete", message="File Finished Converting")

        #Resetting the window
        self.sideBarFrame.grid_forget()
        self.appLabel.grid_forget()
        self.fpsLabel.grid_forget()
        self.fpsInt.grid_forget()
        self.startSecond.grid_forget()
        self.startSecondEntry.grid_forget()
        self.endingSecond.grid_forget()
        self.endingSecondEntry.grid_forget()
        self.gifNameLabel.place_forget()
        self.gifNameEntry.place_forget()
        self.convertGifButton.place_forget()
        self.videoplayer.pack_forget()
        self.progressBar.place_forget()
        self.OpenFile()

if __name__ == '__main__':
    app = App()
    app.mainloop()
