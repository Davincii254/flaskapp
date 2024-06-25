from flask import Flask, make_response, jsonify  # Import necessary classes and functions from the Flask library
from flask_migrate import Migrate  # Import the Migrate class for handling database migrations
from models import db, Patient, Doctor  # Import the SQLAlchemy db instance and the Patient and Doctor models
from flask_restful import Resource, Api  # Import Resource and Api classes from flask_restful for creating RESTful APIs

# Initialize the Flask application
app = Flask(__name__)

# Set the database URI for SQLAlchemy to use an SQLite database named 'flaskapp.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskapp.db'

# Create an instance of the Migrate class to handle database migrations and bind it to the app and db
migrate = Migrate(app, db)

# Initialize the app with the SQLAlchemy db instance
db.init_app(app)

# Create an instance of the Api class to add RESTful resources to the app
api = Api(app)

# Define a route for the root URL with GET and POST methods allowed
@app.route('/', methods=['GET','POST'])
def home():
    # Return a simple HTML greeting message
    return '<h1>Hello there, Karibuni</h1>'

# Define a route for fetching a patient by their ID
@app.route('/patients/<int:id>')
def getpatient(id):
    # Query the database for the patient with the specified ID
    ourpatient = Patient.query.filter_by(id=id).first()
    # Create a dictionary with the patient's name and their doctor's name
    patientobj = {"patient-name": ourpatient.name, "doctor": ourpatient.doctors.name}
    # Create a response with the patient object in JSON format and a status code of 200 (OK)
    resp = make_response(jsonify(patientobj), 200)
    # Return the response to the client
    return resp

# Define a resource class for handling HTTP requests related to doctors
class DoctorsRoutes(Resource):
    # Define a GET method to fetch all doctors
    def get(self):
        doctorslist = []  # Initialize an empty list to store doctor data
        all_doctors = Doctor.query.all()  # Query the database for all doctors
        # Iterate over each doctor and convert them to a dictionary
        for i in all_doctors:
            docObj = i.to_dict()  # Convert the doctor object to a dictionary
            doctorslist.append(docObj)  # Add the dictionary to the list
        # Create a response with the list of doctors in JSON format and a status code of 200 (OK)
        response = make_response(jsonify(doctorslist), 200)
        # Return the response to the client
        return response
    
    # Uncomment and implement the POST method if needed
    # def post(self):
    #     return '<h1>Uko kwa Doctors</h1>'

# Add the DoctorsRoutes resource to the API with the endpoint '/doctors'
api.add_resource(DoctorsRoutes, '/doctors')  # Accessible at /doctors

# Check if the script is being run directly (i.e., not imported as a module)
if __name__ == '__main__':
    # Run the Flask application on the default port (5000) with debug mode enabled
    app.run()
