from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Document_Category(db.Model):
    """
    Document_Category model representing Document Categories in the application.
    """
    __tablename__ = 'document_categories'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    default_option = db.Column(db.Boolean, nullable=False)
    name = db.Column(db.String, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # Define Relationships
    # Define a one-to-many relationship with Documents
    job_document = db.relationship('Job_Document', back_populates='document_category', cascade="delete")
