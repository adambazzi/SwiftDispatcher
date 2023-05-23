from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Patient(db.Model):
    """
    Patient model representing patients in the application.
    """
    __tablename__ = 'patients'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id'), ondelete='CASCADE'), nullable=False)

    specialization = db.Column(db.String(100), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    is_smoker = db.Column(db.Boolean, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    race = db.Column(db.String(100), nullable=False)
    insurance_name = db.Column(db.String(100), nullable=False)
    policy_number = db.Column(db.String(100), nullable=False)
    group_number = db.Column(db.String(100), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # Define Relationships
    # Define a one-to-one relationship with Users
    user = db.relationship('User', uselist=False, back_populates='patient', cascade="delete")
    # Define one-to-many relationship with appointments table
    appointments = db.relationship('Appointment', back_populates='patient')
    # Define one-to-many relationship with medical_record table
    medical_records = db.relationship('Medical_Record', back_populates='patient', cascade="delete")
