import customtkinter as ctk
import tkinter as tk
import os
import cv2 as cv2
from messagebox.CTkMessagebox import CTkMessagebox
from PIL import ImageTk, Image, ImageDraw, ImageFont
from tkinter import PhotoImage, filedialog

photo = None
cv_img = None


def add_text():
    global cv2
    text = entry.get()
    if text != '':
        position = (50, 50)  # Position where the text will be placed
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        color = (99, 99, 99)  # White color
        thickness = 2
        # Add text to the image using OpenCV
        cv2.putText(cv_img, text, position, font, font_scale, color, thickness)
        
        # Update the image label with the new image
        cv_img_rgb = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(cv_img_rgb)
        photo = ImageTk.PhotoImage(pil_img)
        label.configure(image=photo)
        label.image = photo

    else:
        CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel")


def open_image():
    global cv_img, photo
    image_file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])

    if image_file_path:
        # Open the image using OpenCV
        cv_img = cv2.imread(image_file_path)

        # Convert the image from BGR to RGB color space
        cv_img_rgb = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        
        # Convert the OpenCV image to a PIL image
        pil_img = Image.fromarray(cv_img_rgb)
        
        # Convert the PIL image to an ImageTk photo image
        photo = ImageTk.PhotoImage(pil_img)
        
        # Display the image in the Tkinter label
        label.configure(image=photo, text="")
        label.image = photo

#_____________________________________________________gui_____________________________________________________________________________

root = ctk.CTk()
root.title("DC")

window_width = 1080
window_height = 630

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

root.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

frame_right = ctk.CTkFrame(root, corner_radius=20, width=400)
frame_right.pack_propagate(False)
frame_right.pack(side=ctk.RIGHT, fill=ctk.BOTH, padx=20, pady=20)

frame_left = ctk.CTkFrame(root, corner_radius=20, width=640)
frame_left.pack_propagate(False)
frame_left.pack(side=ctk.LEFT, fill=ctk.BOTH, padx=20, pady=20)

frame_image = ctk.CTkFrame(frame_left, corner_radius=20, width=400, height=500)
frame_image.pack_propagate(False)
frame_image.pack(side=ctk.TOP, padx=20, pady=20)

frame_box = ctk.CTkFrame(frame_right, corner_radius=20, width=440, height=50)
frame_box.pack_propagate(False)
frame_box.pack(side=ctk.TOP, padx=20, pady=20)

#_____________________________________________________left frame_____________________________________________________________________________

select_btn = ctk.CTkButton(frame_left, fg_color='#5b0e75', hover_color='#270433', text='Select Image',
                           font=('Poppins', 16), corner_radius=20, height=35, command=open_image)
select_btn.pack()

label = ctk.CTkLabel(frame_image)
label.pack(expand=True)

#_____________________________________________________right frame_____________________________________________________________________________

entry = ctk.CTkEntry(frame_box, width=200, height=40, corner_radius=15)
entry.pack(side=ctk.LEFT, padx=(10, 10))

add_text_btn = ctk.CTkButton(frame_box, fg_color='#5b0e75', hover_color='#270433', text='Add Text',
                                font=('Poppins', 16), corner_radius=20, width=30, height=35, command=add_text)
add_text_btn.pack(side=ctk.RIGHT, padx=(0, 10))

combo_size = ctk.CTkComboBox(frame_right, button_color='#5b0e75')
combo_size.set("Select")
combo_size.pack(side=ctk.TOP, pady=(150, 0))

save_btn = ctk.CTkButton(frame_right, fg_color='#5b0e75', hover_color='#270433', text='Save', font=('Poppins', 16), corner_radius=20, width=30, height=35)
save_btn.pack(side=ctk.TOP, pady=10)

root.mainloop()