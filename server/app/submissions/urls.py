from django.urls import path

from .views import (
    SubmissionCreateView,
    SubmissionDeleteView,
    SubmissionListView,
    SubmissionRetrieveView,
    SubmissionUpdateView,
)

app_name = "submissions"

urlpatterns = [
    path("", SubmissionListView.as_view(), name="list"),
    path("create", SubmissionCreateView.as_view(), name="create"),
    path("<str:pk>", SubmissionRetrieveView.as_view(), name="retrieve"),
    path("<str:pk>", SubmissionUpdateView.as_view(), name="update"),
    path("<str:pk>", SubmissionDeleteView.as_view(), name="delete"),
]
