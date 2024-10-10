from PIL import Image
from tkinter import filedialog
#
import gui
import cnn


app = gui.create()
gui.draw_image(app, Image.open('gui/upload.jpg'))
gui.draw_label(app, f"Upload image in format JPEG to count faces.")
frame = gui.draw_frame(app)
image_resize = gui.draw_entry(frame, "Image resize", 0)
min_face_size = gui.draw_entry(frame, "Min face size", 1)


def button_event() -> None:
    resize = 160 if image_resize.get() == ''  else int(image_resize.get())
    face_size = 28 if min_face_size.get() == '' else int(min_face_size.get())
    try:
        filename = filedialog.askopenfilename()
        image = Image.open(filename)
        image, quantity = cnn.detect_face(image, resize, face_size)
        gui.draw_image(app, image)
        gui.draw_label(app, f"Total {quantity} faces detected.")
    except AttributeError:
        print("Deu erro aqui ó")

gui.draw_button(frame, "Upload Image", button_event, 2)
app.mainloop()