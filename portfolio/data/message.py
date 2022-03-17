from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class MessageForm(FlaskForm):
    username = StringField("Логин", validators=[DataRequired()])
    email = EmailField("Электронная почта", validators=[DataRequired()])
    password = EmailField("Электронная почта", validators=[DataRequired()])
    message = TextAreaField("Сообщение")
    submit = SubmitField("Отправить")
