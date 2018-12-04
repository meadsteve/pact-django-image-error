from django.conf.urls import url

from .views import PutImageView

urlpatterns = [
    url(r'^$', PutImageView.as_view(), name='index'),
]