from django.urls import path
from meme import views
urlpatterns = [
  path('',views.index),
  path('meme/<str:Category>',views.Get_Category),


]