from django.conf.urls import url
from .views import *

# from django.views.static.
app_name='app_cursos'
urlpatterns = [
    url(r'^$', Curso.as_view(), name='p_inicio'),
]
