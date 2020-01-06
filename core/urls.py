from django.urls import path
from .views import ListRoomView

app_name = "core"

urlpatterns = [path("list", ListRoomView.as_view())]