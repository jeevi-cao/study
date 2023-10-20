from PIL import Image, ImageSequence
from PIL import features


image_old = '0o3ESyUzcxc.gif'
sequence = []
im = Image.open(image_old)
for frame in ImageSequence.Iterator(im):
    sequence.append(frame.copy())

image_new = './gif-test-2.webp'
sequence[0].save(image_new, save_all=True,  append_images=sequence[1:])
