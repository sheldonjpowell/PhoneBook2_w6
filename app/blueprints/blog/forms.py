from cgi import print_directory
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = StringField('Body', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    submit = SubmitField('Create')
    # product = StringField('Product', validators=[DataRequired()])


class PurchaseItemForm(FlaskForm):
    submit = SubmitField('Purchase')




# class AddressForm(FlaskForm):
#     name = StringField('name', validators=[DataRequired()])
#     address = StringField('Address', validators=[DataRequired()])
#     phonenumber = StringField('Phonenumber', validators=[DataRequired()])
#     submit = SubmitField('Add Address')
