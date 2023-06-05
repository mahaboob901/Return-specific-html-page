from django.urls import path
from app3.views import dhoni
app_name='something'
urlpatterns=[
    path('dhoni/',dhoni,name='dhoni')
]