from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('top_page/', views.top_page, name='top_page'),
]