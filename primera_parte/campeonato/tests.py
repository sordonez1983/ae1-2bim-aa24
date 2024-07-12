from django.urls import reverse

class MyTest(TestCase):

    def test_home_page_status_code(self):
        """Test that the home page returns a status code of 200 (OK)"""
        url = reverse('home')  # Replace 'home' with your actual URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)