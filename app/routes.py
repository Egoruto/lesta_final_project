from flask import Blueprint, request, jsonify
from app.models import db, Result

bp = Blueprint('main', __name__)


@bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "ok"})


@bp.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    score = data.get('score')

    if not name or not score:
        return jsonify({"error": "Missing name or score"}), 400

    result = Result(name=name, score=score)
    db.session.add(result)
    db.session.commit()

    return jsonify({"message": "Data saved successfully"}), 201


@bp.route('/results', methods=['GET'])
def results():
    all_results = Result.query.all()
    output = []
    for r in all_results:
        output.append({
            "id": r.id,
            "name": r.name,
            "score": r.score,
            "timestamp": r.timestamp.isoformat()
        })
    return jsonify(output)
