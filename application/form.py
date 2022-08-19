from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class UserInputForm(FlaskForm):
    item = StringField('Item', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    unit = SelectField('Unit', validators=[DataRequired()],
                            choices=[('kg', 'kg'),
                                    ('m³', 'm³'),
                                    ('m²', 'm²')
                        ])
    rate = IntegerField('Rate(per unit BDT)',validators=[DataRequired()])

    submit = SubmitField('Generate Report')

