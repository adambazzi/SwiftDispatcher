from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


Job_X_Job_Type = db.Table(
    'job_x_job_types',
    db.Column('job_id', db.Integer, db.ForeignKey(
        add_prefix_for_prod("jobs.id")), primary_key=True),
    db.Column('job_type_id', db.Integer, db.ForeignKey(
        add_prefix_for_prod("job_types.id")), primary_key=True),
    # Add a foreign key constraint with cascade delete-orphan
    db.ForeignKeyConstraint(['job_id'], [add_prefix_for_prod("jobs.id")], ondelete='CASCADE',),
    extend_existing=True
)


if environment == "production":
    Job_X_Job_Type.schema = SCHEMA
