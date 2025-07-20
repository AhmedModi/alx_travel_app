from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = 'Seed the database with listings'

    def handle(self, *args, **kwargs):
        user, created = User.objects.get_or_create(username='hostuser', defaults={'password': 'test123'})
        
        for i in range(5):
            Listing.objects.create(
                title=f"Cozy Apartment {i}",
                description="A nice and comfortable place to stay.",
                price_per_night=random.uniform(30, 200),
                location=f"City {i}",
                host=user
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded listings'))
