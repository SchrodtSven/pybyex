# https://www.pythoninformer.com/python-libraries/numpy/numpy-and-images/

from PIL import Image
import numpy as np

# width = 5
# height = 4

# array = np.zeros([height, width, 3], dtype=np.uint8)

im = Image.open("test_image_rgb.webp")
#im.show()


box = (0, 0, 200, 200)
region = im.crop(box)
region.show()

# region = region.transpose(Image.Transpose.ROTATE_180)
# region.show()


# im.paste(region, box)


#im.show()
