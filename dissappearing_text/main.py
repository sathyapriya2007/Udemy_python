import tkinter as tk

# Function to clear text if user stops typing
def reset_timer(event=None):
    global timer
    window.after_cancel(timer)
    timer = window.after(5000, clear_text)   # 5 seconds

def clear_text():
    text_box.delete("1.0", tk.END)

# Create window
window = tk.Tk()
window.title("Disappearing Text App")
window.geometry("500x300")

# Text box
text_box = tk.Text(window, font=("Arial", 14))
text_box.pack(expand=True, fill="both")

# Bind typing event
text_box.bind("<Key>", reset_timer)

# Timer
timer = window.after(5000, clear_text)

window.mainloop()