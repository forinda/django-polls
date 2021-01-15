from django.urls import path,reverse
from . import views as poll_views

app_name = 'polls'
urlpatterns = [
    path('', poll_views.IndexView.as_view(), name='index'),
    path('<slug:pk>/', poll_views.DetailView.as_view(), name='detail'),
    path('<slug:pk>/results/', poll_views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', poll_views.vote, name='vote'),
]
