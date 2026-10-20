import customtkinter as ctk
from maths import button_action  # Import your function

app = ctk.CTk()
app.geometry("300x200")

# ⚠️ CRITICAL: Do NOT put parentheses () after button_action. 
# Writing `command=button_action()` calls it instantly on startup.
# Writing `command=button_action` passes it as a reference to be run on click.
btn = ctk.CTkButton(app, text="Click Me", command=button_action)
btn.pack(pady=40)

app.mainloop()