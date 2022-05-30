import tkinter
from tkinter import ttk
import cv2
from PIL import Image, ImageTk

MIN_THRESH_RANGE = 0
MAX_THRESH_RANGE = 1500


def main(input_image):
    root = tkinter.Tk()
    root.geometry("600x400")
    root.resizable(False, False)
    root.title("Edge Detection Demo")

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)

    min_threshold_slider_value = tkinter.IntVar(value=50)
    max_threshold_slider_value = tkinter.IntVar(value=100)

    # photo_image = tkinter.PhotoImage(file=input_image)
    base_image = cv2.imread(input_image)
    base_gray = cv2.cvtColor(base_image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(base_gray, 50, 100)

    # convert to RGB for pillow
    image = cv2.cvtColor(edged, cv2.COLOR_BGR2RGB)

    # convert to PIL
    image = Image.fromarray(image)

    # convert to TK
    global photo_image
    photo_image = ImageTk.PhotoImage(image)

    # image dislay label
    def get_current_image():
        global photo_image
        min_threshold = int(min_threshold_slider_value.get())
        # trying out setting a threshold delta instead of the range directly
        max_threshold = min_threshold + int(max_threshold_slider_value.get())
        edged = cv2.Canny(
            base_gray,
            min_threshold,
            max_threshold,
        )
        image = cv2.cvtColor(edged, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        photo_image = ImageTk.PhotoImage(image)
        return photo_image

    image_label = ttk.Label(root, image=get_current_image())
    image_label.grid(row=0, columnspan=2, sticky="n")

    # def get_min_slider_value():
    # return f"{min_threshold_slider_value.get():.2f}"

    def min_threshold_slider_changed(event):
        image_label.configure(image=get_current_image())
        threshold_label.configure(text=get_threshold_text())
        # min_threshold_value_label.configure(text=get_min_slider_value())

    # Label for min val slider
    slider_label = ttk.Label(root, text="Min Threshold:")

    slider_label.grid(column=0, row=1, sticky="w")

    # min val slider
    min_threshold_slider = ttk.Scale(
        root,
        from_=MIN_THRESH_RANGE,
        to=MAX_THRESH_RANGE,
        orient="horizontal",
        variable=min_threshold_slider_value,
        command=min_threshold_slider_changed,
    )
    min_threshold_slider.grid(column=1, row=1, sticky="we")

    # min_threshold_label = ttk.Label(root, text="Min Threshold:")

    # min_threshold_label.grid(row=2, columnspan=2, sticky="n", ipadx=10, ipady=10)

    # min_threshold_value_label = ttk.Label(root, text=get_min_slider_value())
    # min_threshold_value_label.grid(row=3, columnspan=2, sticky="n")

    # def get_max_slider_value():
    # return f"{max_threshold_slider_value.get():.2f}"

    def max_threshold_slider_changed(event):
        image_label.configure(image=get_current_image())
        threshold_label.configure(text=get_threshold_text())
        # max_threshold_value_label.configure(text=get_max_slider_value())

    # Label for max val slider
    slider_label = ttk.Label(root, text='Threshold "Gap":')

    slider_label.grid(column=0, row=4, sticky="w")

    # max val slider
    max_threshold_slider = ttk.Scale(
        root,
        from_=MIN_THRESH_RANGE,
        to=MAX_THRESH_RANGE,
        orient="horizontal",
        variable=max_threshold_slider_value,
        command=max_threshold_slider_changed,
    )
    max_threshold_slider.grid(column=1, row=4, sticky="we")

    # max_threshold_label = ttk.Label(root, text='Threshold "Gap":')

    # max_threshold_label.grid(row=5, columnspan=2, sticky="n", ipadx=10, ipady=10)

    # max_threshold_value_label = ttk.Label(root, text=get_max_slider_value())
    # max_threshold_value_label.grid(row=6, columnspan=2, sticky="n")

    def get_threshold_text():
        min_thresh = min_threshold_slider_value.get()
        max_thresh = min_thresh + max_threshold_slider_value.get()
        return f"Threshold: {min_thresh} - {max_thresh}"

    # label for threshold values
    threshold_label = ttk.Label(root, text=get_threshold_text())
    threshold_label.grid(row=6, columnspan=2, sticky="n")

    root.mainloop()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input_image")
    args = parser.parse_args()

    main(args.input_image)
