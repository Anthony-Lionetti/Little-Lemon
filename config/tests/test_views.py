from django.test import TestCase
from django.urls import reverse

from restaurant import models, serializers


class MenuViewTest(TestCase):
    
    def setUp(self):
        # Add a few test instances of the Menu model
        models.Menu.objects.create(name="Breakfast Menu", description="Morning meals.")
        models.Menu.objects.create(name="Lunch Menu", description="Afternoon meals.")
        models.Menu.objects.create(name="Dinner Menu", description="Evening meals.")

    def test_getall(self):
        # Use the Django test client to simulate a GET request
        response = self.client.get(reverse('menu-list'))  # Assuming 'menu-list' is the name of your URL pattern for listing all menus

        # Retrieve all the Menu objects added for test purposes
        menus =  models.Menu.objects.all()
        # Serialize the data
        serializer = serializers.MenuSerializer(menus, many=True)

        # Run assertions to check if the serialized data equals the response
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)