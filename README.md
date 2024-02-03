# AI Gallery Wrapper

Welcome to AI Gallery Wrapper, a powerful CLI tool for interacting with the AI Gallery website powered by StableHorde. This wrapper provides a seamless command-line interface for generating captivating images using various AI models with high-level customization. Whether you're a beginner or an experienced user, this README will guide you through the process of setting up and generating your first image.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Configuration](#configuration)
  - [Generating an Image](#generating-an-image)
- [Examples](#examples)

## Prerequisites

Make sure you have the following prerequisites installed on your system:
- Python 3.7 or higher
- [Requests](https://pypi.org/project/requests/)
- [Fake User Agent](https://pypi.org/project/fake-useragent/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Recentaly/AI-Gallery-Wrapper.git
   cd AI-Gallery-Wrapper
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Configuration

Before generating an image, you need to set up your configuration. Open the `config.json` file in the root directory. The configuration file has the following parameters:

- `"model"`: The Model you'd like to use. A list of them can be found under res/models/models.json. Copy the name and insert it into the JSON.
- `"steps"`: The number of steps the AI should take during the generation process.
- `"sampler_name"`: The name of the sampler to be used.
- `"width"` and `"height"`: The dimensions of the generated image.
- `"cfg_scale"`: The scale of the configuration.
- `"seed_variation"`: Variation in seed values for the generation process.
- `"seed"`: The seed for generating the image. Leave empty for random seed.
- `"karras"`: Whether to use Karras sampler (true/false).
- `"denoising_strength"`: The strength of denoising applied to the generated image.
- `"tiling"`: Whether to use tiling in the generation process (true/false).
- `"hires_fix"`: Whether to apply high-resolution fix (true/false).
- `"clip_skip"`: The skip value for clipping during the generation process.

Update these parameters according to your preferences and save the file.

### Generating an Image

To generate an image, use the following command:

```bash
python ai-cli.py --prompt "Your prompt here" --config config.json
```

- `--prompt`: Specify the prompt that instructs the AI on what to generate.
- `--config`: Provide the path to your configuration file (e.g., `config.json`).

Optional parameters:

- `--output-directory`: Specify the directory where the generated image will be saved (default: "output").
- `--output-filename`: Set the filename for the generated image (default: "OUTPUT").

## Examples

1. Generate an image with a specific prompt and default configuration:

   ```bash
   python ai-cli.py --prompt "A mesmerizing landscape" --config config.json
   ```

2. Generate an image and save it in a custom directory with a custom filename:

   ```bash
   python ai-cli.py --prompt "Abstract art" --config config.json --output-directory my_images --output-filename abstract_image
   ```
