from django.urls import path

from .views import (
    ClarificationCreateView,
    ClarificationDeleteView,
    ClarificationListView,
    ClarificationRetrieveView,
    ClarificationUpdateView,
)

app_name = "clarifications"

urlpatterns = [
    path("", ClarificationListView.as_view(), name="list"),
    path("create", ClarificationCreateView.as_view(), name="create"),
    path("<str:pk>", ClarificationRetrieveView.as_view(), name="retrieve"),
    path("<str:pk>", ClarificationUpdateView.as_view(), name="update"),
    path("<str:pk>", ClarificationDeleteView.as_view(), name="delete"),
]
