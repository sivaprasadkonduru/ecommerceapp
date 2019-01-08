from django.conf.urls import url
from products.views import add_store_details, get_store_details, success, \
    add_details_using_form, StoreView

urlpatterns = [
    url(r'store_details/', add_store_details, name="add_stores"),
    url(r'get_details/', get_store_details, name="store_details"),
    #url(r'add_details/', AddStoreDetailsView.as_view()),
    url(r'add_new_store/', add_details_using_form),
    url(r'success/', success, name='success'),
    url(r'store_data/', StoreView.as_view())
]