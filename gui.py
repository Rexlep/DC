import customtkinter as ctk
import tkinter as tk
import os
import cv2 as cv2
from PIL import ImageTk, Image, ImageDraw, ImageFont
from tkinter import PhotoImage, filedialog


def add_text(image):
    # Get text to add to image
    text_to_add = entry.get()

    # Edit the Image
    edit_image = ImageDraw.Draw(image)
    edit_image.text((150, 300), text_to_add, ("green"), font=text_font)

    # Save The Image
    my_image.save(image)

    # Clear the entry box
    entry.delete(0, END)
    entry.insert(0, "Saving File...")

    # Wait a couple seconds and then show image
    my_label.after(2000, show_pic)



def open_image():
    image_file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if image_file_path:
        selected_img = ImageTk.PhotoImage(Image.open(image_file_path))
        image_label = tk.Label(frame_image, image=selected_img)
        image_label.image = selected_img
        image_label.pack(expand=True, fill=tk.BOTH)
        add_text(image=selected_img)



#_____________________________________________________gui_____________________________________________________________________________

root = ctk.CTk()
root.title("DC")

# root.iconpath = ImageTk.PhotoImage(file=os.path.join("assets","dc.png"))
# rott.wm_iconbitmap()
# root.iconphoto(False,root.iconpath)


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

#_____________________________________________________right frame_____________________________________________________________________________

entry = ctk.CTkEntry(frame_box, width=200, height=40, corner_radius=15)
entry.pack(side=ctk.LEFT, padx=(10, 10))

change_text_btn = ctk.CTkButton(frame_box, fg_color='#5b0e75', hover_color='#270433', text='Chaneg Text',
                                font=('Poppins', 16), corner_radius=20, width=30, height=35, command=add_text)
change_text_btn.pack(side=ctk.RIGHT, padx=(0, 10))

combo_size = ctk.CTkComboBox(frame_right, button_color='#5b0e75')
combo_size.set("Select")
combo_size.pack(side=ctk.TOP, pady=(150, 0))

save_btn = ctk.CTkButton(frame_right, fg_color='#5b0e75', hover_color='#270433', text='Save', font=('Poppins', 16), corner_radius=20, width=30, height=35)
save_btn.pack(side=ctk.TOP, pady=10)

root.mainloop()


