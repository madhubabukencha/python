import requests
import os
import random, string
import time
import concurrent.futures


start = time.perf_counter()

image_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
]

os.chdir("images")


def download_img(image_url):
    content = requests.get(image_url).content
    file_name = "".join(random.choices(string.ascii_letters+string.digits, k=10))+".jpg"
    with open(file_name, "wb") as file:
        file.write(content)


with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(download_img, image_urls)

end = time.perf_counter()
print(f"Total time: {end-start:.2f}")
