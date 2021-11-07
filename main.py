#Import the required Libraries

import os
from tkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw
# import subprocess
# subprocess.check_call(['gs', '--version'])


orig_image = (Image.open("maya.png"))
width, height = orig_image.size
print(width, height)
watermark_image = orig_image.copy()


#Load an image in the script
def make_mark():
    global orig_image
    global watermark_image
    global new_image
    global canvas
    draw = ImageDraw.Draw(watermark_image)
    font = ImageFont.truetype("Arial.ttf", int(width/30))
    draw.text((int(width*0.990), int(width*0.990)), "Maya", (0, 0, 0), font=font, anchor="rd")
    draw.text((int(width*0.988), int(width*0.988)), "Maya", (255, 255, 255), font=font, anchor="rd")
    watermark_image.save("maya_wm.png")
    new_image = ImageTk.PhotoImage(watermark_image.resize((600,600), Image.ANTIALIAS))
    canvas.create_image(0, 0, anchor=NW, image=new_image)
    canvas.update()

    return watermark_image

#Create an instance of tkinter frame
window = Tk()
window.title("Watermark 水印")
#Set the geometry of tkinter frame
window.geometry("19204x1024")


label = Label(text="Watermark App", font=("Arial", 72, "bold"))
label.pack()

button = Button(text="Run", command=make_mark)
button.pack()

#Create a canvas
canvas = Canvas(window, width= 600, height= 600)
canvas.pack()

resized_orig_img = orig_image.resize((600,600), Image.ANTIALIAS)
resized_watermark_image = watermark_image.resize((600,600), Image.ANTIALIAS)

new_image = ImageTk.PhotoImage(resized_orig_img)

canvas.create_image(0,0, anchor=NW, image=new_image)

canvas.update()
# canvas.postscript(file="file_name.eps", colormode='color', height=600, width=600)
# save_img = Image.open("file_name.eps")
# save_img.save("mayawm.png", "png")




window.mainloop()