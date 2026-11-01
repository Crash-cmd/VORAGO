"""Reusable VORAGO navigation panels for CustomTkinter.

These widgets are deliberately independent of app.py. They accept callbacks
from the main application and never create a second CTk root window.
"""
from __future__ import annotations

from typing import Callable, Mapping, Optional
import customtkinter as ctk


NAV_ITEMS = (
    ("home", "Home", "⌂"),
    ("maths", "Mathematics", "∑"),
    ("physics", "Physics", "⚛"),
    ("chemistry", "Chemistry", "⚗"),
    ("settings", "Settings", "⚙"),
)


class _NavigationBase(ctk.CTkFrame):
    """Shared navigation behavior for both orientations."""

    def __init__(
        self,
        master,
        commands: Optional[Mapping[str, Callable[[], None]]] = None,
        *,
        brand: str = "VORAGO",
        active: str = "home",
        **kwargs,
    ):
        super().__init__(master, **kwargs)
        self.commands = dict(commands or {})
        self.active = active
        self.brand = brand
        self._buttons = {}

    def _select(self, key: str):
        self.active = key
        self._refresh()
        callback = self.commands.get(key)
        if callback:
            callback()

    def set_active(self, key: str):
        """Update the highlighted item without invoking its callback."""
        if key not in {item[0] for item in NAV_ITEMS}:
            raise ValueError(f"Unknown navigation key: {key}")
        self.active = key
        self._refresh()

    def _make_button(self, parent, key, label, symbol, *, horizontal=False):
        text = f"{symbol}   {label}" if horizontal else f"{symbol}\n{label}"
        button = ctk.CTkButton(
            parent,
            text=text,
            height=42 if horizontal else 62,
            width=112 if horizontal else 76,
            corner_radius=12,
            anchor="center",
            font=ctk.CTkFont(size=13, weight="bold" if key == self.active else "normal"),
            fg_color=("gray82", "#252A36") if key == self.active else "transparent",
            hover_color=("gray75", "#303849"),
            text_color=("gray12", "#F2F4F8"),
            command=lambda item=key: self._select(item),
        )
        self._buttons[key] = button
        return button

    def _refresh(self):
        for key, button in self._buttons.items():
            selected = key == self.active
            button.configure(
                fg_color=("gray82", "#252A36") if selected else "transparent",
                font=ctk.CTkFont(size=13, weight="bold" if selected else "normal"),
            )


class VerticalPanel(_NavigationBase):
    """Compact left navigation rail."""

    def __init__(self, master, commands=None, *, brand="VORAGO",
                 active="home", width=104, **kwargs):
        super().__init__(
            master, commands, brand=brand, active=active,
            width=width, corner_radius=18, **kwargs
        )
        self.grid_propagate(False)
        self.columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self, text=brand, font=ctk.CTkFont(size=15, weight="bold")
        ).grid(row=0, column=0, padx=8, pady=(18, 24))

        for row, (key, label, symbol) in enumerate(NAV_ITEMS, start=1):
            self._make_button(self, key, label, symbol).grid(
                row=row, column=0, padx=10, pady=6, sticky="ew"
            )

        self.rowconfigure(len(NAV_ITEMS) + 1, weight=1)

        ctk.CTkLabel(
            self, text="UI\nPREVIEW", text_color=("gray45", "gray60"),
            font=ctk.CTkFont(size=9, weight="bold")
        ).grid(row=len(NAV_ITEMS) + 2, column=0, pady=16)


class HorizontalPanel(_NavigationBase):
    """Top navigation bar with horizontally arranged sections."""

    def __init__(self, master, commands=None, *, brand="VORAGO",
                 active="home", height=76, **kwargs):
        super().__init__(
            master, commands, brand=brand, active=active,
            height=height, corner_radius=18, **kwargs
        )
        self.grid_propagate(False)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self, text=brand, font=ctk.CTkFont(size=18, weight="bold")
        ).grid(row=0, column=0, padx=(22, 28), sticky="w")

        nav = ctk.CTkFrame(self, fg_color="transparent")
        nav.grid(row=0, column=1, padx=12, pady=10, sticky="e")

        for column, (key, label, symbol) in enumerate(NAV_ITEMS):
            self._make_button(nav, key, label, symbol, horizontal=True).grid(
                row=0, column=column, padx=4, pady=4
            )

        self.columnconfigure(1, weight=0)
