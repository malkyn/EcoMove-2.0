# backend/routes/measurements.py
from flask import Blueprint, request, jsonify
from app import db
from models import Measurement, User, Residue

measurements_bp = Blueprint('measurements', __name__)

@measurements_bp.route('/', methods=['GET'])
def get_measurements():
    measurements = Measurement.query.all()
    return jsonify([m.to_dict() for m in measurements])

@measurements_bp.route('/<int:id>', methods=['GET'])
def get_measurement(id):
    m = Measurement.query.get(id)
    if not m:
        return jsonify({'error': 'Measurement not found'}), 404
    return jsonify(m.to_dict())

@measurements_bp.route('/', methods=['POST'])
def add_measurement():
    data = request.get_json()
    user = User.query.get(data['user_id'])
    residue = Residue.query.get(data['residue_id'])
    if not user or not residue:
        return jsonify({'error': 'Invalid user_id or residue_id'}), 400

    quantity = float(data['quantity_kg'])
    total_energy = quantity * residue.energy_potential_kwh
    price_per_kwh = float(data.get('price_per_kwh', 0.95))  # exemplo: R$0,95/kWh
    estimated_savings = total_energy * price_per_kwh

    new_m = Measurement(
        user_id=user.id,
        residue_id=residue.id,
        quantity_kg=quantity,
        total_energy_kwh=total_energy,
        estimated_savings=estimated_savings
    )
    db.session.add(new_m)
    db.session.commit()
    return jsonify(new_m.to_dict()), 201

@measurements_bp.route('/<int:id>', methods=['PUT'])
def update_measurement(id):
    m = Measurement.query.get(id)
    if not m:
        return jsonify({'error': 'Measurement not found'}), 404

    data = request.get_json()
    if 'quantity_kg' in data:
        m.quantity_kg = float(data['quantity_kg'])
        m.total_energy_kwh = m.quantity_kg * m.residue.energy_potential_kwh
        m.estimated_savings = m.total_energy_kwh * float(data.get('price_per_kwh', 0.95))

    db.session.commit()
    return jsonify(m.to_dict())

@measurements_bp.route('/<int:id>', methods=['DELETE'])
def delete_measurement(id):
    m = Measurement.query.get(id)
    if not m:
        return jsonify({'error': 'Measurement not found'}), 404
    db.session.delete(m)
    db.session.commit()
    return jsonify({'message': 'Measurement deleted successfully'})
