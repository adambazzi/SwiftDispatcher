from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Department(db.Model):
    """
    Department model representing departments in the application.
    """
    __tablename__ = 'departments'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    specialization = db.Column(db.String(100), nullable=False)


    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # Define Relationships
    # Define a one-to-many relationship with Doctors
    doctors = db.relationship('Doctor', back_populates='department')
