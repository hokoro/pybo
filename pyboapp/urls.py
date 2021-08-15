from django.urls import path

from pyboapp import views

app_name = 'pyboapp'
urlpatterns = [
    path('',views.index)
]