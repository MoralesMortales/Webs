from django.test import SimpleTestCase
from django.urls import reverse

""" FIXME: """

class IndexTest(SimpleTestCase):
    
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
    def test_url_available_by_name(self):
        response = self.client.get(reverse("Index"))
        self.assertEqual(response.status_code, 200)
        
    def test_template_name_correct(self): # new
        response = self.client.get(reverse("Index"))
        self.assertTemplateUsed(response, "Index.html")
        
    def test_template_content(self): # new
        response = self.client.get(reverse("Index"))
        self.assertContains(response, "<h1>Welcome pal</h1>")
        
class InfoTests(SimpleTestCase):
    
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/Info/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("Info"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self): # new
        response = self.client.get(reverse("Info"))
        self.assertTemplateUsed(response, "Information.html")
        
    def test_template_content(self): # new
        response = self.client.get(reverse("Info"))
        self.assertContains(response, "<h3>Bienvenido a info</h3>")