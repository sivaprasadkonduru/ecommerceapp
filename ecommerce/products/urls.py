from django.conf.urls import url
from products.views import add_store_details, get_store_details

urlpatterns = [
    url(r'store_details/', add_store_details),
    url(r'get_details/', get_store_details)
]