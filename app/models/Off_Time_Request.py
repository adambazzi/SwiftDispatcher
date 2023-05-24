from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Off_Time_Request(db.Model):
    """
    Off_Time_Request model representing appointments in the application.
    """
    __tablename__ = 'off_time_requests'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('patients.id'), ondelete='CASCADE'), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # Define Relationships
    # Define a many-to-one relationship with Patients
    user = db.relationship('Off_Time_Request', back_populates='user', cascade="delete")
