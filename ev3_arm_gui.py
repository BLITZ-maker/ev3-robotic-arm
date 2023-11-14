import tkinter as tk
from tkinter import PhotoImage

window = tk.Tk()
window.title("G4 robot controller")
window.geometry("222x230")
window.resizable(width=False, height=False)

image_path = "Images\Arrow-Up-icon.png" 
image = PhotoImage(file=image_path)
resized_image = image.subsample(7, 7)
button = tk.Button(window, image=resized_image)
button.pack(side=tk.TOP, anchor=tk.N)

image1_path = "Images\Arrow-Down-icon.png"  
image1 = PhotoImage(file=image1_path)
resized_image1 = image1.subsample(7, 7)
button1 = tk.Button(window, image=resized_image1)
button1.pack(side=tk.BOTTOM, anchor=tk.N)

image2_path = "Images\Arrow-Left-icon.png"  
image2 = PhotoImage(file=image2_path)
resized_image2 = image2.subsample(4, 4)
button2 = tk.Button(window, image=resized_image2)
button2.pack(side=tk.LEFT, anchor=tk.CENTER)

image3_path = "Images\Arrow-Right-icon.png"  
image3 = PhotoImage(file=image3_path)
resized_image3 = image3.subsample(4, 4)
button3 = tk.Button(window, image=resized_image3)
button3.pack(side=tk.RIGHT, anchor=tk.CENTER)

image4_path = "Images\grab.png"  
image4 = PhotoImage(file=image4_path)
resized_image4 = image4.subsample(7, 8)
button4 = tk.Button(window, image=resized_image4)
button4.pack(anchor=tk.CENTER)

window.mainloop()

