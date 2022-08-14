# Development portfolio website

A convenient layout for your portfolio made with Python and Django.

## Licensing

You can freely use all materials of this repository except for the QuickNode logotype.

## Running the website locally

In your command shell 
Create a Python virtual environment and activate it:

    python3 -m venv venv
    source venv/bin/activate

(Linux or Mac)

    python3 -m venv venv
    venv\Scripts\activate.bat

(Windows)

Install the requirements:

    pip install -r requirements.txt

Replace the file `venv/lib/python3.8/site-packages/markdownx/urls.py`, where `venv` is your Python virtual enrivonment directory, with the file `urls.py` located in the directory `replace` of this project.

Finally, launch the website via the Python server:

    python manage.py runserver 8000

where `8000` is an arbitrary server port.

The website should be available via your browser at `localhost:8000` or `127.0.0.1:8000`.

## Possible deployment strategy

You can use Gunicorn with nginx reverse proxy on a Linux server.

## Contact form

The contact form hides your e-mail address from e-mail harvesting robots using a small [JavaScript code](https://stackoverflow.com/a/16244461/7806269).
