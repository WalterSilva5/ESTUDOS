from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    CursoAPIView,
    CursosAPIView,
    AvaliacaoAPIView,
    AvaliacoesAPIView,
    CursoViewSet,
    AvaliacaoViewSet,
    index)


router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)


urlpatterns = [
    path('', index, name="index"),
    #lista os cursos
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    #recupera um curso, atualiza ou deleta
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    #lista as avaliações
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
    #recupera uma avaliação e atualiza ou deleta
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='curso_avaliacao'),

    #lista todas as avaliações
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    #lista uma avaliação
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
]

