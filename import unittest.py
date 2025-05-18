   import unittest
   from app import app

   class NotificationServiceTestCase(unittest.TestCase):
       def setUp(self):
           self.app = app.test_client()
           self.app.testing = True

       def test_create_notification(self):
           response = self.app.post('/notifications', json={
               'type': 'email',
               'user_id': 1,
               'message': 'Test notification'
           })
           self.assertEqual(response.status_code, 201)

       def test_get_user_notifications(self):
           response = self.app.get('/users/1/notifications')
           self.assertEqual(response.status_code, 200)

   if __name__ == '__main__':
       unittest.main()
   