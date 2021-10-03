from django.urls import path
#views
from app.views import index
urlpatterns = [
   path('', index, name='index'),
]
