from faker import Faker  # Import the Faker class for generating fake data
from random import choice as rc  # Import the choice function for selecting random items
import random  # Import the random module for generating random numbers
import ipdb  # Import ipdb for interactive debugging

from app import app  # Import the Flask app instance
from models import db, Doctor, Patient  # Import the SQLAlchemy db instance and the Doctor and Patient models

# Create an instance of the Faker class
fake = Faker()

with app.app_context():
    # Delete all existing records in the doctors and patients tables
    Doctor.query.delete()
    Patient.query.delete()

    # Create a list to store doctor objects
    doctors = []
    # Generate 30 fake doctors
    for n in range(30):
        doctor = Doctor(name=fake.name())  # Create a new doctor with a fake name
        doctors.append(doctor)  # Add the doctor to the list
    db.session.add_all(doctors)  # Add all doctors to the session

    # Create a list to store patient objects
    patients = []
    # Generate 60 fake patients
    for i in range(60):
        # Create a new patient with a fake name and assign them to a random doctor
        patient = Patient(name=fake.name(), doctor_id=random.randint(0, 60))
        patients.append(patient)  # Add the patient to the list

    db.session.add_all(patients)  # Add all patients to the session
    db.session.commit()  # Commit the session to save the records to the database
    print("DONE")

    # Fetch the first patient from the database
    mypat = Patient.query.first()
    # Start an interactive debugging session
    ipdb.set_trace()
