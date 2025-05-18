   from flask import Blueprint, request, jsonify
   from .utils import send_notification, get_user_notifications

   api = Blueprint('api', __name__)

   @api.route('/notifications', methods=['POST'])
   def create_notification():
       data = request.json
       notification_type = data.get('type')
       user_id = data.get('user_id')
       message = data.get('message')
       success = send_notification(notification_type, user_id, message)
       return jsonify({'success': success}), 201

   @api.route('/users/<int:user_id>/notifications', methods=['GET'])
   def user_notifications(user_id):
       notifications = get_user_notifications(user_id)
       return jsonify(notifications), 200
   