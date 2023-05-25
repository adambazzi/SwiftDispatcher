from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.schema import CheckConstraint
from flask_login import UserMixin
from .user_x_job import user_x_jobs


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True, index=True)
    email = db.Column(db.String(255), nullable=False, unique=True, index=True)
    phone = db.Column(db.String(255), nullable=False, unique=True)
    lng = db.Column(db.Float,nullable=False)
    lat = db.Column(db.Float,nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    hashed_password = db.Column(db.String(255), nullable=False)


    # Define a one-to-one relationship with patient
    profile_picture = db.relationship('Profile_Picture', back_populates='user', uselist=False)


    # Check constraints for basic email and phone validation
    __table_args__ = (
        CheckConstraint('email ~* \'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$\'', name='email_check'),
        CheckConstraint('phone ~* \'^\+\d{1,3}\s?\d{1,14}(\s?\d{1,13})?\'', name='phone_check'),
    )

    @property
    def password(self):
        raise AttributeError("Password attribute is not readable.")

    @password.setter
    def password(self, password):
        # Password complexity check
        pattern = re.compile(
            r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        )
        if not pattern.match(password):
            raise ValueError(
                "Password must contain at least 8 characters, including an uppercase letter, "
                "lowercase letter, a digit and a special character (@$!%*?&)."
            )
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }

    # Define Relationships
    # Define a many-to-many relationship with Jobs
    jobs = db.relationship("Job",secondary=user_x_jobs, back_populates='users')
