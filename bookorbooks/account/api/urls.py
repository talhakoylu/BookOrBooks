from django.urls import path
from account.api.views import CreateUserAPIView, ChildListAPIView, ChildListCreateAPIView

app_name = "account"

urlpatterns = [
    path("register", CreateUserAPIView.as_view(), name="register"),
    path("child-list", ChildListAPIView.as_view(), name="child_list"),
    path("add-child-record", ChildListCreateAPIView.as_view(), name="child_list_create"),
]
