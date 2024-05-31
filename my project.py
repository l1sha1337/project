from tkinter import *
from tkinter import messagebox
from PIL import Image
def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        tk.destroy()
        
tk = Tk()        
tk.geometry("250x100")
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Приложение")
clicks = 0

def click_button():
    global clicks
    clicks += 1
    buttonText.set("Clicks {}".format(clicks))

buttonText = StringVar()
buttonText.set("Clicks {}".format(clicks))
btn = Button(textvariable = buttonText,background="#555",foreground="#ccc",
             padx="20",pady="8",font="16",command=click_button)
btn.pack()
tk.mainloop()

if clicks >= 20:
    image = Image.open("image.png")
    image.show()

if clicks >= 50:
    image = Image.open("image2.png")
    image.show()


if clicks >= 100:
    image = Image.open("image3.png")
    image.show()

