import cv2
import sys


def display(infile, nogui=False):
    image = cv2.imread(infile)
    if nogui:
        cv2.imwrite('test_display2.png', image)
    else:
        cv2.imshow("Image", image)
        cv2.waitKey(0)

if __name__ == "__main__":
    # Read the image. The first command line argument is the image
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('input_image')
    parser.add_argument('-f', action='store_true')
    args = parser.parse_args()

    display(args.input_image,  args.f)