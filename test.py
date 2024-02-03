import requests
import json
import os

os.system("cls" if os.name == "nt" else "clear")

url: str = "https://stablehorde.net/api/v2/generate/async"
status = "check"
id = ""
status_url = "https://stablehorde.net/api/v2/generate/"
compiled_url = status_url + status + id

headers = {
    "POST": "/api/v2/generate/async HTTP/1.1",
    "Host": "stablehorde.net",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://aigallery.app/",
    "Content-Type": "application/json",
    "apikey": "0000000000",
    "Content-Length": "498",
    "Origin": "https://aigallery.app",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site"
}

headers_2 = {
    "GET": "/api/v2/generate/check/6135938d-aa48-4aab-af8f-3bd1ce622721 HTTP/1.1",
    "Host": "stablehorde.net",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://aigallery.app/",
    "Origin": "https://aigallery.app",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site"
}

headers_3 = {
        "GET": "/stable-horde/f67f9a17-d72e-4112-925d-ad7130a019c3.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=246782cc9101762ba914350d8058cd83%2F20240203%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20240203T125326Z&X-Amz-Expires=1800&X-Amz-SignedHeaders=host&X-Amz-Signature=d480fd823a4179bae4c5d110b924b9df9de3ce75c0e42d8a87d05b16a4e4528f HTTP/1.1",
        "Host": "a223539ccf6caa2d76459c9727d276e6.r2.cloudflarestorage.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://aigallery.app/",
        "Origin": "https://aigallery.app",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site"
    }

data = {
    "prompt": "Anime woman. Full body. Naked. Laying on bed. Blonde. Hazel eyes. Steamy, warm climate.\n",
    "params": {
        "steps": 30,
        "n": 1,
        "sampler_name": "k_euler",
        "width": 512,
        "height": 512,
        "cfg_scale": 7,
        "seed_variation": 1000,
        "seed": "",
        "karras": True,
        "denoising_strength": 0.75,
        "tiling": False,
        "hires_fix": False,
        "clip_skip": 1,
        "post_processing": []
    },
    "nsfw": True,
    "censor_nsfw": False,
    "trusted_workers": False,
    "models": ["Hentai Diffusion"],
    "shared": False,
    "r2": True,
    "jobId": "",
    "index": 0,
    "gathered": False,
    "failed": False
}

response = requests.post(url, headers=headers, json=data)

response.raise_for_status()

id = response.json()["id"]
print("Id: ", id)

# continue to check status
while True:

    response = requests.get(f"https://stablehorde.net/api/v2/generate/check/{id}", headers=headers_2)

    response.raise_for_status()

    print(f'Waiting time: {response.json()["wait_time"]}' + '\r')

    if response.json()["done"] == True:

        status = "status"
        break

# get the finished image
response = requests.get(f"https://stablehorde.net/api/v2/generate/status/{id}", headers=headers_3)
image_url = response.json()["generations"][0]["img"]

# download the image
response = requests.get(image_url)

with open("image.png", "wb") as file:
    file.write(response.content)
