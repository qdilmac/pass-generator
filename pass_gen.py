# Random Pass Generator with GUI
# Another simple project for me to pass some time and practice
# First time using string library/module -> one of this little project's useful outcomes 
# 20/09/2023 13.08 // Author: Mustafa Osman Dilmaç


import tkinter as tk
import random
import string


def pass_generator():
    pass_length = int(pass_length_var.get())
    include_upper = uppercase_var.get()
    include_nums = num_var.get()
    include_special = special_var.get()

    chars = string.ascii_lowercase
    if include_upper:
        chars += string.ascii_uppercase
    if include_nums:
        chars += string.digits
    if include_special:
        chars += string.punctuation

    if pass_length < 1:
        result_text.delete("1.0", tk.END)  # Clear previous result
        result_text.insert(tk.END, "Password length must be greater than 1.")
        return
    
    generated_password = ''.join(random.choice(chars) for _ in range(pass_length)) # "_" is a dummy variable. Means that I have no intentions of using the loop control variable anywhere in my code
    result_text.config(state=tk.NORMAL) # make the text box editable to insert generated pass
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, generated_password)
    result_text.config(state=tk.DISABLED) # disable the editing so the user cant change it just copies it

def main():
    global uppercase_var
    global num_var
    global special_var
    global pass_length_var
    global result_text

    root = tk.Tk()
    root.title("Password Generator v0.1")
    root.geometry("640x200")
    root.resizable(False,False)

    pass_length_label = tk.Label(root, text="How long would you like your password to be?:",pady=10)
    pass_length_label.pack()
    pass_length_var = tk.StringVar()
    pass_length_entry = tk.Entry(root, textvariable=pass_length_var)
    pass_length_entry.pack()

    uppercase_var = tk.BooleanVar()
    uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase",variable=uppercase_var)
    uppercase_checkbox.pack()

    num_var = tk.BooleanVar()
    num_checkbox = tk.Checkbutton(root, text="Include Numbers",variable=num_var)
    num_checkbox.pack()

    special_var = tk.BooleanVar()
    special_checkbox = tk.Checkbutton(root, text="Include Special Characters",variable=special_var)
    special_checkbox.pack()

    generate_pass_button = tk.Button(root, text="Generate",command=pass_generator)
    generate_pass_button.pack()

    result_text = tk.Text(root, wrap=tk.WORD, height=2, width=40)
    result_text.pack()
    result_text.config(state=tk.DISABLED)

    root.mainloop()

if __name__ == "__main__":
    main()