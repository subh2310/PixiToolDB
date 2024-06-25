from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from pixi_db.views import (
    SQLAlchemyComparePairsAPIView,
    SQLAlchemyConnectNEAPIView,
    SQLAlchemyDisconnectNEAPIView,
    SQLAlchemySendRCVAPIView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/connectdb/', SQLAlchemyConnectNEAPIView.as_view()),
    path('api/disconnectdb/', SQLAlchemyDisconnectNEAPIView.as_view()),
    path('api/sendRcvdb/', SQLAlchemySendRCVAPIView.as_view()),
    path('api/compairPairdb/', SQLAlchemyComparePairsAPIView.as_view()),

]
