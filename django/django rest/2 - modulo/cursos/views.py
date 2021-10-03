from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from django.shortcuts import render
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

"""
API V1
"""

# serve par alistar um ou varios registros do banco e inserir um registro no banco
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


# serve pra atualizar ou deletar um registro do banco
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


# serve par alistar um ou varios registros do banco e inserir um registro no banco
class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    # caso seja passado um curso como parametro na url retorna o curso
    def get_queryset(self):
        # o parametro deve ser o mesmo que foi passado na url
        if self.kwargs.get("curso_pk"):
            return self.queryset.filter(curso_id=self.kwargs.get("curso_pk"))
        # retorna todos os cursos
        return self.queryset.all()


# serve para manipular um registro do banco
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get("curso_pk"):
            # caso esteja sendo passado uma ide de curso como parametro cai nessa condição
            # e retorna as avaliuações do curso que foi passado como parametro
            return get_object_or_404(
                self.get_queryset(),
                curso_id=self.kwargs.get("curso_pk"),
                pk=self.kwargs.get("avaliacao_pk"),
            )
        # retorna todas as avaliações
        return get_object_or_404(
            self.get_queryset(), pk=self.kwargs.get("avaliacao_pk")
        )


"""
API V2
"""


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=["get"])
    def avaliacoes(self, request, pk=None):
        self.pagination_class.page_size = 2
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)


"""
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
"""


class AvaliacaoViewSet(
    #mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

def index(request):
    return render(request, "dist/index.html")