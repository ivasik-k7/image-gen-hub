# image-gen-hub

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v1.json)](https://github.com/astral-sh/ruff)

## Overview

**image-gen-hub** is a Python-based project that integrates multiple image generation providers with RabbitMQ for automated image generation. This project allows users to generate images using different providers (like OpenAI's DALL-E, Stable Diffusion, etc.) and process requests through RabbitMQ queues.

## Features

- **Multiple Image Generation Providers**: Support for various image generation providers, making the system flexible and extensible.
- **RabbitMQ Integration**: Utilizes RabbitMQ for queuing and processing image generation requests, ensuring scalability and reliability.
- **Extensible Architecture**: Easy to add new image generation providers and customize existing ones.
- **Error Handling**: Robust error handling to ensure stable operation.

## Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/ivasik-k7/image-gen-hub.git .
   ```

2. **Install dependencies**:
   Make sure you have `poetry` installed. If not, install it from [here](https://python-poetry.org/docs/#installation).

   ```sh
   poetry install
   ```

3. **Configure RabbitMQ**:
   Update the `rabbit_mq_config.py` file with your RabbitMQ server details.

   ```python
   # .env
   USERNAME = 'your_username'
   PASSWORD = 'your_password'
   HOST = 'localhost'  # or your RabbitMQ server's host
   PORT = 5672  # or your RabbitMQ server's port
   ```

## Usage

1. **Start the RabbitMQ Listener**:

   ```sh
   poetry run python manage.py
   ```

2. **Send Test Message**:
   Use the provided script to send a test message to the RabbitMQ queue.

   ```sh
   poetry run python send_test_message.py
   ```

3. **Implement Image Providers**:
   Extend the `ImageGeneratorProvider` class to add new providers in the `app/providers` directory.
