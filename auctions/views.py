from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import NewAuctionForm, NewBidForm, NewCommentForm

from .models import Auction, Bid, Category, Comment, Watchlist

def home(request):
    data = { 
        'active_auctions': Auction.objects.filter(active=True),
        'inactive_auctions': Auction.objects.filter(active=False)
    }
    return render(request, 'auctions/auctionsList.html', data)

def show(request, id):
    # Common data
    auction = get_object_or_404(Auction, pk=id)
    bids = Bid.objects.filter(auction_id = id)
    last_bid = bids.order_by('-amount')
    if not last_bid:
        last_bid = ['--']
    error = ""
    comments = Comment.objects.filter(auction_id = id)
    is_in_watchlist = Watchlist.objects.filter(user=request.user, auction=auction)
    # is_in_watchlist = list(filter(lambda w: w.auction == auction, user_watchlist))
    
    # POST method cases
    if request.method == 'POST':
        bid_form = NewBidForm(request.POST)
        comment_form = NewCommentForm(request.POST)
        
        # if submitted a new bid
        if bid_form.is_valid():
            amount = bid_form.cleaned_data.get("amount")
            # If there is at least one bid done
            if last_bid:
                # Amount needs to be higher than that bid to save it
                if amount>last_bid[0].amount:
                    Bid.objects.create(user_id=request.user.id,auction_id=id,amount=amount)
                    return redirect ('auctions-show', id = id)
                # If not, will show an error message
                else:
                    error += "Your bid needs to be higher than last bid"
            # If there is no bid yet, amount needs to be greater or equal to initial price to save it
            elif amount>=auction.initial_price:
                Bid.objects.create(user_id=request.user.id,auction_id=id,amount=amount)
                return redirect ('auctions-show', id = id)
             # If not, will show an error message
            else:
                error += "Your bid needs to be higher than initial price."
                
        # If submitted a new comment
        elif comment_form.is_valid():
            title = comment_form.cleaned_data.get('title')
            message = comment_form.cleaned_data.get('message')
            Comment.objects.create(user_id = request.user.id,title = title,message = message, auction_id=id)
            return redirect ('auctions-show', id=id)
        
        # If deactivating an auction
        elif request.POST['auction']:
            deactivated = auction.deactivate()
            deactivated.save()
            return redirect ('auctions-home')
        
        # If adding to watchlist
        elif request.POST['watchlist'] == "True":
            if not is_in_watchlist:
                Watchlist.objects.create(user_id=request.user.id,auction_id=id)
            return redirect ('auctions-show', id=id)

        # If removing from watchlist
        elif request.POST['watchlist'] == "False":
            is_in_watchlist.delete()
            return redirect ('auctions-show', id=id)
        
    # Data to send to frontend if request method is GET or if any of the POST cases ended with an error
    data = {
        'total_bids' : len(bids),
        'last_bid' : last_bid[0],
        'comments' : comments,
        'auction': auction,
        'bid_form' : NewBidForm(),
        'comment_form' : NewCommentForm(),
        'error': error,
        'is_in_watchlist': True if len(is_in_watchlist) else False
    }
    return render(request, 'auctions/auction.html', data)

    
@login_required
def create(request):
    if request.method == 'POST':
        form = NewAuctionForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user.id
            title = form.cleaned_data.get("title")
            description = form.cleaned_data.get("description")
            initial_price = form.cleaned_data.get("initial_price")
            photo = form.cleaned_data.get("photo")
            category = form.cleaned_data.get("category")
            auction=Auction.objects.create(user_id=user,title=title,description=description,initial_price=initial_price,photo=photo,category=category)
            return redirect("auctions-show", id = auction.id )
    else:
        form = NewAuctionForm()
        
    data = {'form': form}
    return render(request, 'auctions/new.html', data)

@login_required
def watchlist(request):
    data = {
        'my_watchlist' : Watchlist.objects.filter(user=request.user)
    }
    return render(request, 'auctions/watchlist.html', data)

@login_required
def my_listings(request):
    data = {
        'my_auctions' : Auction.objects.filter(user=request.user)
    }
    return render(request, 'auctions/myListings.html', data)

def categories(request):
    data = {
        'categories' : Category.objects.all()
    }
    return render(request, 'auctions/categories.html',data)


def by_category(request, id):
    data = {
        'auctions' : Auction.objects.filter(category_id = id)
    }
    return render(request, 'auctions/by_category.html', data)
