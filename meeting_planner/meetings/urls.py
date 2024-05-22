from django.urls import path

from .views import MeetingUpdateView, MeetingDeleteView
from . import views

urlpatterns = [
    path("<int:id>", views.detail, name="detail"),
    path("rooms", views.rooms_list, name="rooms"),
    path("new", views.new, name="new_meeting"),
    path('meeting/<int:pk>/update/', MeetingUpdateView.as_view(), name='meeting_update'),
    path('meeting/<int:pk>/delete/', MeetingDeleteView.as_view(), name='meeting_delete'),
]