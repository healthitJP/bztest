from django.urls import path
from . import views
app_name = 'api'
urlpatterns = [
    path('get-local-time/', views.get_local_time, name="get-local-time"),
]