from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, InputRequired, Length, ValidationError
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    author = StringField("Author")
    submit = SubmitField("Submit Post")

## Register Form
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Submit")

## Login Form
class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired()], render_kw={"placeholder":"Email"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder":"Password"})
    submit = SubmitField("Login")

## Comment Form
class CommentForm(FlaskForm):
    comment_ = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit")
