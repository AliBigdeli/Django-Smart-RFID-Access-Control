from django.urls import path
from . import views

app_name = "api-v1"

urlpatterns = [
    path("card-reader/",views.CardReaderListApiView.as_view(),name="card-reader-list"),
    path("card-reader/<int:pk>/",views.CardReaderDetailApiView.as_view(),name="card-reader-Detail"),
    path("card-id/",views.CardUidListApiView.as_view(),name="card-uid-list"),
    path("card-id/<int:pk>/",views.CardUidDetailApiView.as_view(),name="card-uid-Detail"),
    path("card-reader/gateway/",views.GatewayCardReaderApiView.as_view(),name="gateway-card-reader"),
    path("card-gateway/log/",views.CardReaderLogApiView.as_view(),name="card-gateway-log"),
]

