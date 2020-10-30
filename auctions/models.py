from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    watchlist = models.ManyToManyField('AuctionListing',blank = True,related_name="watchlists")

class AuctionListing(models.Model):
    category_choices = (
        ('Fashion','Fashion'),
        ('Electronics','Electronics'),
        ('Home','Home'),
        ('Sports','Sports'),
        ('Toys','Toys'),
        ('Automobile','Automobile'),
        ('Books','Books'),
        ('Videogames','Videogames'),
        ('Other','Other'),
    )
    title = models.CharField(max_length = 64,primary_key = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    price = models.DecimalField(max_digits = 10,decimal_places = 2)
    desc = models.CharField(max_length = 1000)
    picture = models.URLField(default="https://www.riobeauty.co.uk/images/product_image_not_found.gif")
    category = models.CharField(max_length = 64,choices=category_choices)
    date_added = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title}: {self.price},{self.desc},{self.picture},{self.category},{self.date_added}"


class Comment(models.Model):
    listing = models.ForeignKey(AuctionListing,on_delete = models.CASCADE,related_name="comments")
    user = models.ForeignKey(User,related_name="commited_user",on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.listing.title, self.user)
class Bids(models.Model):
    bid_value = models.DecimalField(max_digits = 10,decimal_places = 2)
    user = models.ForeignKey(User,on_delete = models.CASCADE, related_name="bidding_user")
    listing = models.ForeignKey(AuctionListing, on_delete= models.CASCADE, related_name="bidding_listing")
    
    def __str__(self):
        return '%s - %s - %s' % (self.bid_value, self.user, self.listing)
