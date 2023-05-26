from flask import Blueprint, request, jsonify
from sqlalchemy.orm import joinedload
from app.models import Job
from app import db
from sqlalchemy.exc import IntegrityError


job_routes = Blueprint('jobs', __name__)

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

@job_routes.route('/job', methods=['POST'])
def create_job():
    data = request.get_json()

    new_job = Job(
        project_manager_id=data.get('project_manager_id'),
        client_id=data.get('client_id'),
        job_number=data.get('job_number'),
        project_info=data.get('project_info'),
        address=data.get('address'),
        city=data.get('city'),
        state=data.get('state'),
        zip_code=data.get('zip_code'),
        lat=data.get('lat'),
        lng=data.get('lng'),
        start_date=data.get('start_date'),
        end_date=data.get('end_date'),
        job_status=data.get('job_status', 'Pending'),
        contact_name=data.get('contact_name'),
        contact_number=data.get('contact_number'),
        project_manager_name=data.get('project_manager_name')
    )

    db.session.add(new_job)
    try:
        db.session.commit()
        return jsonify({'message': 'Job created successfully', 'job_id': new_job.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Job creation failed'}), 400
