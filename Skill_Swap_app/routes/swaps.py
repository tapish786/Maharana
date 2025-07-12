from flask import Blueprint, request, jsonify
from Models import db, SwapRequest

swaps_bp = Blueprint('swaps_bp', __name__)

# ✅ Create new swap request
@swaps_bp.route('/', methods=['POST'])
def create_swap():
    data = request.get_json()
    try:
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
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# ✅ Get all swaps
@swaps_bp.route('/', methods=['GET'])
def get_all_swaps():
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

# ✅ Update status of a swap (Accept/Reject)
@swaps_bp.route('/<int:id>', methods=['PUT'])
def update_swap(id):
    data = request.get_json()
    swap = SwapRequest.query.get(id)
    if not swap:
        return jsonify({'error': 'Swap not found'}), 404
    swap.status = data.get('status', swap.status)
    db.session.commit()
    return jsonify({'message': 'Swap status updated successfully'}), 200

# ✅ Delete a swap
@swaps_bp.route('/<int:id>', methods=['DELETE'])
def delete_swap(id):
    swap = SwapRequest.query.get(id)
    if not swap:
        return jsonify({'error': 'Swap not found'}), 404
    db.session.delete(swap)
    db.session.commit()
    return jsonify({'message': 'Swap deleted successfully'}), 200
