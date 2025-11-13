from django.test import TestCase
from .models import MenuItem,Category

class MenuItemTest(TestCase):
    def test_get_item(self):

        category = Category.objects.create(
            slug="dessert",
            title="Dessert"
        )

        item = MenuItem.objects.create(title='Ice Cream',
                price=80,
                inventory=100,
                category=category,
                featured=True
            )
        itemstr = item.get_item()

        self.assertEqual(itemstr,'Ice Cream')