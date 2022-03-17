import ssl

from flask import Flask, render_template, request, redirect
from portfolio.data.message import MessageForm
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
app.config["SECRET_KEY"] = "elmir"
host = "smtp.gmail.com"
toAddr = "ahmadullinta@gmail.com"


@app.route("/", methods=["GET", "POST"])
def index():
    form = MessageForm()
    if request.method == "GET":
        return render_template("index.html", form=form)
    elif request.method == "POST":
        if form.validate_on_submit():
            send_message("/index", form.email, form.password, form.username, form.message)  # DO!!!!
        return render_template("index.html", form=form)


@app.route("/my_achievements", methods=["GET", "POST"])
def achievements():
    form = MessageForm()
    if request.method == "GET":
        return render_template("my_achievements.html", form=form)
    elif request.method == "POST":
        if form.validate_on_submit():
            send_message("/my_achievements", form.email, form.password, form.username, form.message)  # DO!!!!
    return render_template("my_achievements.html")


@app.route("/my_projects")
def projects():
    form = MessageForm()
    if request.method == "GET":
        return render_template("my_projects.html", form=form)
    elif request.method == "POST":
        if form.validate_on_submit():
            send_message("/my_projects", form.email, form.password, form.username, form.message)  # DO!!!!
        return render_template("my_projects.html")


def send_message(cur_segment, fromAddr, password, username, message_content):  # DO!!!!
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    server = smtplib.SMTP_SSL("smtp.gmail.com", 587)
    server.starttls(context=context)
    server.login("ahmadullinarus@gmail.com", "Rjk,fcf12")
    server.sendmail("ahmadullinarus@gmail.com", "ahmadullinta@gmail.com", "Hello")
    server.quit()
    msg = MIMEMultipart()
    msg['From'] = fromAddr
    msg["To"] = toAddr
    msg["Subject"] = f"Отзыв профиля от {username}"
    msg.attach(MIMEText(message_content, 'plain'))
    text = msg.as_string()
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(fromAddr, password)
    server.sendmail(fromAddr, toAddr, text)
    server.quit()
    return redirect(cur_segment)


if __name__ == "__main__":
    app.run()