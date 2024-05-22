from django.urls import path

from . import views 

app_name = 'polls'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:q_id>/vote/', views.vote, name='vote'),
    path('<int:q_id>/results/', views.results, name='results'),
]