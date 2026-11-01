"""Run with: python -m ui_panels.demo"""
import customtkinter as ctk
from ui_panels.navigation import VerticalPanel, HorizontalPanel

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class PanelDemo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("VORAGO | Navigation Preview")
        self.geometry("1100x700")
        self.minsize(760, 520)
        self.configure(fg_color="#0D1018")

        self.current_page = "home"
        self.panel = None

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.content = ctk.CTkFrame(self, fg_color="transparent")
        self.content.grid(row=0, column=1, sticky="nsew", padx=28, pady=28)
        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_rowconfigure(1, weight=1)

        self.toolbar = ctk.CTkFrame(self.content, fg_color="transparent")
        self.toolbar.grid(row=0, column=0, sticky="ew", pady=(0, 24))
        ctk.CTkLabel(
            self.toolbar, text="PANEL ORIENTATION",
            font=ctk.CTkFont(size=12, weight="bold")
        ).pack(side="left")

        self.orientation = ctk.StringVar(value="Vertical")
        ctk.CTkSegmentedButton(
            self.toolbar, values=["Vertical", "Horizontal"],
            variable=self.orientation, command=self._change_orientation
        ).pack(side="right")

        self.preview = ctk.CTkFrame(
            self.content, corner_radius=22, fg_color="#151B27"
        )
        self.preview.grid(row=1, column=0, sticky="nsew")
        self.preview.grid_columnconfigure(0, weight=1)
        self.preview.grid_rowconfigure(0, weight=1)

        self.page_title = ctk.CTkLabel(
            self.preview, text="Welcome to VORAGO",
            font=ctk.CTkFont(size=32, weight="bold")
        )
        self.page_title.grid(row=0, column=0, padx=30, pady=(100, 12))

        self.page_subtitle = ctk.CTkLabel(
            self.preview, text="Choose a section from the navigation panel.",
            text_color="#9AA6B8", font=ctk.CTkFont(size=15)
        )
        self.page_subtitle.grid(row=1, column=0, padx=30, pady=8, sticky="n")

        self._build_panel()

    def _commands(self):
        return {
            "home": lambda: self._show_page("Home", "Your VORAGO dashboard."),
            "maths": lambda: self._show_page("Mathematics", "Math shortcuts and practice."),
            "physics": lambda: self._show_page("Physics", "Physics shortcuts and concepts."),
            "chemistry": lambda: self._show_page("Chemistry", "Chemistry shortcuts and concepts."),
            "settings": lambda: self._show_page("Settings", "Appearance and application preferences."),
        }

    def _show_page(self, title, subtitle):
        self.page_title.configure(text=title)
        self.page_subtitle.configure(text=subtitle)

    def _build_panel(self):
        if self.panel is not None:
            self.panel.destroy()

        panel_class = VerticalPanel if self.orientation.get() == "Vertical" else HorizontalPanel
        self.panel = panel_class(
            self, commands=self._commands(), active=self.current_page
        )

        if self.orientation.get() == "Vertical":
            self.panel.grid(row=0, column=0, sticky="ns", padx=(18, 0), pady=18)
        else:
            self.panel.grid(
                row=0, column=0, columnspan=2, sticky="ew",
                padx=18, pady=(18, 0)
            )
            self.content.grid(row=1, column=0, columnspan=2, sticky="nsew",
                              padx=28, pady=28)
            self.grid_rowconfigure(1, weight=1)
            self.grid_columnconfigure(0, weight=1)

        if self.orientation.get() == "Vertical":
            self.content.grid(row=0, column=1, sticky="nsew", padx=28, pady=28)
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=1)

    def _change_orientation(self, value):
        self.current_page = self.panel.active if self.panel else "home"
        self._build_panel()


if __name__ == "__main__":
    PanelDemo().mainloop()
