from argparse import ArgumentParser
from res.src.Api import API
import json
import logging

# create logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

parser = ArgumentParser(description='AI CLI')

parser.add_argument('--prompt', help='Prompt. Tells the AI what to generate.', type=str, required=True)
parser.add_argument('--config', help='Path to your config file. Required.', type=str, required=True)
parser.add_argument('--output-directory', help='Output Directory of the generated image', type=str, required=False, default="output")
parser.add_argument('--output-filename', help='Output Filename of the generated image. The .png is pre-provided.', type=str, required=False, default="OUTPUT")

args = parser.parse_args()

# api instance
api = API()

# try accessing config.json
try:
    with open(args.config, "r") as f:
        config = json.load(f)

        # check for model key
        if "model" not in config:
            logger.error("No models found in config file. Exiting..")
            exit()

        else:

            if api.model_exists(config["model"]) == False:
                logger.error(f"Model {config['model']} not found. Exiting..")
                exit()

        # try accessing other config file
        try:
            with open("res/src/required_parameters.json", "r") as f:
                required_config = json.load(f)

                # try loading default config
                try:
                    with open("res/src/default_parameters.json", "r") as f:
                        default_config = json.load(f)

                        for key in required_config.get("params"):
                            if key not in config:
                                logger.warning(f"Key {key} not found in config file. Using default value..")
                                try:    config[key] = default_config[key];  logger.info(f"Key {key} set to default value: {default_config[key]}")
                                except: logger.warning(f"Key {key} not found in default config. Exiting");  exit()

                        # save
                        logger.info("All required keys found. Saving..")
                        with open(args.config, "w") as f:
                            json.dump(config, f, indent=1)                        
                    
                except (FileNotFoundError, PermissionError, OSError):
                    logger.warning("Default config not found. Could cause issues. Continuing..")
                    exit()

        except (FileNotFoundError, PermissionError, OSError):
            logger.error("PRIMARY CONTROL CONFIG FILE NOT FOUND! PLEASE REINSTALL.")
            exit()
    
except (FileNotFoundError, PermissionError, OSError):

    logger.error("Could not access your config file. Exiting..")
    exit()

# send request
api.send_request(args.prompt, config)

# check 
while True:
    done, wait_time = api.check()
    if done:
        break
    else:
        print(f"Time left (may be misleading. Exit if stuck in infinite loop): {wait_time} seconds", end="\r", flush=True)

# log status
logger.info("Done. Getting image..")

# get image
api.get_image(save_path=args.output_directory, file_name=args.output_filename)

                        


