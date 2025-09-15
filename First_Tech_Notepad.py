# Creating Desktop Notepad with some more features

## Import Data
from tkinter import *
from tkinter import ttk
import webbrowser
from tkinter.messagebox import showerror, showinfo, showwarning
from tkinter.colorchooser import askcolor
from tkinter import filedialog

# Display project Data
window = Tk()
window.title("***First_Tech***")
window.geometry("1366x700")
window.config(bg="white")

# max or min window
window.maxsize(1360,700)
window.minsize(1000,500)


# Functon for Open_file
def open_file():
    var = filedialog.askopenfile(initialdir="/", filetypes=[
        ("Text files", "*.txt"),
        ("All files", "*.*")
    ], title="First_Tech")

    if var:
        content = var.read()
        text.delete(1.0, END)     # Clear existing content
        text.insert(INSERT, content)  # Insert file content into Text widget
        var.close()


# function for asksaveas file

def ask_save_as_file():

    var = filedialog.asksaveasfile(title="Save as",mode="w"
                                   ,defaultextension=".txt",
                                    initialdir="/",
                                   filetypes=[("Txt File","*.txt"),("Python","*.py"),
                                              ("All files","*.*")]
                                              )
    if var:
        content = text.get(1.0, END)  #  Get content from the text area
        var.write(content)            #  Write to file
        var.close()

# funtion for save 
def ask_save_as_file_name():

    var = filedialog.asksaveasfilename(title="Save as",mode="w"
                                   ,defaultextension=".txt",
                                    initialdir="/",
                                   filetypes=[("Txt File","*.txt"),("Python","*.py"),
                                              ("All files","*.*")]
                                              )
    if var:
        content = text.get(1.0, END)  #  Get content from the text area
        var.write(content)           
        var.close()


# function for close
def close_window():
    window.destroy()
    
# ✅ Create the main menu bar
main_menu = Menu(window)
window.config(menu=main_menu,bg="Blue")  # Set once


# === File Menu ===
file_menu = Menu(main_menu, tearoff=0)



 

# sub menu for (new) via file_menu

new_sub_menu = Menu(file_menu,tearoff=0)
new_sub_menu.add_command(label="New page")
new_sub_menu.add_command(label="New window")

file_menu.add_cascade(label="New",menu=new_sub_menu)


file_menu.add_command(label="Save",command=ask_save_as_file_name)
file_menu.add_command(label="Save as",command=ask_save_as_file)
file_menu.add_command(label="Save wth Password")
file_menu.add_command(label="Open",command = open_file) # command for open file
file_menu.add_command(label="Exit",command=window.quit)
main_menu.add_cascade(label="File", menu=file_menu)

# === Edit Menu ===
edit_menu = Menu(main_menu, tearoff=0)

edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Paste")
edit_menu.add_separator()  # Visual separator
edit_menu.add_command(label="Find Text")
main_menu.add_cascade(label="Edit", menu=edit_menu)

# Font size menu

font_size_menu = Menu(edit_menu,tearoff = 0)
font_size_menu.add_command(label="10")
font_size_menu.add_command(label="14")
font_size_menu.add_command(label="18")
font_size_menu.add_command(label="22")
font_size_menu.add_command(label="26")
font_size_menu.add_command(label="30")
font_size_menu.add_command(label="34")
edit_menu.add_cascade(label="Font size",menu=font_size_menu)

# View Menu
view_menu = Menu(main_menu,tearoff = 0)
view_menu.add_command(label="Zoom in       Ctrl + plus")
view_menu.add_command(label="Zoom out      Ctrl + minus")
main_menu.add_cascade(label="View", menu= view_menu)


# About Menu

def show_info():
    showinfo(title=("About us"), message=("📝 First_Tech Notepad\nVersion:" \
    " 5.7.25\nDeveloper: Nitesh"))

help_menu = Menu(main_menu, tearoff = 0)
help_menu.add_command(label="About", command=show_info)
main_menu.add_cascade(label="Help",menu=help_menu)


# set links

def open_link_youtube():
    webbrowser.open("https://www.youtube.com/")

def open_link_whatsapp():
    webbrowser.open("https://web.whatsapp.com/") # for web desktop

def open_link_linkedin():
    webbrowser.open("https://www.linkedin.com/feed/")

def open_link_snapchat():
    webbrowser.open("links_menu.add_separator()")


# Links menu

links_menu = Menu(main_menu, tearoff = 0)
links_menu.add_command(label="Whatsapp",command=open_link_whatsapp)
links_menu.add_command(label="Snapchat",command=open_link_snapchat)
links_menu.add_separator()
links_menu.add_command(label="YouTube",command=open_link_youtube)
links_menu.add_separator()
links_menu.add_command(label="Linkedin",command=open_link_linkedin)
main_menu.add_cascade(label="Links", menu=links_menu)



# Text Box are
text_frame = Frame(window)
text_frame.place(x=0, y=1, width=1366, height=670)


scroll_y = Scrollbar(text_frame, orient = VERTICAL)
scroll_y.pack(side = RIGHT, fill=Y)

scroll_x  = Scrollbar(text_frame,orient=HORIZONTAL)
scroll_x.pack(side = BOTTOM,fill=X)



text = Text(text_frame, font=("Times New Roman", 15),wrap=NONE,undo=TRUE,
            yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
text.pack(fill=BOTH, expand=True)

scroll_x.config(command=text.xview)
scroll_y.config(command=text.yview)


# function for ask color
def ask_color1():
    color = askcolor(title=("choose \n font Color"))
    if color:
        text.config(fg=color[1])


# choose color via menu bar

ask_color = Menu(main_menu,tearoff=0)
ask_color.add_command(label="Choose font color",command=ask_color1)
main_menu.add_cascade(label="Font Color",menu=ask_color)


# Night Mode
# night_mode = Menu(main_menu,tearoff = 0)
# # night_mode.add_command(label="Night Mode")
# main_menu.add_cascade(label="Night Mode",menu = night_mode)

# Image for Night Mood
night_mode = Image.open()

window.mainloop()
