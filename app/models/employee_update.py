from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Employee_Update(db.Model):
    """
    Employee_Update model representing Employee Updates in the application.
    """
    __tablename__ = 'employee_updates'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('jobs.id')), nullable=False)
    update_response = db.Column(db.String(200), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # Define Relationships
    # Define a many-to-one relationship with Jobs
    job = db.relationship('Job', back_populates='employee_updates')
