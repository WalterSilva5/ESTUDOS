from django.urls import path, include
from rest_framework import routers
from app.views import PessoaViewSet

router = routers.DefaultRouter()
router.register(r'pessoa', PessoaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
