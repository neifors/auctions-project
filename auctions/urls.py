from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='auctions-home'),
    path('<int:id>/', views.show, name='auctions-show'),
    path("new/", views.create, name="auctions-create"),
]
