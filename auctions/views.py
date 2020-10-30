from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import  HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from .models import User,AuctionListing,Comment,Bids


categories = ['Fashion','Electronics','Home','Sports','Toys','Automobile','Books','Videogames', 'Other']

class BidForm(forms.Form):
    bid_value = 0.00

    def __init__(self, bid_value,*args,**kwargs ):
        super().__init__(*args,**kwargs)
        self.bid_value = bid_value + 1
        self.fields['bid'].widget.attrs['min'] = self.bid_value 
 
    bid = forms.DecimalField(decimal_places=2)

def watch(request,title):
    """
    Used to assign watchlist and unwatch for a user

    """
    if request.method =="POST":
        listing_obj = AuctionListing.objects.get(title=title)
        if request.user in listing_obj.watchlists.all():
            request.user.watchlist.remove(listing_obj)
        else:
            request.user.watchlist.add(listing_obj)
    previous_url = request.POST.get('previous','/')
    
    return HttpResponseRedirect(previous_url) 

def watchlist(request):
    """
    Used to display the page Watchlist

    """
    listings = request.user.watchlist.all()

    return render(request,"auctions/watchlist.html",{
        "Watchlistings": listings
    })
    
def index(request):
    """
    Used to Display the homepage
    """
    listings = AuctionListing.objects.all()
    
    return render(request, "auctions/index.html",{
        "Listings":listings,
        
    })
def all_listings(request):
    """
    Used to display all the listings
    """
    listings = AuctionListing.objects.all()

    return render(request,"auctions/all_listings.html",{
        "Listings":listings
    })
    
def listing(request,title):
    """
    Used to display the listing page and commenting

    """
    listing_obj = AuctionListing.objects.get(pk = title)
    bids = Bids.objects.get(listing = listing_obj)
    if request.method == "POST":
        body = request.POST["comment_body"]
        comment = Comment(user=request.user,listing=listing_obj,body = body)
        comment.save()
        
    return render(request,"auctions/listing.html",{
        "Listing": listing_obj,
        "bids" : bids,
        "bid_form":BidForm(bids.bid_value)
    })

def category(request,cat_name = None):
    """
    Used to dispaly the category page 
    """
    if( cat_name != None):
        if cat_name.capitalize() in categories:

            listings = AuctionListing.objects.filter(category=cat_name.capitalize())
            print(listings)

            return render(request, "auctions/category.html",{
            "listings":listings,
            "cat_name": cat_name

            })
        
    else:
        return render(request,"auctions/category_listing.html",{
            "categories": categories
        })

def login_view(request):
    """
    Used to authenticate a user

    """
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    """
    Used to log out a user
    """
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    """
    Used to register a user
    """
    
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create(request):
    """
    Used to create a Listing
    """
    if request.method == "POST":
        title = request.POST["title"] 
        desc = request.POST["desc"] 
        starting_bid = request.POST["starting_bid"]
        photo_url = request.POST["photo"]
        
        # alternate photo to display
        if photo_url == "":
            photo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/No_image_available_600_x_450.svg/1280px-No_image_available_600_x_450.svg.png"
        category_value = request.POST["category"]
        listing_obj = AuctionListing(title = title, desc = desc, user = request.user,price = starting_bid, picture = photo_url,category=category_value)
        listing_obj.save()
        bid_obj = Bids(bid_value = starting_bid, listing = listing_obj, user = request.user)
        bid_obj.save()
        return render(request,"auctions/index.html",{
            "Listings" : AuctionListing.objects.all()
        })
    else:    
        return render(request,"auctions/create_listing.html",{
            "categories":categories
        })
def bid(request, title):
    """
    Used to bid on a listing
    """
    listing_value = AuctionListing.objects.get(title=title)
    bid_obj = Bids.objects.get(listing = listing_value)
    form = BidForm(bid_obj.bid_value,request.POST)
    if form.is_valid():
        new_bid_value = form.cleaned_data["bid"]
    bid_obj.bid_value = float("{0:.2f}".format(new_bid_value))
    bid_obj.user = request.user
    bid_obj.save()

    return render(request,"auctions/listing.html",{   
        "Listing": listing_value,
        "bids" : bid_obj,
        "bid_form":BidForm(bid_obj.bid_value)
     })
def close_bid(request,title):
    """
    Used to end the listing and declare a winner
    """
    listing_value = AuctionListing.objects.get(title=title)
    listing_value.closed = True
    listing_value.save()

    #  get a hidden input to return back to same page

    previous_url = request.POST.get('previous','/')
    return HttpResponseRedirect(previous_url)




