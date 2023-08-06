from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import ValidationError


def name_validator(form, field):
    if not field.data.isalpha():
        raise ValidationError(
            f'{field.data} has non-letter characters'
        )


class CityForm(FlaskForm):
    name = StringField('name', validators=[name_validator])
