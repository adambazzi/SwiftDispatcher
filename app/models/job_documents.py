from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Job_Document(db.Model):
    """
    Job_Document model representing Job Documents in the application.
    """
    __tablename__ = 'job_documents'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('jobs.id')), nullable=False)

    category = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # Define Relationships
    # Define a many-to-one relationship with Jobs
    job = db.relationship('Job', backref='job_documents')
    # Define a one-to-one relationship with document categories
    document_category = db.relationship('Document_Category', uselist=False, back_populates='job_document', cascade="delete")
