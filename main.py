import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFont, ImageDraw

PROJECT_TITLE = "Watermark App"
PROJECT_HEADING = "A desktop app to add text to the lower right hand corner of an image file."

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.orig_image = None
        self.create_interface()
        self.grid()

    def create_interface(self):

        title_config = {'bg': 'red', 'fg': 'white'}

        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)
        self.heading_label = Label(text=PROJECT_TITLE, font=("Arial", 36, "bold"), cnf=title_config)
        self.heading_label.grid(row=0, column=0, columnspan=4)
        self.subheading_label = Label(text=PROJECT_HEADING, font=("Arial", 14), cnf=title_config)
        self.subheading_label.grid(row=1, column=0, columnspan=4)

        self.get_file_browse_button = Button(text="Select file", command=self.browsefunc)
        self.get_file_browse_button.grid(row=2, column=0)

        self.entry_watermark_text_label = Label(text="Add Text Here:", font=("Arial", 14))
        self.entry_watermark_text_label.grid(row=2, column=1)

        self.entry_watermark_text = Entry()
        self.entry_watermark_text.grid(row=2, column=2)

        self.make_button = Button(text="Add/Update", command=lambda: self.make_mark(self.entry_watermark_text.get()))
        self.make_button.grid(row=2, column=3)

        self.canvas_width = 480
        self.canvas_height = 480

        self.canvas = Canvas(master=None,
                             width=self.canvas_width,
                             height=self.canvas_height,
                             bg="black",
                             )
        self.image_on_canvas = self.canvas.create_image(0, 0, image=None, anchor=NW, state=NORMAL)
        self.canvas.grid(row=4, column=0, columnspan=4)

        self.quit = Button(text="Save", fg="black", command=lambda: self.watermark_image.save(self.filename))
        self.quit.grid(row=5, column=0)

        self.quit = Button(text="save As...", fg="black", command=self.save_as_image)
        self.quit.grid(row=5, column=1)

        self.quit = Button(text="Clear", fg="black", command=self.clear_text)
        self.quit.grid(row=5, column=2)

        self.quit = Button(text="QUIT", fg="red", command=self.master.destroy)
        self.quit.grid(row=5, column=3)

    def browsefunc(self):
        self.filename = filedialog.askopenfilename(
            filetypes=[
                ("TIFF files", ("*.tiff", "*.tif")),
                ("JPEG files", ("*.jpeg", "*.jpg", "*.jfif")),
                ("PNG files", "*.png"),
                ("BMP files", "*.bmp"),
                ("GIF files", "*.gif"),
                ("All files", "*.*")
            ])
        # self.get_file_entry.configure(state='normal')
        # self.get_file_entry.delete(0, END)
        # self.get_file_entry.insert(END, self.filename)
        # self.get_file_entry.configure(state='disabled')
        self.set_image()

    def set_image(self):
        print("start set_image func")
        self.orig_image = Image.open(self.filename)
        self.main_width, self.main_height = self.orig_image.size
        print(self.main_width, self.main_height)
        if self.main_width >= self.main_height:
            self.img_resize_width = self.canvas_width
            self.img_resize_height = int(self.canvas_height * (self.main_height / self.main_width))
        else:
            self.img_resize_width = int(self.canvas_width * (self.main_width / self.main_height))
            self.img_resize_height = self.canvas_height
        print(self.img_resize_width, self.img_resize_height)
        new_image = ImageTk.PhotoImage(
            self.orig_image.resize((self.img_resize_width, self.img_resize_height), Image.ANTIALIAS))
        self.canvas.itemconfig(self.image_on_canvas, image=new_image)
        self.image_on_canvas.update()
        self.image_on_canvas.update
        self.canvas.update()

    def make_mark(self, watermark_text):
        self.watermark_image = self.orig_image.copy()
        draw = ImageDraw.Draw(self.watermark_image)
        font = ImageFont.truetype("Arial.ttf", int(self.main_width / 30))
        draw.text((int(self.main_width * 0.990), int(self.main_height * 0.990)), watermark_text, (0, 0, 0), font=font,
                  anchor="rd")
        draw.text((int(self.main_width * 0.988), int(self.main_height * 0.988)), watermark_text, (255, 255, 255),
                  font=font, anchor="rd")
        new_image = ImageTk.PhotoImage(
            self.watermark_image.resize((self.img_resize_width, self.img_resize_height), Image.ANTIALIAS))
        self.canvas.itemconfig(self.image_on_canvas, image=new_image)
        self.image_on_canvas.update()

    def clear_text(self):
        self.entry_watermark_text.delete(0, END)
        self.make_mark(self.entry_watermark_text.get())

    def save_as_image(self):
        self.watermark_image.save(filedialog.asksaveasfilename(filetypes=[
            (f"{self.orig_image.format} files", (f"*.{self.orig_image.format.lower()}")),
            ("All files", "*.*")
        ]
        )
        )

    def say_hi(self):
        print("hi there, everyone!")


root = Tk()
root.title("Watermark")
app = Application(master=root)
app.mainloop()

# orig_image = (Image.open("maya.png"))
# width, self.main_height = orig_image.size
# print(width, self.main_height)
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
# # canvas.postscript(file="file_name.eps", colormode='color', self.main_height=600, width=600)
# # save_img = Image.open("file_name.eps")
# # save_img.save("mayawm.png", "png")
#
#
# app = Application(master=window)
# app.mainloop()
