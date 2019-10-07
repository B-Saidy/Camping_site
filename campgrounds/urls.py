from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.home, name='index'),
    path('home/<int:camp_id>', views.show, name='show'),
    path('home/<int:camp_id>/delete', views.delete_comment, name='delete_comment'),
    path('home/<int:camp_id>/edit', views.edit, name='edit'),
    # path('home/<int:camp_id>/edit/update', views.update, name='update'),
    path('new', views.new, name='new'),
]
