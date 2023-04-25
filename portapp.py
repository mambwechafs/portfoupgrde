from flask import Flask, render_template, request, flash, redirect
from flask_mail import Mail, Message


app = Flask(__name__)

app.config['FLASK_DEBUG'] = True
# Secret Key
app.config['SECRET_KEY'] = "fdaiihqerhgfj%vjfda658"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'chafungwamambwe@gmail.com' # Replace with your email address
app.config['MAIL_PASSWORD'] = '' # Replace with your email password or app-specific password
app.config['MAIL_DEFAULT_SENDER'] = 'chafungwamambwe@gmail.com' # Replace with your email address

mail = Mail(app)

@app.route('/')
def my_home():
    return render_template('index.html')



@app.route('/send_message', methods=['POST'])
def send_message():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        try:
            # send email using Flask-Mail
            msg = Message(subject=subject, sender=email, recipients=['chafungwamambwe@gmail.com'])
            msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
            mail.send(msg)
            # return success message using flash
            flash('Your message has been sent. Thank you!', 'primary')
        except Exception as e:
            # return error message using flash
            flash('There was an error sending your message. Please try again.')
    
    # redirect back to index page
    return redirect('/')

# @app.route('/send_message', methods=['POST'])
# def send_message():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         subject = request.form['subject']
#         message = request.form['message']
        
#         try:
#             # send email using Flask-Mail
#             msg = Message(subject=subject, sender=email, recipients=['chafungwamambwe@gmail.com'])
#             msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
#             mail.send(msg)
#             # return success message
#             return render_template('index.html', sent=True)
#         except Exception as e:
#             # return error message
#             return render_template('index.html', error=True)
