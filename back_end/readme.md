# Desafio Conecta Nuvem - Backend

## Description
This is basically a Flask api based on Flask's MethodViews.  
The database is a Google's Firebase Realtime Database.  

## Usage
Project available at https://backend.desafioconectanuvem.andrevicente.dev.br. 
The API base URL is `/api/v1`.  
Allowed endpoints and methods:
- `/users`
  - `POST`: creates a new user
- `/user/token`
  - `POST`: creates and returns a new api token for a specific user
- `/contacts`
  - `POST`: creates a new contact in an user contact list
  - `GET`: returns the list of contacts of an user

## Requirements
- python3.9+
- python3-venv
- python3-pip

## Installation
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.pip`
- For development also install requirements.dev.pip, for formatting and linting

## Running
- Populate `.env` file as described in [.env.example](.env.example)
- If the environment is not activated: `source .venv/bin/activate`
- Development
  - `flask run`
- Production
  - `pip install gunicorn`
  - `nohup gunicorn 'src.app:create_app()' &`
    - Example with bind and workers: `nohup gunicorn -w 3 -bind 127.0.0.1:8080 'src.app:create_app()' &`
  - You should use NGINX
  - You should user supervisor instead of nohup


