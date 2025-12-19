from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import House, HouseImage, CATEGORIES
from collections import defaultdict

def house_list(request):
    houses = House.objects.all()
    all_grouped = []

    for house in houses:
        images = house.images.all()
        grouped = defaultdict(list)
        for img in images:
            # Build full URL manually since image is a CharField
            grouped[img.category].append(settings.MEDIA_URL + img.image)

        hero_image = grouped['Exterior'][0] if grouped['Exterior'] else '/static/placeholder.jpg'

        all_grouped.append({
            'house': house,
            'grouped': grouped,
            'hero_image': hero_image,
            'categories': CATEGORIES
        })

    return render(request, 'houses/house_list.html', {'all_grouped': all_grouped})


def house_detail(request, house_id):
    house = get_object_or_404(House, id=house_id)
    grouped = defaultdict(list)

    for img in house.images.all():
        grouped[img.category].append(settings.MEDIA_URL + img.image)

    template_name = 'houses/listings.html' if request.GET.get('view') == 'listing' else 'houses/house_detail.html'
    
    return render(request, template_name, {
        'house': house,
        'grouped': grouped,
        'categories': CATEGORIES
    })

from django.http import HttpResponse

def contact_agent(request, house_id):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        # You can save to DB or send email here
        return HttpResponse("Message sent! We will contact you soon.")
    else:
        return HttpResponse("Invalid request method.")
