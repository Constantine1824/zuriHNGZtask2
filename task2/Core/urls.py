from django.urls import path, re_path
from .views import CRUDApiView

urlpatterns = [
    re_path(r'(/)?(?P<id>\d+)?(?P<name>\w+)?$', CRUDApiView.as_view(), name='main'),
]