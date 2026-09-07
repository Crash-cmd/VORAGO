import customtkinter as ctk

app = ctk.CTk()
app.geometry("500x400")

# 1. Main Frame with locked width/height
main_frame = ctk.CTkFrame(app, width=450, height=350, fg_color="gray20")
main_frame.pack(padx=20, pady=20)
main_frame.pack_propagate(False)  # Prevents main_frame from shrinking/growing based on children

# 2. Configure Grid inside main_frame
# Row 0 expands vertically
main_frame.grid_rowconfigure(0, weight=1)

# Column 0 (Sidebar) stays fixed or controlled; Column 1 (Main content) gets remaining space
main_frame.grid_columnconfigure(0, weight=0)  # Sidebar
main_frame.grid_columnconfigure(1, weight=1)  # Content Area

# 3. Side Panel (sub_frame) - increase its explicit width
side_panel = ctk.CTkFrame(main_frame, width=200, fg_color="royalblue") 
side_panel.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
# 'sticky="nsew"' stretches the panel to fill the entire height of main_frame

# Optional content area frame
content_area = ctk.CTkFrame(main_frame, fg_color="gray30")
content_area.grid(row=0, column=1, sticky="nsew", padx=(0, 10), pady=10)

app.mainloop()