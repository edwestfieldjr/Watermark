# (C)opyright 2021 Edward Francis Westfield Jr.
# https://edwestfieldjr.com/
# MIT License

# Note: This project was created for a class: 100 Days of Code:
# The Complete Python Pro Bootcamp for 2022
# (Day 84, Assignment 4: Image Watermarking Desktop App)
# https://www.udemy.com/course/100-days-of-code/learn/practice/1251146#questions

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFont, ImageDraw

PROJECT_APP_NAME = "The Watermark App"
PROJECT_HEADING = "A desktop app to add text to the lower right hand corner of an image file."
PROJECT_WINDOW_TITLE = "Watermark 水印"

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.orig_image = None
        self.create_interface()
        self.grid()

    def create_interface(self):
        title_config = {'bg': 'red', 'fg': 'white'}
        self.heading_label = Label(text=PROJECT_APP_NAME, font=("Arial", 36, "bold"), cnf=title_config)
        self.heading_label.grid(row=0, column=0, columnspan=4, sticky=EW)
        self.subheading_label = Label(text=PROJECT_HEADING, font=("Arial", 14), cnf=title_config)
        self.subheading_label.grid(row=1, column=0, columnspan=4, sticky=EW)
        self.get_file_browse_button = Button(text="Select file", bg="#dddddd", highlightbackground="#dddddd", fg="black", command=self.browsefunc)
        self.get_file_browse_button.grid(row=2, column=0)
        self.entry_watermark_text_label = Label(text="Add Text Here:", font=("Arial", 14))
        self.entry_watermark_text_label.grid(row=2, column=1)
        self.entry_watermark_text = Entry()
        self.entry_watermark_text.grid(row=2, column=2)
        self.make_button = Button(text="Add/Update", bg="#dddddd", highlightbackground="#dddddd", fg="black", command=lambda: self.make_mark(self.entry_watermark_text.get()))
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
        self.quit = Button(text="Save", bg="#dddddd", highlightbackground="#dddddd", fg="black", command=lambda:self.watermark_image.save(self.filename))
        self.quit.grid(row=5, column=0)
        self.quit = Button(text="Save As...", bg="#dddddd", highlightbackground="#dddddd", fg="black", command=self.save_as_image)
        self.quit.grid(row=5, column=1)
        self.quit = Button(text="Clear", bg="#dddddd", highlightbackground="#dddddd", fg="black", command=self.clear_text)
        self.quit.grid(row=5, column=2)
        self.quit = Button(text="QUIT", bg="#dddddd", highlightbackground="#dddddd", fg="red", command=self.master.destroy)
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
        self.image_on_canvas.update
        self.canvas.update()

    def make_mark(self, watermark_text):
        self.watermark_image = self.orig_image.copy()
        draw = ImageDraw.Draw(self.watermark_image)
        font = ImageFont.truetype("Arial.ttf", int(self.main_width / 20))
        draw.text((int(self.main_width * 0.990), int(self.main_height * 0.990)), watermark_text, (0, 0, 0), font=font, anchor="rd")
        draw.text((int(self.main_width * 0.988), int(self.main_height * 0.988)), watermark_text, (255, 255, 255), font=font, anchor="rd")
        new_image = ImageTk.PhotoImage(self.watermark_image.resize((self.img_resize_width, self.img_resize_height), Image.ANTIALIAS))
        self.canvas.itemconfig(self.image_on_canvas, image=new_image)
        self.image_on_canvas.update()

    def clear_text(self):
        self.entry_watermark_text.delete(0, END)
        self.make_mark(self.entry_watermark_text.get())


    def save_as_image(self):
        try:
            self.watermark_image.save(filedialog.asksaveasfilename(filetypes=[
                (f"{self.orig_image.format} files", (f"*.{self.orig_image.format.lower()}")),
                ("All files", "*.*")
            ]))
        except:
            pass


root = Tk()
root.title(PROJECT_WINDOW_TITLE)
app = Application(master=root)
app.mainloop()