from skimage.io import imread
from matplotlib import pyplot as plt
import numpy as np
import skimage


def paula_and_matheus_blur():
    ## Original code created during the conversation between Paula and me

    cat = imread(
        r"C:\Users\uzuna\Documents\GITHUB\My_projects\Code_studies\Python\Random_stuff\cat.png"
    )
    pass

    KERNEL = [3, 3]

    blurred_image = np.zeros(cat.shape)

    for iline, line in enumerate(cat):
        for icol, col in enumerate(cat):

            average = 0
            for row_pixel in range(KERNEL[0]):
                for col_pixel in range(KERNEL[1]):
                    kernel_pixel = cat[iline - row_pixel, icol - col_pixel]
                    average = average + kernel_pixel
            average = average / 9
            blurred_image[iline - row_pixel, icol - col_pixel] = average

    ## ------------- -------------- Plot the original and blurred images
    fig, ax = plt.subplot_mosaic(
        [["Original Image", "Blurred_image"]],
        layout="constrained",
        sharex=True,
        sharey=True,
    )

    # blurred_machine = skimage.filters.gaussian(cat, sigma=1.5)

    fig.set_size_inches(7, 7)
    ax["Original Image"].imshow(cat, cmap="gray")
    ax["Original Image"].set_title("Original Image", loc="center")
    ax["Blurred_image"].imshow(blurred_image, cmap="gray")
    ax["Blurred_image"].set_title("Blurred_image", loc="center")
    ax["Blurred_image"].set_xticks([])
    ax["Blurred_image"].set_yticks([])

    plt.draw()
    plt.waitforbuttonpress(0)
    plt.close()

    pass


def chatgpt_blur():
    ## ----------- -------------- ChatGPT verion of the blurring algorithm

    # Define image as a 2D numpy array
    image = imread(
        r"C:\Users\uzuna\Documents\GITHUB\My_projects\Code_studies\Python\Random_stuff\umbrella.bmp"
    )

    # Define kernel as a 3x3 numpy array
    kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

    # Define the dimensions of the image and the kernel
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape

    # Define the padding size
    pad_size = int((kernel_height - 1) / 2)

    # Create a padded image with zeros
    padded_image = np.zeros((image_height + pad_size * 2, image_width + pad_size * 2))
    padded_image[pad_size:-pad_size, pad_size:-pad_size] = image

    # Create a blurred image using list comprehension
    blurred_image = np.array(
        [
            [
                sum(
                    [
                        padded_image[i + m, j + n] * kernel[m, n]
                        for m in range(kernel_height)
                        for n in range(kernel_width)
                    ]
                )
                for j in range(image_width)
            ]
            for i in range(image_height)
        ]
    )

    ## ------------- -------------- Plot the original and blurred images
    fig, ax = plt.subplot_mosaic(
        [["Original Image", "Blurred_image"]],
        layout="constrained",
        sharex=True,
        sharey=True,
    )

    fig.set_size_inches(7, 7)
    ax["Original Image"].imshow(image, cmap="gray")
    ax["Original Image"].set_title("Original Image", loc="center")
    ax["Blurred_image"].imshow(blurred_image, cmap="gray")
    ax["Blurred_image"].set_title("Blurred_image", loc="center")
    ax["Blurred_image"].set_xticks([])
    ax["Blurred_image"].set_yticks([])

    plt.show()
    pass


paula_and_matheus_blur()
