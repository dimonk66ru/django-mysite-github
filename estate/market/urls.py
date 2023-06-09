from django.urls import path
from .views import (
    AboutView,
    EstateListView,
)

app_name = "market"

urlpatterns = [
    path("about/", AboutView.as_view(), name="about"),
    path("market/", EstateListView.as_view(), name="estates"),
]
