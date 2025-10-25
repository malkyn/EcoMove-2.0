# backend/routes/dashboard.py
from flask import Blueprint, jsonify
from app import db
from models import User, Residue, Measurement
from sqlalchemy import func

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/', methods=['GET'])
def get_dashboard_data():
    # ---- 1️⃣ Totais gerais ----
    total_energy = db.session.query(func.sum(Measurement.total_energy_kwh)).scalar() or 0
    total_savings = db.session.query(func.sum(Measurement.estimated_savings)).scalar() or 0
    total_measurements = db.session.query(func.count(Measurement.id)).scalar() or 0
    total_users = db.session.query(func.count(User.id)).scalar() or 0

    # ---- 2️⃣ Ranking de usuários ----
    user_ranking = (
        db.session.query(
            User.name,
            func.sum(Measurement.total_energy_kwh).label('energy'),
            func.sum(Measurement.estimated_savings).label('savings')
        )
        .join(Measurement, Measurement.user_id == User.id)
        .group_by(User.id)
        .order_by(func.sum(Measurement.estimated_savings).desc())
        .limit(5)
        .all()
    )
    user_ranking_data = [
        {'user': u.name, 'total_energy_kwh': round(u.energy or 0, 2), 'total_savings': round(u.savings or 0, 2)}
        for u in user_ranking
    ]

    # ---- 3️⃣ Energia e economia por resíduo ----
    residue_stats = (
        db.session.query(
            Residue.name,
            func.sum(Measurement.total_energy_kwh).label('energy'),
            func.sum(Measurement.estimated_savings).label('savings')
        )
        .join(Measurement, Measurement.residue_id == Residue.id)
        .group_by(Residue.id)
        .order_by(func.sum(Measurement.total_energy_kwh).desc())
        .all()
    )
    residue_data = [
        {'residue': r.name, 'total_energy_kwh': round(r.energy or 0, 2), 'total_savings': round(r.savings or 0, 2)}
        for r in residue_stats
    ]

    # ---- 4️⃣ Retorno consolidado ----
    data = {
        'overview': {
            'total_users': total_users,
            'total_measurements': total_measurements,
            'total_energy_kwh': round(total_energy, 2),
            'total_savings_reais': round(total_savings, 2),
        },
        'ranking': user_ranking_data,
        'by_residue': residue_data
    }

    return jsonify(data)
