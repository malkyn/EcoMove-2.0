# backend/models.py
from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    measurements = db.relationship('Measurement', backref='user', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at
        }


class Residue(db.Model):
    __tablename__ = 'residues'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    energy_potential_kwh = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))

    measurements = db.relationship('Measurement', backref='residue', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'energy_potential_kwh': self.energy_potential_kwh,
            'description': self.description
        }


class Measurement(db.Model):
    __tablename__ = 'measurements'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    residue_id = db.Column(db.Integer, db.ForeignKey('residues.id'), nullable=False)
    quantity_kg = db.Column(db.Float, nullable=False)
    total_energy_kwh = db.Column(db.Float)
    estimated_savings = db.Column(db.Float)
    date_recorded = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'residue_id': self.residue_id,
            'quantity_kg': self.quantity_kg,
            'total_energy_kwh': self.total_energy_kwh,
            'estimated_savings': self.estimated_savings,
            'date_recorded': self.date_recorded,
            'residue_name': self.residue.name if self.residue else None,
            'user_name': self.user.name if self.user else None
        }
