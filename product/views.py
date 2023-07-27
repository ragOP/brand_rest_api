from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.

from .models import Category
from .serializers import CategorySerializers

class CategoryViewsSet(viewsets.ViewSet):
    queryset=Category.objects.all()

    def list(self,request):
        serializer=CategorySerializers(self.queryset,many=True)
        return Response(serializer.data)
        



