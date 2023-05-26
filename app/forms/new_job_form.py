from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, Optional

class NewJobForm(FlaskForm):
    project_manager_id = IntegerField('project_manager_id', validators=[DataRequired()])
    client_id = IntegerField('client_id', validators=[DataRequired()])
    job_number = StringField('job_number', validators=[DataRequired(), Length(max=20)])
    project_info = StringField('project_info', validators=[DataRequired(), Length(max=500)])
    address = StringField('address', validators=[DataRequired(), Length(max=255)])
    city = StringField('city', validators=[DataRequired(), Length(max=100)])
    state = StringField('state', validators=[DataRequired(), Length(max=100)])
    zip_code = StringField('zip_code', validators=[DataRequired(), Length(max=10)])
    lat = StringField('lat', validators=[Optional()])
    lng = StringField('lng', validators=[Optional()])
    start_date = DateField('start_date', format='%Y-%m-%d', validators=[DataRequired()])
    end_date = DateField('end_date', format='%Y-%m-%d', validators=[DataRequired()])
    job_status = StringField('job_status', validators=[DataRequired(), Length(max=20)])
    contact_name = StringField('contact_name', validators=[DataRequired(), Length(max=255)])
    contact_number = StringField('contact_number', validators=[DataRequired(), Length(max=255)])
    project_manager_name = StringField('project_manager_name', validators=[DataRequired(), Length(max=255)])
