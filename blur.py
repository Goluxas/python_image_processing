import cv2
import sys


def blur_display(infile, nogui=False, blur_degree=7, stack_operations=False):
    # The first argument is the image
    image = cv2.imread(infile)

    # conver to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # blur it
    if stack_operations:
        blurred_image = cv2.GaussianBlur(gray_image, (blur_degree, blur_degree), 0)
    else:
        blurred_image = cv2.GaussianBlur(image, (blur_degree, blur_degree), 0)

    if nogui:
        cv2.imwrite("test_blurred.png", blurred_image)
    else:

        # Show all 3 images
        cv2.imshow("Original Image", image)
        cv2.imshow("Gray Image", gray_image)
        cv2.imshow("Blurred Image", blurred_image)

        cv2.waitKey(0)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("input_image")
    parser.add_argument("-f", action="store_true")
    parser.add_argument(
        "-b",
        type=int,
        default=7,
        help="Degree of blur. Must be odd number.",
    )
    parser.add_argument(
        "-s",
        action="store_true",
        help="Do both operations (output a gray and blurred image)",
    )
    args = parser.parse_args()

    assert args.b % 2 == 1
    blur_display(args.input_image, args.f, args.b, args.s)
