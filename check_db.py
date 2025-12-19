import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'house_price_project_final.settings')
django.setup()

from houses.models import House, HouseImage, CATEGORIES

print('Available categories in model:', CATEGORIES)
print('\nHouses in database:')
for h in House.objects.all():
    print(f'  - {h.title}')
    print(f'    Images for this house:')
    for img in h.images.all():
        print(f'      Category: {img.category}, Image path: {img.image}')
