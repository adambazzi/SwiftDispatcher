from flask import Blueprint, request, jsonify
from sqlalchemy.orm import joinedload
from app.models import Job
from app import db
from sqlalchemy.exc import IntegrityError
from app.forms import NewJobForm
import re

def camel_to_snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


job_routes = Blueprint('jobs', __name__)

# GET route to retrieve all jobs and clients
@job_routes.route('/job-client', methods=['GET'])
def get_job_client_info():
    # Use joinedload() to perform an eager load of Job and Client
    result = db.session.query(Job).options(joinedload(Job.client)).all()

    # Convert query result to list of dictionaries to make it serializable
    data = []
    for job in result:
        job_data = {
            'job_id': job.id,
            'project_manager_id': job.project_manager_id,
            'client_id': job.client_id,
            'job_number': job.job_number,
            'project_info': job.project_info,
            'address': job.address,
            'city': job.city,
            'state': job.state,
            'zip_code': job.zip_code,
            'lat': job.lat,
            'lng': job.lng,
            'start_date': job.start_date,
            'end_date': job.end_date,
            'job_status': job.job_status,
            'contact_name': job.contact_name,
            'contact_number': job.contact_number,
            'project_manager_name': job.project_manager_name,
            'client_name': job.client.name,
            'client_address': job.client.address,
            'client_city': job.client.city,
            'client_state': job.client.state,
            'client_zip_code': job.client.zip_code,
            'client_lat': job.client.lat,
            'client_lng': job.client.lng,
        }
        data.append(job_data)

    return jsonify(data), 200

# POST route to create a new job
@job_routes.route('/job', methods=['POST'])
def create_job():
    data = request.get_json()

    snake_case_data = {camel_to_snake(k): v for k, v in data.items()}

    form = new_job_form(data=snake_case_data)

    if form.validate():
        new_job = Job(**form.data)

        db.session.add(new_job)
        try:
            db.session.commit()
            return jsonify({'message': 'Job created successfully', 'job_id': new_job.id}), 201
        except IntegrityError:
            db.session.rollback()
            return jsonify({'message': 'Job creation failed'}), 400

    else:
        return jsonify(form.errors), 400
