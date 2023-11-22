from django.shortcuts import render
from django.db.models import Q
from .models import turmas,escola
from .serializer import TurmaSerializer,VotacaoSerializer,EscolaSerializer

# Create your views here.
from rest_framework.generics import CreateAPIView, GenericAPIView,ListAPIView,UpdateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

class PaginateionTrumas(PageNumberPagination):
    page_size =34
    page_query_param = 'page_size'
    max_page_size = 100

class turmaLista(GenericAPIView):
    throttle_classes = [AnonRateThrottle]
    queryset = turmas.objects.all().order_by('-votos')
    serializer_class = TurmaSerializer
    pagination_class = PaginateionTrumas

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

   
    

class turmaCriar(CreateAPIView):
    queryset = turmas.objects.all()
    serializer_class = TurmaSerializer
    permission_classes = [IsAdminUser]
    


class turmadetelhes(RetrieveUpdateDestroyAPIView):
    queryset = turmas.objects.all()
    serializer_class = TurmaSerializer
    permission_classes = [IsAdminUser]



class Votacao(UpdateAPIView):
    serializer_class = VotacaoSerializer

    def get_queryset(self):
        qs =turmas.objects.filter(id=self.kwargs['pk'])
        return qs
    

    def partial_update(self, request, *args, **kwargs):
        id = kwargs['pk']
        turma = self.get_queryset().first()

        turma.votos += 1

        turma.save()

        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)



class escolaLista(ListAPIView):
    queryset = escola.objects.all()
    serializer_class = EscolaSerializer
    pagination_class = PaginateionTrumas

    def get_queryset(self):
        return super().get_queryset()