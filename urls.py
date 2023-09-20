
from django.urls import path
from app_praia import views

urlpatterns = [
# rota, view respossável, nome de refererência
# lojadepraia.com
path('',views.home,name='home'),
]
