from PIL import Image
from typing import Callable
import customtkinter as ctk


primary_color="#7176B7"
secondary_color="#6164A1"

ctk.set_appearance_mode("dark")


def create() -> ctk.CTk:
    app = ctk.CTk()
    app.title("Face Detection Count")
    app.geometry("600x500")
    app.resizable(False, False)
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure((0, 1), weight=1)
    return app


def draw_image(app: ctk.CTk, image: Image) -> None:
    ctk_image = ctk.CTkImage(image, size=(600, 400))
    label_image = ctk.CTkLabel(app, image=ctk_image, text="")
    label_image.grid(column=0, row=0, padx=10, pady=10, sticky="ew")


def draw_label(app: ctk.CTk, text: str) -> None:
    label_count = ctk.CTkLabel(app, text=text)
    label_count.grid(column=0, row=1, padx=0, pady=0, sticky="ew")


def draw_frame(app: ctk.CTk) -> ctk.CTkFrame:
    frame = ctk.CTkFrame(app)
    frame.grid(column=0, row=2, padx=10, pady=10, sticky="ew")
    return frame


def draw_entry(app: ctk.CTkFrame, text: str, column: int) -> ctk.CTkEntry:
    entry = ctk.CTkEntry(app, placeholder_text=text, width=170)
    entry.grid(column=column, row=0, padx=10, pady=10, sticky="w")
    return entry


def draw_button(app: ctk.CTkFrame, text: str, command: Callable, column: int) -> None:
    button = ctk.CTkButton(app, text=text, width=180, command=command, fg_color=primary_color, hover_color=secondary_color)
    button.grid(column=column, row=0, padx=10, pady=10, sticky="w")