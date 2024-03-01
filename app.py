# app.py

from flask import Flask, render_template, request

import re

app = Flask(__name__)

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

@app.route('/')
def custom_home():
    return render_template('custom_home.html')

@app.route('/custom_regex_tester', methods=['GET', 'POST'])
def custom_regex_tester():
    if request.method == 'POST':
        test_string = request.form['test_string']
        regex_pattern = request.form['regex_pattern']

        try:
            re.compile(regex_pattern)
            matches = re.findall(regex_pattern, test_string)
            return render_template('custom_regex_tester.html', test_string=test_string, regex_pattern=regex_pattern, matches=matches)
        except re.error as e:
            error_message = f"Error in regex pattern: {str(e)}"
            return render_template('custom_regex_tester.html', error_message=error_message, test_string=test_string, regex_pattern=regex_pattern)

    return render_template('custom_regex_tester.html')

@app.route('/custom_email_validation', methods=['GET', 'POST'])
def custom_email_validation():
    if request.method == 'POST':
        email_to_validate = request.form['email_to_validate']
        is_valid = is_valid_email(email_to_validate)
        return render_template('custom_email_validation.html', email_to_validate=email_to_validate, is_valid=is_valid)

    return render_template('custom_email_validation.html')

if __name__ == '__main__':
    app.run(debug=True)
