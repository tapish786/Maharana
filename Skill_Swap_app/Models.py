from flask import Blueprint, request, jsonify
from Models import db, SwapRequest

swapes_bp = Blueprint('swapes_bp', __name__)

# ✅ Create new swap request
@swapes_bp.route('/', methods=['POST'])
def create_swap():
    data = request.get_json()
    swap = SwapRequest(
        sender_id=data['sender_id'],
        receiver_id=data['receiver_id'],
        skill_offered=data['skill_offered'],
        skill_requested=data['skill_requested'],
        message=data.get('message', '')
    )
    db.session.add(swap)
    db.session.commit()
    return jsonify({'message': 'Swap request created successfully'}), 201

# ✅ Get all swap requests
@swapes_bp.route('/', methods=['GET'])
def get_swaps():
    swaps = SwapRequest.query.all()
    return jsonify([{
        'id': s.id,
        'sender_id': s.sender_id,
        'receiver_id': s.receiver_id,
        'skill_offered': s.skill_offered,
        'skill_requested': s.skill_requested,
        'message': s.message,
        'status': s.status
    } for s in swaps]), 200

# ✅ Update swap status (Accept / Reject)
@swapes_bp.route('/<int:id>', methods=['PUT'])
def update_swap_status(id):
    data = request.get_json()
    swap = SwapRequest.query.get(id)
    if not swap:
        return jsonify({'error': 'Swap request not found'}), 404
    swap.status = data.get('status', swap.status)
    db.session.commit()
    return jsonify({'message': 'Swap request updated successfully'}), 200

# ✅ Delete a swap request
@swapes_bp.route('/<int:id>', methods=['DELETE'])
def delete_swap(id):
    swap = SwapRequest.query.get(id)
    if not swap:
        return jsonify({'error': 'Swap request not found'}), 404
    db.session.delete(swap)
    db.session.commit()
    return jsonify({'message': 'Swap request deleted'}), 200
