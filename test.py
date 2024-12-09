from tkinter import *
from PIL import Image, ImageFont, ImageDraw
from tkinter import filedialog


root = Tk()
root.title('Codemy.com - Add Text To Images')
root.geometry("600x650")

file_image = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])


# Add Text To Image
def add_it():

	# Open our image
    my_image = Image.open(file_image)
	# Define The Font
    text_font = ImageFont.truetype("arial.ttf", 46)
    # Get text to add to image
    text_to_add = my_entry.get()

    # Edit the Image
    edit_image = ImageDraw.Draw(my_image)
    edit_image.text((150, 300), text_to_add, ("green"), font=text_font)

    # Save The Image
    my_image.save(file_image)

    # Clear the entry box
    my_entry.delete(0, END)
    my_entry.insert(0, "Saving File...")

    # Wait a couple seconds and then show image
    my_label.after(2000, show_pic)

def show_pic():
	# Show New Image
	global aspen2
	aspen2 = PhotoImage(file=file_image)
	my_label.config(image=aspen2)

	# Clear the entry box 
	my_entry.delete(0, END)



# Define Image
aspen = PhotoImage(file=file_image)

# Create A Label
my_label = Label(root, image=aspen)
my_label.pack(pady=20)

#Entry Box
my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=20)

# Button
my_button = Button(root, text="Add Text To Image",
	command=add_it, font=("Helvetica", 24))
my_button.pack(pady=20)

root.mainloop()