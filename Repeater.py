import tkinter as tk
from tkinter import *

def repeat_word():
    word = input_word.get()
    
    try:
        repeat_count = int(input_num.get())
    except ValueError:
        results.config(state="normal")  # Temporarily enable to change text
        results.delete("1.0", "end")
        results.insert("1.0", "Please enter a valid number")
        results.config(state="disabled")
        return
    
    repeated_text = (word + " ") * repeat_count if repeat_count > 0 else ""
    
    results.config(state="normal")  # Temporarily enable to change text
    results.delete("1.0", "end")
    results.insert("1.0", repeated_text.strip())
    results.config(state="disabled")

# Window options
main_window = tk.Tk()
title = Label(main_window, text="Welcome to repeater!", font=("Arial", 16, "bold"))
title.pack()
main_window.title("Repeater")
main_window.geometry("1024x760")


# Entry options
r = Label(main_window, text="What word do you want to repeat?", font=("Arial", 10))
r.pack(padx=5, pady=20)
r.place(x=10, y=50)

input_word = Entry(main_window, width=30, font=("Arial", 10))
input_word.pack(padx=10, pady=10)
input_word.place(x=250, y=50)

n = Label(main_window, text="How many times do you want to repeat it? (maximum 200)", font=("Arial", 10))
n.pack()
n.place(x=10, y=100)

input_num = Spinbox(main_window, from_=0, to=200, increment=1, width=10, font=("Arial", 10))
input_num.pack()
input_num.place(x=380, y=100)

# Add a button to trigger the repetition
repeat_button = Button(main_window, text="Repeat Word", command=repeat_word, 
                      bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
repeat_button.place(x=500, y=95, width=120, height=30)

# Results options
results = Text(main_window, width=95, height=25, relief="solid", background="white",
              font=("Arial", 10), wrap="word", state="disabled")
results.pack()
results.place(x=70, y=150)

# Add some instruction text
instruction = Label(main_window, 
                   text="Type a word in the top field, choose how many times to repeat it, then click 'Repeat Word'",
                   font=("Arial", 9), fg="#555")
instruction.place(x=70, y=700)

main_window.mainloop()