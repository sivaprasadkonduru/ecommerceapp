from django.conf.urls import url
from products.rest_views import StoreViewAPI, StoreRetrieveAPI, StoreViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('store_view', StoreViewSet)

urlpatterns = [
    url(r'store_api/', StoreViewAPI.as_view()),
    url(r'store_ret/(?P<pk>\d+)/', StoreRetrieveAPI.as_view()),
]

urlpatterns += router.urls