**# Custom-Youtube-API**

## Description
A custom REST API for extracting and storing historical YouTube analytics data. The goal is to provide this data to the creator(s) for easier understanding of the performance of their and other people's channel(s).

Project has following functionalities:<br />
- Authentication<br />
- Django REST API for getting, posting and deleting YouTube analytics data (views, subscriptions, videos, most liked videos, comments,...)<br />
- React Frontend consuming the API (with login, search, statistics and videos page)<br />
- Data saved in DB<br />

How to setup project:<br />
    1. First clone the repository<br />
    ```
    $ git clone https://github.com/ndinevski/Custom_YT_REST_API
    ```
    <br />
    2. Setting up python virtual environment and activating it<br />
    ```
    $ python -m venv .venv
    ```
    <br />
    ```
    $ .\.venv\Scripts\activate
    ```
    <br />
    3. Install all dependancies in ./dependancies.txt <br />
    4. Set up your settings.py, from the ./settings_example.txt,<br />
       Configure your Postgres DB, OAuth credentials and YT_API_KEY<br />
    5. Once the DB has been properly set up, run migrations<br />
    ```
    $ python manage.py makemigrations
    ```
    <br />
    ```
    $ python manage.py migrate
    ```
    <br />
    6. Go in the ./frontend folder and run<br />
    ```
    $ npm run build
    ```
    <br />
    Finally, go back to root directory and run the server<br />
    ```
    $ python manage.py runserver
    ```

Technologies used:
 - Python Django
 - React
 - PostgreSQL
 - Git
