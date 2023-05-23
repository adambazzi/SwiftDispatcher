from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Doctor(db.Model):
    """
    Doctor model representing doctors in the application.
    """
    __tablename__ = 'doctors'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id'), ondelete='CASCADE'), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('departments.id'), ondelete='SET NULL'), nullable=False)

    specialization = db.Column(db.String(100), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # Define Relationships
    # Define Many-to-One relationship with departments table
    department = db.relationship('Department', back_populates='doctors')
    # Define a one-to-one relationship with Users
    user = db.relationship('User', uselist=False, back_populates='doctor', cascade="delete")
    # Define one-to-many relationship with appointments table
    appointments = db.relationship('Appointment', back_populates='doctor')
