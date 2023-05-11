"""
    Get the RGB value of the pixel.
    Calculate tr, tg and tb using the formula

    tr = 0.393R + 0.769G + 0.189B
    tg = 0.349R + 0.686G + 0.168B
    tb = 0.272R + 0.534G + 0.131B

    Take the integer value.

    Set the new RGB value of the pixel as per the following condition:

    If tr > 255 then r = 255 else r = tr
    If tg > 255 then g = 255 else g = tg
    If tb > 255 then b = 255 else b = tb

"""
from PIL import Image, ImageOps

from skimage.io import imread
from matplotlib import pyplot as plt
import numpy as np

cute_cat = imread(r"C:\Users\uzuna\Documents\GITHUB\My_projects\Code_studies\Python\Random_stuff\cute_cat.jpg")
image_path = r"C:\Users\uzuna\Documents\GITHUB\My_projects\Code_studies\Python\Random_stuff\cute_cat.jpg"
sepia_image = np.zeros(cute_cat.shape, np.uint8)


def apply_sepia_filter(image_path):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to grayscale
    grayscale_image = ImageOps.grayscale(image)

    # Apply sepia tone
    sepia_tone = (87, 60, 40)
    highlight_color = (255, 240, 192)
    sepia_image_PIL = ImageOps.colorize(
        grayscale_image,
        sepia_tone,
        highlight_color,
    )

    return sepia_image_PIL


for iline, line in enumerate(cute_cat):
    for icol, col in enumerate(cute_cat):
        pixel = cute_cat[iline, icol]
        R = pixel[0]
        G = pixel[1]
        B = pixel[2]

        if int((0.393 * R) + (0.769 * G) + (0.189 * B)) > 255:
            R = 255
            sepia_image[iline, icol][0] = R
        else:
            R = int((0.393 * R) + (0.769 * G) + (0.189 * B))
            sepia_image[iline, icol][0] = R

        if int((0.349 * R) + (0.686 * G) + (0.168 * B)) > 255:
            G = 255
            sepia_image[iline, icol][1] = G
        else:
            G = int((0.349 * R) + (0.686 * G) + (0.168 * B))
            sepia_image[iline, icol][1] = G

        if int((0.272 * R) + (0.534 * G) + (0.131 * B)) > 255:
            B = 255
            sepia_image[iline, icol][2] = B
        else:
            B = int((0.272 * R) + (0.534 * G) + (0.131 * B))
            sepia_image[iline, icol][2] = B

# Example usage
pillow_sepia = apply_sepia_filter(image_path)

fig, ax = plt.subplot_mosaic(
    [["Original Image", ".", "Sepia_image"], [".", "pillow_sepia", "."]],
    layout="constrained",
    sharex=True,
    sharey=True,
)

fig.set_size_inches(7, 7)
ax["Original Image"].imshow(cute_cat)
ax["Original Image"].set_title("Original Image", loc="center")
ax["Sepia_image"].imshow(sepia_image)
ax["Sepia_image"].set_title("Sepia_image", loc="center")
ax["pillow_sepia"].imshow(pillow_sepia)
ax["pillow_sepia"].set_title("Sepia_image", loc="center")
ax["Sepia_image"].set_xticks([])
ax["Sepia_image"].set_yticks([])


plt.draw()
plt.show()
plt.close()
