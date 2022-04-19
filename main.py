from PIL import Image
import sys
import os

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)


def grayscale(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)


def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)


def main(new_width=100):

    if not  len(sys.argv)>1:
        return print('Image path must be the first argument')
    
    if not os.path.exists(sys.argv[1]):
        return print('Image does not exist')

    path = sys.argv[1]
    image = Image.open(path)

    new_image_data = pixels_to_ascii(grayscale(resize_image(image)))

    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index+new_width)]
                            for index in range(0, pixel_count, new_width)])


    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)


if __name__ == "__main__":
    main(200)
