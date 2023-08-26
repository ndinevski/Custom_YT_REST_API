**# Custom-Youtube-API**

## Description
A custom REST API for extracting and storing historical YouTube analytics data. The goal is to provide this data to the creator(s) for easier understanding of the performance of their and other people's channel(s).

Project has following functionalities:
    - Authentication
    - Django REST API for getting, posting and deleting YouTube analytics data (views, subscriptions, videos, most liked videos, comments,...)
    - React Frontend consuming the API (with login, search, statistics and videos page)
    - Data saved in DB

How to setup project:
    1. First clone the repository
    ```
    $ git clone https://github.com/ndinevski/Custom_YT_REST_API
    ```
    2. Setting up python virtual environment and activating it
    ```
    $ python -m venv .venv
    $ .\.venv\Scripts\activate
    ```
    3. Install all dependancies in ./dependancies.txt 
    4. Set up your settings.py, from the ./settings_example.txt,
       Configure your Postgres DB, OAuth credentials and YT_API_KEY
    5. Once the DB has been properly set up, run migrations
    ```
    $ python manage.py makemigrations
    $ python manage.py migrate
    ```
    6. Go in the ./frontend folder and run
    ```
    $ npm run build
    ```
    Finally, go back to root directory and run the server
    ```
    $ python manage.py runserver
    ```

Technologies used:
 - Python Django
 - React
 - PostgreSQL
 - Git
