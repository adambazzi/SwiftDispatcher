from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime



User_X_Job = db.Table(
    'user_x_jobs',
    db.Column('user_id', db.Integer, db.ForeignKey(
        add_prefix_for_prod("users.id")), primary_key=True),
    db.Column('job_id', db.String, db.ForeignKey(
        add_prefix_for_prod("jobs.id")), primary_key=True),
    # Add a foreign key constraint with cascade delete-orphan
    db.ForeignKeyConstraint(['job_id'], [add_prefix_for_prod("jobs.id")], ondelete='CASCADE',),
    extend_existing=True
)

if environment == "production":
    User_X_Job.schema = SCHEMA
