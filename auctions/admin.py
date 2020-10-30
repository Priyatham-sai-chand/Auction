from django.contrib import admin
from .models import User
from .models import AuctionListing,Comment,Bids

# Register your models here.
admin.site.register(User)
admin.site.register(AuctionListing)
admin.site.register(Comment)
admin.site.register(Bids)
