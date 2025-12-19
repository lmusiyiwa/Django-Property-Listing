import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'house_price_project_final.settings')
django.setup()

from houses.models import House, HouseImage

# Get the first house
house = House.objects.first()

if house:
    print(f"Adding images to: {house.title}")
    
    # Add sample images
    images_data = [
        ('Exterior', '/static/photos/1/Exterior/IMG_9437.webp'),
        ('Exterior', '/static/photos/1/Exterior/IMG_9438.webp'),
        ('Exterior', '/static/photos/1/Exterior/IMG_9439.webp'),
        ('Exterior', '/static/photos/1/Exterior/IMG_9443.webp'),
        ('Exterior', '/static/photos/1/Exterior/IMG_9444.webp'),
        ('Exterior', '/static/photos/1/Exterior/IMG_9446.webp'),
        ('Bedrooms', '/static/photos/1/Bedroom/IMG_9445.webp'),
        ('Kitchen', '/static/photos/1/Kitchen/IMG_9448.webp'),
        ('Other', '/static/photos/1/Other/IMG_9447.webp'),
    ]
    
    for category, image_path in images_data:
        img, created = HouseImage.objects.get_or_create(
            house=house,
            category=category,
            image=image_path
        )
        if created:
            print(f"  ✓ Added {category}: {image_path}")
        else:
            print(f"  - Already exists: {category}: {image_path}")
    
    print("\nVerifying images:")
    for img in house.images.all():
        print(f"  - {img.category}: {img.image}")
else:
    print("No house found in database!")
