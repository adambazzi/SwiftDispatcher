from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime



business_categories = db.Table(
    'user_x_jobs',
    db.Model.metadata,
    db.Column('users', db.Integer, db.ForeignKey(add_prefix_for_prod('users.id'))),
    db.Column('jobs', db.Integer, db.ForeignKey(add_prefix_for_prod('jobs.id'))),
    db.Column('employee_confirm_status', db.String, default='pending'),
    db.Column('start_date', db.DateTime),
    db.Column('end_date', db.DateTime)
)
if environment == "production":
    business_categories.schema = SCHEMA
