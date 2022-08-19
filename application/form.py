from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class UserInputForm(FlaskForm):
    item = StringField('Item', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    unit = SelectField('Unit', validators=[DataRequired()],
                            choices=[('kg', 'kg'),
                                    ('m^3', 'm^3'),
                                    ('m^2', 'm^2')
                        ])
    rate = IntegerField('Rate',validators=[DataRequired()])

    submit = SubmitField('Generate Report')

