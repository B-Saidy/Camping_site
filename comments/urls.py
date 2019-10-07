from django.urls import path, include
from . import views
urlpatterns = [
    path('<int:camp_id>/', views.new_comment, name='new_comment'),
    path('edit/', views.edit_comment, name='edit_comment'),
]