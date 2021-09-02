from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
    path('shows', views.index_shows, name="index_shows"),
    path('shows/new', views.newShow, name="new_show"),
    path('shows/create', views.createShow, name="create"),
    path('shows/<int:id>/delete', views.deleteShow, name="delete"),
    path('shows/<int:id>/edit', views.editShow, name="edit"),
    path('shows/<int:id>/save', views.saveShow, name="save"),
    path('shows/<int:id>', views.viewShow, name="view_show"),

]