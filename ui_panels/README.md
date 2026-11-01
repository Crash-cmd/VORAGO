# VORAGO UI Panels

An isolated CustomTkinter UI experiment. It adds reusable navigation panels
without changing `app.py`, question modules, or theme files.

## Files
- `navigation.py`: `VerticalPanel` and `HorizontalPanel`.
- `demo.py`: standalone preview with a live orientation switch.
- `__init__.py`: package exports.

## Run
From the repository root, activate your virtual environment:

```bash
python -m pip install customtkinter
python -m ui_panels.demo
```

## Integrate later
Import the classes:

```python
from ui_panels import VerticalPanel, HorizontalPanel
```

Provide callbacks keyed by `home`, `maths`, `physics`, `chemistry`,
and `settings`. For example:

```python
commands = {
    "home": show_home,
    "maths": show_maths,
    "physics": show_physics,
    "chemistry": show_chemistry,
    "settings": show_settings,
}
```

Left-side layout:

```python
navigation = VerticalPanel(app_window, commands=commands, active="home")
navigation.grid(row=0, column=0, sticky="ns", padx=10, pady=20)
main_frame.grid(row=0, column=1, sticky="nsew")
app_window.grid_columnconfigure(1, weight=1)
app_window.grid_rowconfigure(0, weight=1)
```

Top layout:

```python
navigation = HorizontalPanel(app_window, commands=commands, active="home")
navigation.grid(row=0, column=0, sticky="ew", padx=16, pady=16)
main_frame.grid(row=1, column=0, sticky="nsew")
app_window.grid_columnconfigure(0, weight=1)
app_window.grid_rowconfigure(1, weight=1)
```

Call `panel.set_active("maths")` to change the highlighted item without
running its callback. The components do not create a root window, alter the
appearance mode, or manage application pages; the host app owns those tasks.
