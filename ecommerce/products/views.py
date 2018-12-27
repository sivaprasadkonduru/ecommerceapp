from django.shortcuts import render
from django.http import HttpResponse
from .models import Stores
# Create your views here.

def add_store_details(request):

    with open(r'C:\Users\User\workspace\stores.txt') as std:
        store_data = std.readlines()
        for sd in store_data[1:]:
            data = sd.split(',')
            data = [i.strip(r'\n') for i in data]
            std_data = Stores.objects.get_or_create(name=data[0], address=data[1], \
                                                    contact_no=data[2], landmark=data[3], \
                                                    email=data[4], location=data[5])

        return HttpResponse("Added store details")


def get_store_details(request):

    data = Stores.objects.all()
    return render(request, 'store_details.html', {'store_data': data})



