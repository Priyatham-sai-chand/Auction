"""commerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("auctions.urls"))
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


           
    #    
    #    # alternate photo to display
    #    if photo_url == "":
    #        photo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/No_image_available_600_x_450.svg/1280px-No_image_available_600_x_450.svg.png"
    #    category_value = request.POST["category"]
    #    listing_obj = AuctionListing(title = title, desc = desc, user = request.user,price = starting_bid, picture = photo_url,category=category_value)
    #    listing_obj.save()
    #    bid_obj = Bids(bid_value = starting_bid, listing = listing_obj, user = request.user)
    #    bid_obj.save()
    #    return render(request,"auctions/index.html",{
    #        "Listings" : AuctionListing.objects.all()
    #    })