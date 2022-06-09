from django import forms
from .models import Auction, Bid, Comment
from django.core.exceptions import ValidationError



class NewAuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['title', 'description', 'initial_price','category', 'photo']

class NewBidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']
        labels = {'amount': "Your amount"}

        
class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'message']
