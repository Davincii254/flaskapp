from flask_sqlalchemy import SQLAlchemy  # Import the SQLAlchemy class for database interactions
from sqlalchemy_serializer import SerializerMixin  # Import SerializerMixin to easily serialize model objects

# Create an instance of the SQLAlchemy class
db = SQLAlchemy()

# Define the Doctor model class
class Doctor(db.Model, SerializerMixin):
    # Set the table name for the model
    __tablename__ = 'doctors'

    # Define the columns for the table
    id = db.Column(db.Integer, primary_key=True)  # Primary key column
    name = db.Column(db.String)  # Column for storing the doctor's name

    # Define a relationship to the Patient model
    patients = db.relationship('Patient', backref='doctors')

    # Specify rules for serialization
    serialize_rules = ('-patients.doctors',)

# Define the Patient model class
class Patient(db.Model, SerializerMixin):
    # Set the table name for the model
    __tablename__ = 'patients'

    # Define the columns for the table
    id = db.Column(db.Integer, primary_key=True)  # Primary key column
    name = db.Column(db.String)  # Column for storing the patient's name
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))  # Foreign key to the doctors table

    # Specify rules for serialization
    serialize_rules = ('-doctors.patient',)
