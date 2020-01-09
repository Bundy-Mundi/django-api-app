from django.urls import path
from .views import ListRoomView, SeeRoomView

app_name = "core"

urlpatterns = [
  path("", ListRoomView.as_view()),
  path("<int:pk>/", SeeRoomView.as_view())
]