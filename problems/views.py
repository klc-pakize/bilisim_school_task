from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import Problem
from .serializers import ProblemSerializer
# Create your views here.

class ProblemView(ModelViewSet):

    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    # Yeni bir problem oluşturmak için kullanılan fonksiyon.
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
        except ValueError as e:
            # Eğer kullanıcı sayısal olmayan bir girdi-input kullanırsa, ValueError üretir ve
            # bu hatayı yakalar. Daha sonra kullanıcıya bir hata mesajı döner.
            error_message = {"input": str(e)}
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    # Var olan bir problemi güncellemek için kullanılan fonksiyon.
    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

        except ValueError as e:
            # Eğer kullanıcı sayısal olmayan bir girdi-input kullanırsa, ValueError üretir ve
            # bu hatayı yakalar. Daha sonra kullanıcıya bir hata mesajı döner.
            error_message = {"input": str(e)}
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    # Bir problemi silmek için kullanılan fonksiyon.
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        
        # İlgili problem silindiği zaman, kullanıcıya silenen problemin silindiğine dair cevap-response döner.
        message = {
            "message":f"The problem named {instance.title} has been deleted"
        }
        return Response(message,status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()