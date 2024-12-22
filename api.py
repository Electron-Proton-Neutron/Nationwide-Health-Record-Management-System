import base64

import request
from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for,session
import mysql.connector
from otp import otp
from PIL import Image
import io

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
app.secret_key = 'Sunidhi'


def calculate_age(birthdate):
    """
    Calculate the age based on the birthdate.

    :param birthdate: A datetime.date object representing the birthdate.
    :return: Age as an integer.
    """
    # Get the current date
    today = datetime.today().date()

    # Calculate the age
    age = today.year - birthdate.year

    # Adjust if the birthday hasn't occurred yet this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1

    return age

@app.route('/')
def form():
    return render_template('page.html')

@app.route('/submit', methods=['POST'])
def submit():
    ad_no = request.form.get('aadhar')
    session['ad_no'] = ad_no
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
    ad = session.get('ad_no')
    print (ad)
    h_ID = request.form.get('username')
    h_PW= request.form.get('password')
    cursor.execute("SELECT * FROM users WHERE user_name = %s", (h_ID,))
    doctor= cursor.fetchone()

    if doctor:
        cursor.execute("SELECT * FROM Ad, rp WHERE Ad.Aadhaar_number = rp.id AND Ad.Aadhaar_number = %s",(ad,))
        i=cursor.fetchall()

        binary_data = i[0][10]
        image_stream = io.BytesIO(binary_data)
        image = Image.open(image_stream)

        # Convert image to base64 for HTML display
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")
        im = base64.b64encode(buffered.getvalue()).decode()
        return render_template('hospitaldasboard.html',ad=i[0][0],name=i[0][1],age=calculate_age(i[0][3]),g=i[0][4],em=i[0][6],mf=i[0][2],med=i[0][8],dis=i[0][9],rp=f'data:image/jpeg;base64,{im}')
    else:
        return render_template('hospital2.html')
@app.route('/verify',methods=['POST'])
def verify():
    ad = session.get('ad_no')
    pw = request.form.get('otp')
    cursor.execute("SELECT * FROM Ad, rp WHERE Ad.Aadhaar_number = rp.id AND Ad.Aadhaar_number = %s", (ad,))
    i = cursor.fetchall()
    if int(pw)==otp:

        cursor.execute("SELECT * FROM Ad, rp WHERE Ad.Aadhaar_number = rp.id AND Ad.Aadhaar_number = %s", (ad,))
        i = cursor.fetchall()

        binary_data = i[0][10]
        image_stream = io.BytesIO(binary_data)
        image = Image.open(image_stream)

        # Convert image to base64 for HTML display
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")
        im = base64.b64encode(buffered.getvalue()).decode()
        return render_template('userdashboard.html', ad=i[0][0], name=i[0][1], age=calculate_age(i[0][3]), g=i[0][4],
                               em=i[0][6], mf=i[0][2], med=i[0][8], dis=i[0][9], rp=f'data:image/jpeg;base64,{im}')
    else:
        return render_template('user2.html')
if _name_ == '_main_':
    app.run(debug=True)


# Commit changes and close the connection
conn.commit()
conn.close()