from django.urls import path
from . import views


urlpatterns = [
    path('',views.ChartView.as_view(), name='chart'),
    path('api/data/',views.ChartDataAPIView.as_view(),name='chart-data'),
]