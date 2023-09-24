from django.urls import path

from .views import (
    SubmissionListView,
    SubmissionCreateView,
    SubmissionRetrieveUpdateDestroyView,
)

app_name = "submissions"

urlpatterns = [
    path("", SubmissionListView.as_view(), name="list"),
    path("create", SubmissionCreateView.as_view(), name="create"),
    path("<str:pk>", SubmissionRetrieveUpdateDestroyView.as_view(), name="retrieve_update_destroy"),
]
