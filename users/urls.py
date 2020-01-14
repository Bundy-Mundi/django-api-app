from django.urls import path
from core.views import ListUserView, SeeUserView

app_name = "users"

urlpatterns = [
  path("", ListUserView.as_view()),
  path("<int:pk>/", SeeUserView.as_view())
]
