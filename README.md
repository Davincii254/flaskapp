Run `pipenv install` to install the dependencies and `pipenv shell` to enter
your virtual environment before running your code.

```console
$ pipenv install
$ pipenv shell
```


Run the following command to create the `instance` directory with the database
and initialize the database from the existing migration script:

```console
$ flask db upgrade head
```

Confirm the database contains some data on Patients and Doctors `Patient` table and `Doctor` table, either by using the Flask shell or by using a VS Code extension to view the table contents.

```console
$ flask shell
>>> Doctor.query.all()
[]
>>> Patient.query.all()
[]
```


Seed  the table anytime you add either a Patient or a Doctor

```command
$ python seed.py
```


Change into the `lib` directory and configure the `FLASK_APP` and
`FLASK_RUN_PORT` environment variables:

```console
$ cd lib
$ export FLASK_APP=app.py
$ export FLASK_RUN_PORT=5555
```

```console
python app.py
```

In a browser, navigate to 127.0.0.1:5555. You should see this message in your
browser: Hello there, Karibuni