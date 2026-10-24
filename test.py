import customtkinter as ctk

# 1. Set appearance mode (System, Dark, or Light)
ctk.set_appearance_mode("Light")  # Try switching to "Dark" or "Light"

# 2. Load your custom theme JSON file
ctk.set_default_color_theme("app_theme.json")

# 3. Create the main application window
app = ctk.CTk()
app.geometry("500x650")
app.title("CustomTkinter Theme Test")

# --- Test Widgets ---

# Title Label
title_label = ctk.CTkLabel(app, text="Theme Test Dashboard", font=ctk.CTkFont(size=18, weight="bold"))
title_label.pack(pady=15)

# Entry Widget
entry = ctk.CTkEntry(app, placeholder_text="Type something here...")
entry.pack(pady=10, padx=20, fill="x")

# Button
def on_button_click():
    print("Button clicked! Text:", entry.get())

button = ctk.CTkButton(app, text="Click Me", command=on_button_click)
button.pack(pady=10, padx=20, fill="x")

# Checkbox
checkbox = ctk.CTkCheckBox(app, text="Check Box Option")
checkbox.pack(pady=10)

# Switch
switch = ctk.CTkSwitch(app, text="Toggle Switch")
switch.pack(pady=10)

# Slider
slider = ctk.CTkSlider(app, from_=0, to=100)
slider.set(50)
slider.pack(pady=10, padx=20, fill="x")

# Option Menu
option_menu = ctk.CTkOptionMenu(app, values=["Option 1", "Option 2", "Option 3"])
option_menu.pack(pady=10)

# Textbox
textbox = ctk.CTkTextbox(app, height=80)
textbox.pack(pady=10, padx=20, fill="x")
textbox.insert("0.0", "This is a CTkTextbox.\nYou can type multiple lines here.")

# Run the application
app.mainloop()