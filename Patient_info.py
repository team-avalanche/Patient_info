from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('Patient_Data.csv')

@app.route('/')
def index():
    return render_template('index_patient.html')

@app.route('/result', methods=['POST'])
def result():
    appointment_id = request.form['appointment_id']

    # Check if the AppointmentID exists in the dataset
    if df['AppointmentID'].isin([int(appointment_id)]).any():
        patient_info = df[df['AppointmentID'] == int(appointment_id)].to_dict(orient='records')[0]
        return render_template('result_patient.html', patient_info=patient_info)
    else:
        return render_template('index_patient.html', error_message='Invalid AppointmentID. Please try again.')

if __name__ == '__main__':
    app.run(debug=True)
