from PIL import Image, ImageFilter
import concurrent.futures
import time
import os

start = time.perf_counter()
# I removed all images to decrease the repo size
# while testing you can add some images in images directory
images_list = [os.path.abspath("images\\"+path) for path in os.listdir("images")]
print(images_list)
size = (2000, 2000)
# Total Time 8.809568


def process_image(image):
    img = Image.open(image)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    base_name = os.path.basename(image)
    img.save(f"processed\{base_name}")
    print(f"image {base_name} processed")


if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image, images_list)

    end = time.perf_counter()
    print(f"Total Time {end-start}")