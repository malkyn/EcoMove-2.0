# backend/routes/residues.py
from flask import Blueprint, request, jsonify
from app import db
from models import Residue

residues_bp = Blueprint('residues', __name__)

@residues_bp.route('/', methods=['GET'])
def get_residues():
    residues = Residue.query.all()
    return jsonify([r.to_dict() for r in residues])

@residues_bp.route('/', methods=['POST'])
def add_residue():
    data = request.get_json()
    residue = Residue(
        name=data['name'],
        energy_potential_kwh=data['energy_potential_kwh'],
        description=data.get('description')
    )
    db.session.add(residue)
    db.session.commit()
    return jsonify(residue.to_dict()), 201

@residues_bp.route('/<int:id>', methods=['PUT'])
def update_residue(id):
    residue = Residue.query.get(id)
    if not residue:
        return jsonify({'error': 'Residue not found'}), 404
    data = request.get_json()
    residue.name = data.get('name', residue.name)
    residue.energy_potential_kwh = data.get('energy_potential_kwh', residue.energy_potential_kwh)
    residue.description = data.get('description', residue.description)
    db.session.commit()
    return jsonify(residue.to_dict())

@residues_bp.route('/<int:id>', methods=['DELETE'])
def delete_residue(id):
    residue = Residue.query.get(id)
    if not residue:
        return jsonify({'error': 'Residue not found'}), 404
    db.session.delete(residue)
    db.session.commit()
    return jsonify({'message': 'Residue deleted successfully'})
