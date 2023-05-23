from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Appointment(db.Model):
    """
    Appointment model representing appointments in the application.
    """
    __tablename__ = 'appointments'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('doctors.id'), ondelete='CASCADE'), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('patients.id'), ondelete='CASCADE'), nullable=False)

    datetime = db.Column(db.DateTime, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # Define Relationships
    # Define a many-to-one relationship with Doctors
    doctor = db.relationship('Doctor', back_populates='appointments', cascade="delete")
    # Define a many-to-one relationship with Patients
    patient = db.relationship('Patient', back_populates='appointments', cascade="delete")
