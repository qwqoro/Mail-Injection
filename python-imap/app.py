from flask import Flask
from flask import render_template, request, redirect, url_for, session
from imaplib import IMAP4
from os import urandom

app = Flask(__name__, static_url_path='', static_folder="public", template_folder="public")
app.config['SECRET_KEY'] = urandom(12)

s = IMAP4("hahacking.local")

def checkAlive(e):
  global s
  
  if "Broken pipe" in e or "EOF" in e:
    s = IMAP4("hahacking.local")

@app.route('/')
def index():
  global s

  try:
    s.noop()
  except Exception as e:
    e = str(e)
    checkAlive(e)
    return render_template("index.html", result=f"Failed! Error message: {e}")
    
  if "success" in session and session["success"]:
  
    try: 
      s.select()
      typ, data = s.search(None, "ALL")
      messages = {}
      for num in data[0].split():
        typ, data = s.fetch(num, '(RFC822)')
        messages[num.decode()] = data[0][1].decode()
      return render_template("messages.html", messages=messages)
      
    except Exception as e:
      e = str(e)
      checkAlive(e)
      return render_template("index.html", result=f"Failed! Error message: {e}")
    
  return render_template("index.html", result='')


@app.route("/signin", methods=["GET", "POST"])
def signinPost():
  global s
  
  if request.method == "POST":
    username = request.form.get("username")
    password = request.form.get("password")
    
    try:
      s.login(username, password)
      session["success"] = True
      
    except Exception as e:
      e = str(e)
      checkAlive(e)
      return render_template("index.html", result=f"Failed! Error message: {e}")
      
    return redirect(url_for('index'), 302)

@app.route("/logout", methods=["GET", "POST"])
def logoutPost():
  global s
  
  try:
    s.logout()
    session["success"] = False
      
  except Exception as e:
    e = str(e)
    return render_template("index.html", result=f"Failed! Error message: {e}")
    
  s = IMAP4("hahacking.local")
  return redirect(url_for('index'), 302)


if __name__ == "__main__":
  app.run(host="hahacking.local", port=80)
