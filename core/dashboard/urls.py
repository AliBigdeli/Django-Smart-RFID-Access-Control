from django.urls import path, include
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("card-management/", views.CardIDManagement.as_view(), name="card-management"),
    path("reader-management/", views.CardReaderManagement.as_view(), name="reader-management"),
    path("reader/logs/", views.CardReaderLogs.as_view(), name="reader-logs"),
    path("api/", include("dashboard.api.urls"))
]
