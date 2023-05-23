from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Medical_Record(db.Model):
    """
    Medical_Record model representing appointments in the application.
    """
    __tablename__ = 'medical_records'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('patients.id'), ondelete='CASCADE'), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # Define Relationships
    # Define a many-to-one relationship with Patients
    patient = db.relationship('Patient', back_populates='medical_records', cascade="delete")
