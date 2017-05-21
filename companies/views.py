from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer


# list all stokes or create a new one
class StockList(APIView):
    def get(self,request):
        stokes = Stock.objects.all()
        serializer =  StockSerializer(stokes,many=True)
        return Response(serializer.data)
    def __post__(self):
        pass









