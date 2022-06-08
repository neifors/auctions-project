from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='auctions-home'),
    path('<int:id>/', views.show, name='auctions-show'),
    path("new/", views.create, name="auctions-create"),
    path("watchlist/", views.watchlist, name="auctions-watchlist"),
    path("mylistings/", views.my_listings, name="auctions-mylistings")
]
