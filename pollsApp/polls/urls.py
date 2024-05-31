from django.urls import path

from . import views 

app_name = 'polls'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:q_id>/vote/', views.vote, name='vote'),
    path('<int:q_id>/results/', views.results, name='results'),
    path('results/<int:q_id>/chart/', views.results_chart, name='results_chart'),
]