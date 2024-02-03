from __future__ import annotations

import requests
import json
from fake_useragent import UserAgent
import os

class API(object):

    def __init__(self) -> None:

        # Paths
        self.__headers_path = "res/headers/"
        self.__models_path = "res/models/"

        # Urls
        self.__generate_url = "https://stablehorde.net/api/v2/generate/async"
        self.__check_url = "https://stablehorde.net/api/v2/generate/check/"
        self.__status_url = "https://stablehorde.net/api/v2/generate/status/"

        self.__id = None

    def update_models(self) -> None:

        # collect models from url
        _url: str = "https://stablehorde.net/api/v2/status/models"

        # get models
        response = requests.get(_url)

        # check for errors
        response.raise_for_status()

        # iterate through response's json and overwrite models json
        with open(f"{self.__models_path}/models.json", "w") as f:
            
            # append models to json
            json.dump(response.json(), f, separators=(',', ':'))

    def check(self) -> str:

        # attempt to load headers
        try:
            with open(f"{self.__headers_path}/check.json", "r") as f:
                headers = json.load(f)
                headers["User-Agent"] = UserAgent().random
        except:

            return

        # check status
        response = requests.get(f"{self.__check_url}{self.__id}", headers=headers)
        response.raise_for_status()

        return (response.json()["done"], response.json()["wait_time"])

    def send_request(self, prompt: str, config: dict) -> None:

        # attempt to load headers
        try:
            with open(f"{self.__headers_path}/generate.json", "r") as f:
                headers = json.load(f)
                headers["User-Agent"] = UserAgent().random
        except:

            return
        
        # prepare request data
        model = config.pop("model")

        config["n"] = 1
        config["post_processing"] = []

        data = {
            "prompt": prompt,
            "params": config,
            "nsfw": True,
            "censor_nsfw": False,
            "trusted_workers": False,
            "models": [model],
            "shared": False,
            "r2": True,
            "jobId": "",
            "index": 0,
            "gathered": False,
            "failed": False
        }
        
        # send request
        response = requests.post(self.__generate_url, headers=headers, json=data)
        response.raise_for_status()

        # get id
        self.__id = response.json()["id"]

    def model_exists(self, model_name: str) -> bool:

        # attempt to load models
        try:
            with open(f"{self.__models_path}/models.json", "r") as f:
                models = json.load(f)

                for model in models:

                    if model["name"] == model_name:
                        return True
                    
                return False
        except:

            return False

        # check if model exists
        return model in models

    def get_image(self, save_path: str, file_name: str) -> None:

        # attempt to load headers
        try:
            with open(f"{self.__headers_path}/status.json", "r") as f:
                headers = json.load(f)
                headers["User-Agent"] = UserAgent().random
        except:

            return

        # get the finished image
        response = requests.get(f"{self.__status_url}{self.__id}", headers=headers)
        image_url = response.json()["generations"][0]["img"]

        # download the image
        response = requests.get(image_url)
        response.raise_for_status()

        # check if save dir exists
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # save the image
        with open(f"{save_path}/{file_name}.png", "wb") as f:
            f.write(response.content)
