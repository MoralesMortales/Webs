from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here. everyhting that appears here is ausefull to check if everything is working properly

class HomePage(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
    def test_url_available_by_name(self): # new
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self): # new
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")
        
    def test_template_content(self): # new
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h4>Historia</h4>")

class AboutPage(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self): # new
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        
    def test_template_name_correct(self): # new
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")
        
    def test_template_content(self): # new
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h3>LPMD C.A</h3>")
        

class ContactPage(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)
        
    def test_url_available_by_name(self): # new
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        
    def test_template_name_correct(self): # new
        response = self.client.get(reverse("contact"))
        self.assertTemplateUsed(response, "contact.html")
        
    def test_template_content(self): # new
        response = self.client.get(reverse("contact"))
        self.assertContains(response, "<h5>hola</h5>")
