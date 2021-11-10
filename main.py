import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFont, ImageDraw



class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_interface()
        self.grid()

    def create_interface(self):

        title_config = {'bg': 'red', 'fg': 'white'}

        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)
        self.heading_label = Label(text="Watermark App", font=("Arial", 36, "bold"), cnf=title_config)
        self.heading_label.grid(row=0, column=0, columnspan=3)
        self.subheading_label = Label(text="A way to add text to the lower right hand corner of an image.", font=("Arial", 14))
        self.subheading_label.grid(row=1, column=0, columnspan=3)

        self.get_file_label = Label(text="Select File", font=("Arial", 14))
        self.get_file_label.grid(row=2, column=0)
        self.get_file_entry = Entry(font=40)
        self.get_file_entry.grid(row=2, column=1)
        self.get_file_browse_button = Button(text="Browse", font=40, command=self.browsefunc)
        self.get_file_browse_button.grid(row=2, column=2)


        self.entry_watermark_text_label = Label(text="Add Watermark Text:", font=("Arial", 14))
        self.entry_watermark_text_label.grid(row=3, column=0)

        self.entry_watermark_text = Entry()
        self.entry_watermark_text.grid(row=3, column=1)
        # self.entry_watermark_text.insert(0, "Enter any Text")


        self.make_button = Button(text="Add Ttxt", command=lambda:self.make_mark(self.entry_watermark_text.get()))
        self.make_button.grid(row=3, column=2)

        self.canvas = Canvas(master=None,
                             width=480,
                             height=480,
                             bg="black",
                             )
        # self.canvas.create_image(0, 0, anchor=NW)
        self.canvas.grid(row=4, column=0, columnspan=3)


        self.quit = Button(text="QUIT", fg="red", command=self.master.destroy)
        self.quit.grid(row=5, column=0, columnspan=3)

    def browsefunc(self):
        self.filename = filedialog.askopenfilename(filetypes=(("tiff files", ("*.tiff", "*.tiff")), ("png files", "*.png"), ("All files", "*.*")))
        self.get_file_entry.insert(END, self.filename)  # add this



    def get_image(self):
        pass


    def make_mark(self, watermark_text):
        self.orig_image = (Image.open(self.get_file_entry.get()))
        width, height = self.orig_image.size
        print(width, height)
        watermark_image = self.orig_image.copy()
        draw = ImageDraw.Draw(watermark_image)
        font = ImageFont.truetype("Arial.ttf", int(width / 30))
        draw.text((int(width * 0.990), int(width * 0.990)), watermark_text, (0, 0, 0), font=font, anchor="rd")
        draw.text((int(width * 0.988), int(width * 0.988)), watermark_text, (255, 255, 255), font=font, anchor="rd")
        watermark_image.save("maya_wm.png")
        new_image = ImageTk.PhotoImage(watermark_image.resize((600, 600), Image.ANTIALIAS))
        # canvas.create_image(0, 0, anchor=NW, image=new_image)
        # canvas.update()

    def say_hi(self):
        print("hi there, everyone!")

root = Tk()
root.title("Watermark")
app = Application(master=root)
app.mainloop()

# orig_image = (Image.open("maya.png"))
# width, height = orig_image.size
# print(width, height)
# watermark_image = orig_image.copy()
#
#
# #Load an image in the script
# def make_mark(func_arg):
#     global orig_image
#     global watermark_image
#     global new_image
#     global canvas
#     print(func_arg)
#     draw = ImageDraw.Draw(watermark_image)
#     font = ImageFont.truetype("Arial.ttf", int(width/30))
#     draw.text((int(width*0.990), int(width*0.990)), "Maya", (0, 0, 0), font=font, anchor="rd")
#     draw.text((int(width*0.988), int(width*0.988)), "Maya", (255, 255, 255), font=font, anchor="rd")
#     watermark_image.save("maya_wm.png")
#     new_image = ImageTk.PhotoImage(watermark_image.resize((600,600), Image.ANTIALIAS))
#     canvas.create_image(0, 0, anchor=NW, image=new_image)
#     canvas.update()
#
#     return watermark_image
#
# #Create an instance of tkinter frame
# window = Tk()
# window.title("Watermark 水印")
# #Set the geometry of tkinter frame
# window.geometry("19204x1024")
#
#
# label = Label(text="Watermark App", font=("Arial", 72, "bold"))
# label.pack()
#
# label = Label(text="Watermark App", font=("Arial", 72, "bold"))
# label.pack()
#
#
#
#
# button = Button(text="Run", command=make_mark("yo"))
# button.pack()
#
# #Create a canvas
#
# resized_orig_img = orig_image.resize((600,600), Image.ANTIALIAS)
# resized_watermark_image = watermark_image.resize((600,600), Image.ANTIALIAS)
#
# new_image = ImageTk.PhotoImage(resized_orig_img)
#
# canvas.create_image(0,0, anchor=NW, image=new_image)
#
# canvas.update()
# # canvas.postscript(file="file_name.eps", colormode='color', height=600, width=600)
# # save_img = Image.open("file_name.eps")
# # save_img.save("mayawm.png", "png")
#
#
# app = Application(master=window)
# app.mainloop()