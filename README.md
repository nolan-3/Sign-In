# Sign-In
Tracks which students with free period first actually are at school before the end of first period.

## Setup
This project is built and run using [Flask](https://flask.palletsprojects.com/).

To get started, install the dependencies in `requirements.txt`:
```shell
$ pip install -r requirements.txt
```

**NOTE:** You will also need to create a `password.py` file, to store sensitive information.
 
See `password_template.py` for the example format.

## Running the App
To run the project locally, use flask to open a web server:
```shell
$ flask run
```

And connect to [http://127.0.0.1:5000]() in your browser to interact with the application.

## Testing
Tests for `<module_name>.py` are written in `<module>_test.py` using [pytest](https://docs.pytest.org/en/7.2.x/).

To run all the tests in the current folder:
```shell
$ pytest
```

Alternatively, you can run tests from a specific file:
```shell
$ pytest <module_name>_test.py
```
