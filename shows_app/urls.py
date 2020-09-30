from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.new_show),
    path('shows/create', views.add_show),
    path('shows/<int:show_id>/edit', views.edit_show),
    path('shows/<int:show_id>/update', views.edit_show_now),
    path('shows/<int:show_id>', views.view_show),
    path('shows/<int:show_id>/destroy', views.delete)
]