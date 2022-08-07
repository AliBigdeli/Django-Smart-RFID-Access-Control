from django.urls import path, include
from . import views
app_name = "accounts"

urlpatterns = [
    # template base authentication
    # path('', include('django.contrib.auth.urls')),
    # api based authentication
    path("login/", views.indexView, name="authentication"),
    path("api/", include("accounts.api.urls")),
    
]
