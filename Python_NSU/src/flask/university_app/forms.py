from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    DateField,
    IntegerField,
    PasswordField,
    SelectField,
    SubmitField
)
from wtforms.validators import (
    DataRequired,
    Length,
    EqualTo
)


class UniversityForm(FlaskForm):
    full_name = StringField(
        'Полное название',
        validators=[DataRequired(), Length(max=255)]
    )

    short_name = StringField(
        'Сокращенное название',
        validators=[DataRequired(), Length(max=50)]
    )

    founded_date = DateField(
        'Дата создания',
        validators=[DataRequired()]
    )

    submit = SubmitField('Сохранить')


class StudentForm(FlaskForm):
    full_name = StringField(
        'ФИО',
        validators=[DataRequired(), Length(max=255)]
    )

    birth_date = DateField(
        'Дата рождения',
        validators=[DataRequired()]
    )

    university_id = SelectField(
        'Университет',
        coerce=int,
        validators=[DataRequired()]
    )

    enrollment_year = IntegerField(
        'Год поступления',
        validators=[DataRequired()]
    )

    submit = SubmitField('Сохранить')


class RegistrationForm(FlaskForm):
    username = StringField(
        'Логин',
        validators=[DataRequired(), Length(max=80)]
    )

    password = PasswordField(
        'Пароль',
        validators=[DataRequired()]
    )

    confirm_password = PasswordField(
        'Повторите пароль',
        validators=[
            DataRequired(),
            EqualTo('password', message='Пароли не совпадают')
        ]
    )

    submit = SubmitField('Зарегистрироваться')


class LoginForm(FlaskForm):
    username = StringField(
        'Логин',
        validators=[DataRequired()]
    )

    password = PasswordField(
        'Пароль',
        validators=[DataRequired()]
    )

    submit = SubmitField('Войти')