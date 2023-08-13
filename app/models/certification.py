from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Certifications(db.Model):
    """
    Certifications model representing certifications in the application.
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
    def to_dict(self):
        return {
            'id': self.id,
            'cert_name': self.cert_name,
        }

    # Define Relationships
    # Define a many-to-many relationship with Jobs
    users = db.relationship("User",secondary='user_x_certifications', back_populates='certifications')
