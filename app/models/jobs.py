from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Job(db.Model):
    """
    Job model representing jobs in the application.
    """
    __tablename__ = 'jobs'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    project_manager_id = db.Column(db.String(100), nullable=False)
    client_id = db.Column(db.String(100), nullable=False)
    job_number = db.Column(db.String(100), nullable=False)
    project_info = db.Column(db.Text, nullable=True)
    address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.String(20), nullable=False)
    lat = db.Column(db.Float, nullable=True)
    lng = db.Column(db.Float, nullable=True)
    start_date = db.Column(db.DateTime, nullable=True)
    end_date = db.Column(db.DateTime, nullable=True)
    job_status = db.Column(db.String(50), default='pending')
    contact_name = db.Column(db.String(200), nullable=True)
    contact_number = db.Column(db.String(20), nullable=True)
    project_manager_name = db.Column(db.String(200), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # Define Relationships
