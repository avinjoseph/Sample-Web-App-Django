from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ChartView(TemplateView):
    template_name = 'chart/chart.html';

class ChartDataAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        data = {
            "labels" : ["A","B","C","D","E"],
            "values" : [10,20,30,40,50],
        }

        return Response(data)