from django.urls import path
from app4.views import virat
app_name='nothing'
urlpatterns=[
    path('virat/',virat,name='virat')
]