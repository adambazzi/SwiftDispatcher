from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Certifications(db.Model):
    """
    Certifications model representing doctors in the application.
    """
    __tablename__ = 'certifications'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)

    cert_name = db.Column(db.String(100), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # Define Relationships
