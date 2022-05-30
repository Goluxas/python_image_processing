import tkinter
from tkinter import ttk
import cv2
from PIL import Image, ImageTk


def main(input_image):
    root = tkinter.Tk()
    root.geometry("600x400")
    root.resizable(False, False)
    root.title("Edge Detection Demo")

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)

    slider_value = tkinter.DoubleVar()

    # photo_image = tkinter.PhotoImage(file=input_image)
    image = cv2.imread(input_image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 50, 100)

    # convert to RGB for pillow
    image = cv2.cvtColor(edged, cv2.COLOR_BGR2RGB)

    # convert to PIL
    image = Image.fromarray(image)

    # convert to TK
    photo_image = ImageTk.PhotoImage(image)

    # image dislay label
    def get_current_image():
        return photo_image

    image_label = ttk.Label(root, image=get_current_image())
    image_label.grid(row=0, columnspan=2, sticky="n")

    def get_current_value():
        return f"{slider_value.get():.2f}"

    def slider_changed(event):
        value_label.configure(text=get_current_value())

    # Label for slider
    slider_label = ttk.Label(root, text="Slider:")

    slider_label.grid(column=0, row=1, sticky="w")

    # slider
    slider = ttk.Scale(
        root,
        from_=0,
        to=100,
        orient="horizontal",
        variable=slider_value,
        command=slider_changed,
    )
    slider.grid(column=1, row=1, sticky="we")

    current_value_label = ttk.Label(root, text="Current Value:")

    current_value_label.grid(row=2, columnspan=2, sticky="n", ipadx=10, ipady=10)

    value_label = ttk.Label(root, text=get_current_value())
    value_label.grid(row=3, columnspan=2, sticky="n")

    root.mainloop()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input_image")
    args = parser.parse_args()

    main(args.input_image)
