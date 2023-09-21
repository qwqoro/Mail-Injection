from flask import Flask
from flask import render_template, request
from smtplib import SMTP
from email.utils import parseaddr
from email.message import EmailMessage
from email.headerregistry import Address

app = Flask(__name__, static_url_path='', static_folder='public', template_folder='public')

@app.route('/')
def index():
  return render_template('index.html', result='')

@app.route('/signup', methods=["GET", "POST"])
def signupPost():
  result = ''
  
  if request.method == "POST":
    email = request.form.get('email')
    password = request.form.get('password')

    if parseaddr(email)[1].split('@')[1] == "hahacking.local":
    
      at = email.index("@")
      msg = EmailMessage()
      msg["From"] = Address("HaHacking", "contact", "hahacking.local")
      msg["To"] = Address("You", email[:at], email[at+1:])
      msg.set_content("Welcome to HaHacking! You have successfully signed up!")
      
      with SMTP("hahacking.local", 25) as s:
        s.send_message(msg)
        result = "Вы успешно зарегистрированы!"
        
    else:
        result = "Допускаются только почты домена hahacking.local!"

  return render_template('index.html', result=result)


if __name__ == "__main__":
        app.run(host="hahacking.local", port=80)
