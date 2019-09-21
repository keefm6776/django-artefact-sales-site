from django.conf.urls import url, include
from .views import all_artefacts

urlpatterns = [
    url(r'^$', all_artefacts, name='artefacts'),
]