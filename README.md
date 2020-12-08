# easy-inventory

A django webapp for easy inventory management

## Requirements

- Python (3.8+ preferred)
- Create .env (Inside the project folder)
    >*In order to keep your secrets safe you will need to create an .env file as below (with your own secrets):*

    Example .env file content:

    ```sh
    # Envs for settings.py
    DEBUG=1
    DJANGO_SECRET_KEY=!4s9aw#%qbz+b3y30629d)vp^x#o(5^q@j8*@i*%qydl##&!j=
    DB_NAME=app
    DB_HOST=127.0.0.1
    DB_PORT=5432
    DB_USER=postgres
    DB_PASSWORD=supersecretpassword
    # Envs for docker-compose postgres image
    POSTGRES_DB=app
    POSTGRES_PORT=5432
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=supersecretpassword
    ```

## RUN OPTIONS

1. [Run with pyenv](#run-with-pyenv)
2. [Run with docker-compose (development)](#run-with-docker-compose-development)
3. [Run with docker-compose (production)](#run-with-docker-compose-production)

## Run with pyenv

>*We will use a python version manager called pyenv*

- ### Step 1 - Setup pyenv ([full guide](https://realpython.com/intro-to-pyenv/))

    1. Build required dependencies in order to install pyenv library

        ```sh
        $ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
        libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
        libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl
        ```

    2. Install pyenv

        ```sh
        $ curl https://pyenv.run | bash
        ```

    3. Edit your ~/.bashrc configuration file, add these lines at the end of it:
        > You can use ```$ sudo nano ~/.bashrc to edit```
        ```sh
        export PATH="$HOME/.pyenv/bin:$PATH"
        eval "$(pyenv init -)"
        eval "$(pyenv virtualenv-init -)"
        ```

    4. Reload shell

        ```sh
        $ exec "$SHELL"
        ```

    5. Install python v3.8.5

        > *You can install any version you want later but now we will use 3.8.5 to run our project*

        ```sh
        $ pyenv install 3.8.5
        ```

- ### Step 2 - Setup project

    > *Inside the project folder*
    1. Create virtual enviroment for our project

        ```sh
        $ pyenv virtualenv 3.8.5 easy-inventory
        ```

    2. Activate it

        ```sh
        $ pyenv local easy-inventory
        ```

    3. Install dependencies manager

        ```sh
        $ pip install poetry
        ```

    4. Install project dependencies

        ```sh
        $ poetry install
        ```

- ### Step 3 - Setup database

    >*We will use PostgreSQL as DB*

    Run it directly from Docker image as below:

    ```sh
    $ docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=supersecretpassword -e POSTGRES_DB=app postgres:11-alpine
    ```

    >*Note: Replace "supersecretpassword" password and "app" db name with yours configured in .env file*

- ### Step 4 - Run project

    >*If is the first time you run postgresql container, you need execute ```$ python manage.py migrate``` first*

    ```$ python manage.py runserver```

## Run with docker-compose (development)

```sh
$ docker-compose up --build
```

## Run with docker-compose (production)

```sh
$ docker-compose -f docker-compose-deploy.yml up --build
```
