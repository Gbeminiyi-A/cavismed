from django.test import TestCase, SimpleTestCase #  type: ignore

# Create your tests here.

class TestLogin(SimpleTestCase):
    
    def test_login(self):
        user = self.client.get('/api/v1')
        self.assertEqual(user.status_code, 403)
