from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime



User_X_Certification = db.Table(
    'user_x_certifications',
    db.Column('user_id', db.Integer, db.ForeignKey(
        add_prefix_for_prod("users.id")), primary_key=True),
    db.Column('certification_id', db.String, db.ForeignKey(
        add_prefix_for_prod("certifications.id")), primary_key=True),
    # Add a foreign key constraint with cascade delete-orphan
    db.ForeignKeyConstraint(['certification_id'], [add_prefix_for_prod("certifications.id")], ondelete='CASCADE',),
    extend_existing=True
)

if environment == "production":
    User_X_Certification.schema = SCHEMA
