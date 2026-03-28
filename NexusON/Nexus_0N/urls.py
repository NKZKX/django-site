from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('envia_email/', views.get_email, name='envia_email'),

]