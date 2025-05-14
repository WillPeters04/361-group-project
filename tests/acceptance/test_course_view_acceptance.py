from django.test import TestCase, Client
from webapp.models import User
from webapp.models import Course

class CourseViewAcceptanceTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="courseuser", password="testpass123")

    def test_course_view_requires_login(self):
        response = self.client.get("/courses/")
        self.assertEqual(response.status_code, 302)

    def test_course_view_loads_for_logged_in_user(self):
        self.client.login(username="courseuser", password="testpass123")
        response = self.client.get("/courses/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "standard_pages/list_courses.html")

