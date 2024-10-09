from django.urls import path
from . import views
urlpatterns = [
     # path to predict urls
    path('api/predict', views.predict, name  = 'predict'),
]
