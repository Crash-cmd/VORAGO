

import tkinter as tk
from tkinter import font

root = tk.Tk()
available_fonts = font.families()
print(f"Your system has {(available_fonts)} font families available to Tkinter.")
root.destroy()
