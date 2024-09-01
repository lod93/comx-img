## ⚠️ Warning: Experimental Stage

**This project is currently an experiment and is not fully functional yet.**  
Use with caution, and expect significant changes or issues as development progresses.

ComX-Img is a decentralized system for generating and validating images using AI models within the CommuneX protocol. This repository contains the implementation for both mining (image generation) and validation (image scoring) components. The system utilizes various AI models for generating images and validating them against given prompts.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Setup](#setup)
- [Mining Process](#mining-process)
- [Validation Process](#validation-process)
- [Running the System](#running-the-system)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

ComX-Img integrates with the CommuneX protocol to offer a decentralized image generation and validation system. The mining component generates images based on textual prompts using a generative model, while the validation component assesses the quality of the generated images against the original prompts.

## Requirements

To run the mining and validation components, ensure you have the following dependencies installed:

communex typer uvicorn keylimiter pydantic-settings substrate-interface torch transformers Pillow 

You can install these dependencies using:
pip install -r requirements.txt


## Setup

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/lod93/comx-img.git
    cd comx-img
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure Your Environment:**

   Create a configuration file `config.yaml` in the root directory of the project. Ensure it contains the necessary settings for both mining and validation.

## Mining Process

The mining component generates images based on textual prompts using a specified generative model. The core logic is implemented in the `miner/model.py` file.

### To Run the Miner:

1. **Prepare Your Mining Script:**

    Edit `miner/model.py` to use the appropriate generative model and settings.

2. **Start the Mining Server:**

    ```bash
    python miner/model.py
    ```

## Validation Process

The validation component evaluates the generated images by comparing the image descriptions to the original prompts. The core logic is implemented in the `validator/validator.py` file.

### To Run the Validator:

1. **Prepare Your Validation Script:**

    Edit `validator/validator.py` to integrate the BLIP and CLIP models and set the scoring logic.

2. **Start the Validation Server:**

    ```bash
    python validator/validator.py
    ```

## Running the System

1. **Start the Mining Component:**

    Ensure the mining component is running and generating images based on prompts.

2. **Start the Validation Component:**

    Ensure the validation component is running and scoring the generated images.

3. **Continuous Operation:**

    The validation loop will continuously process new images and update scores based on the configured interval.

## Configuration

Configuration for both mining and validation can be managed through the `config.yaml` file. Customize the settings for models, network parameters, and operational intervals as needed.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
