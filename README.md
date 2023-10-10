# eureka_api 💡
Repository for the Eureka backend microservice, programmed in Python using the Django Framework.

# Requirements 📋
- [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- [Django 4.2](https://docs.djangoproject.com/en/4.2/topics/install/#installing-official-release)
- [Docker](https://www.docker.com/products/docker-desktop/)

# Installation 👩‍💻
### Create virtual ambient in python (only first time) 🐍

###### Windows

    python -m venv venv

###### Linux

    virtualenv -p python3.11 venv

### Activate the venv 🗺

###### Windows:

    venv\Scripts\activate

###### Linux:

    source venv/bin/activate

### Install the requirements 😋

    pip install -r requirements.txt

### Compose the docker (only first time) 🐋

    cd docker
    
    docker-compose up -d

### Run the migrations  🤩
    
    python manage.py migrate

### Run the tests 🧪

    pytest

### To run local set .env file 🤗

    STAGE = TEST

