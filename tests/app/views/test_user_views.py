from django.test import TestCase, RequestFactory

from app.views.user_views import UserViews


class TestUserView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_all_students_view(self):
        request = self.factory.get('/get_all_students')

        response = UserViews.get_all_students(request)

        assert response.status_code == 200
