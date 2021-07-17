import random 
import string
import sys
#help create the GUI
import tkinter as tk
#pick the apps
from  tkinter import filedialog, Text
import os
window = tk.Tk()
#label for ask the password
label = tk.Label(window, text= "how long should the password be, please tell me in numbers:")
#function for a copy button 

#function for ccreate the password 
def password():
    Password_length = int(entry.get())
    if Password_length < 12:
        print("to short, make stronger! like more than 12 ")
        sys.exit()
    Password_character = string.digits + string.ascii_letters + string.punctuation
    Password_character = list(Password_character)
    password1 = random.choices(Password_character, k = Password_length)
    password1 = ''.join(password1)
    return password1
    print(password1)
#function for print the password 
entry_password = tk.Entry(window, text = '', font = ("helvetica",24))
entry_password.pack()
def get_password():
   print(password())
   entry_password.insert(0, password()) 
#function for copy the password
def copy_button():
    window.clipboard_clear()
    window.clipboard_append(password())
 
#entry for get the length
entry = tk.Entry(window, bg = 'yellow')
entry.pack()
# buttons for start the action 

button1 = tk.Button(window, text =" get your password ", command = get_password, bg = 'blue') 
button1.pack()
button2 = tk.Button( window, text ="copy", command = copy_button)
button2.pack()
window.mainloop()

