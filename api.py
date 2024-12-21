import request
import flask
from flask import Flask, request, render_template, redirect, url_for
import mysql.connector
from doctor import doctors
from database import patients
ad_no=0;
conn = mysql.connector.connect(
    host="localhost",  # or your MySQL host
    user="root",
    password="Sunidhi",
    database="Aadhar"
)

# Create a cursor object
cursor = conn.cursor(buffered=True)


app = Flask(_name_)



@app.route('/')
def form():
    return render_template('page.html')

@app.route('/submit', methods=['POST'])
def submit():
    ad_no = request.form.get('aadhar')  # Use .get() to avoid KeyError if field is missing
    selected_option = request.form.get('user-type')  # Use .get() for safety
    cursor.execute("SELECT * FROM Ad WHERE Aadhaar_Number = %s", (ad_no,))
    patient = cursor.fetchone()

    if selected_option == 'healthcare':
        if patient:
            return render_template('hospital.html')

        else:
            return "No patient found with the given Aadhaar number for healthcare."
    elif selected_option == 'user':
        if patient:
            return render_template('user.html')
        else:
            return "Please enter a valid Aadhar number."
    else:
        return "Invalid selection. Please choose a valid option."

@app.route('/login',methods=['POST'])
def login():
    h_ID = request.form.get('username')
    h_PW= request.form.get('password')
    cursor.execute("SELECT * FROM users WHERE user_name = %s", (h_ID,))
    doctor= cursor.fetchone()
    if doctor:
        cursor.execute("SELECT * FROM Ad, rp WHERE Ad.Aadhaar_number = rp.Aadhar_number AND Ad.Aadhaar_number = %s",(ad_no,))
        return render_template('hospitaldasboard.html')
@app.route('/verify',methods=['POST'])
def verify():
        return render_template('userdashboard.html')

if _name_ == '_main_':
    app.run(debug=True)


# Commit changes and close the connection
conn.commit()
conn.close()