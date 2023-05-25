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
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id'), ondelete='CASCADE'), nullable=False)

    # Define additional fields
    employee_confirm_status = db.Column(db.Boolean, default=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    employee_confirm_status = db.Column(db.String, default='Pending')

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # Define Relationships
    # Define a many-to-one relationship with Users
    user = db.relationship('User', back_populates='off_time_requests')
