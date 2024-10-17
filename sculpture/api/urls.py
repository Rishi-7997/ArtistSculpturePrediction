from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
     # path to predict urls
    path('api/predict', views.predict, name  = 'predict'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]
