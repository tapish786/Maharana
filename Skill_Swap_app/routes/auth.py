from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    skill = data.get('skill')
    return jsonify({'message': f'{name} registered with skill: {skill}'}), 201
