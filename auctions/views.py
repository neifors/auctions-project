from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import NewAuctionForm, NewBidForm, NewCommentForm

from .models import Auction, Bid, Comment

def home(request):
    data = { 'auctions': Auction.objects.all() }
    return render(request, 'auctions/auctionsList.html', data)

def show(request, id):
    auction = get_object_or_404(Auction, pk=id)
    if request.method == 'POST':
        bid_form = NewBidForm(request.POST)
        comment_form = NewCommentForm(request.POST)
        if bid_form.is_valid():
            amount = bid_form.cleaned_data.get("amount")
            Bid.objects.create(user_id=request.user.id,auction_id=id,amount=amount)
            return redirect ('auctions-show', id = id)
        elif comment_form.is_valid():
            title = comment_form.cleaned_data.get('title')
            message = comment_form.cleaned_data.get('message')
            Comment.objects.create(user_id = request.user.id,title = title,message = message, auction_id=id)
            return redirect ('auctions-show', id=id)
    else:
        comments = Comment.objects.filter(auction_id = id)
        bids = Bid.objects.filter(auction_id = id)
        last_bid = bids.order_by('-amount')
        if not last_bid:
            last_bid = ['--']
        data = {
            'total_bids' : len(bids),
            'last_bid' : last_bid[0],
            'comments' : comments,
            'auction': auction,
            'bid_form' : NewBidForm(),
            'comment_form' : NewCommentForm()
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

