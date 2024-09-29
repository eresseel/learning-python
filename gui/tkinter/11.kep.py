from tkinter import *      
root = Tk()      
canvas = Canvas(root, width = 300, height = 300)      
canvas.pack()      
img = PhotoImage(file="Martin_p.gif")      
canvas.create_image(20,20, anchor=NW, image=img)      
mainloop() 