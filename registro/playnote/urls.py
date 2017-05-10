from django.conf.urls import url
from .views import pagina_principal_view
#array es lista en python
urlpatterns =  [url(r'^$', pagina_principal_view)]