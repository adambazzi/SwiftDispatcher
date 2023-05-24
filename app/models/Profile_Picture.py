from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Profile_Picture(db.Model):
    """
    Profile Picture model representing patients in the application.
    """
    __tablename__ = 'profile_pictures'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id'), ondelete='CASCADE'), nullable=False)

    address = db.Column(db.String, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # Define Relationships
    # Define a one-to-one relationship with Users
    user = db.relationship('User', uselist=False, back_populates='profile_picture', cascade="delete")
