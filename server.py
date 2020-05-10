from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<page_name>')
def about(page_name):
    return render_template(page_name)


def write_data(data_dict):
    with open('database.csv', newline='', mode='a') as database:
        email = data_dict['email']
        subject = data_dict['subject']
        message = data_dict['message']

        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_data(data)
            return redirect('./thank_you.html')
        except:
            return 'Could´t save the data'
    else:
        return 'Something went wrong. Try again'
