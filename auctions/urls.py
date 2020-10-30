from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all",views.all_listings,name="all_listings"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("create", views.create, name="create"),
    path("categories", views.category, name="categories"),
    path("category/<str:cat_name>",views.category,name="individual_categories"),
    path("listing/<str:title>",views.listing,name="listing"), 
    path("category/listing/<str:title>",views.listing,name="listing"), 
    path("watch/<str:title>",views.watch,name="watch"),
    path("bid/<str:title>",views.bid,name="bid"),
    path("close/<str:title>",views.close_bid,name="close_bid"),
]
