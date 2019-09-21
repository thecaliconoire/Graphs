from django.shortcuts import render
from .models import People
from django.views.generic import TemplateView
from django .shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import PeopleSerializer

# Create your views here.

class ChartData(APIView):

    def get(self, request):
        name = People.objects.all()
        serialized = PeopleSerializer(name, many=True)

                        
        return Response(serialized.data)

def people_network(request):
    return render (request, "chartly/Hchart.html", {})

    
