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

        
    # def is_valid(self):
    #     errors={}
    #     bid = self.cleaned_data('amount')

    #     if bid <= 0:
    #         errors.append(ValidationError("Input an amount greater than 0"))

    #     if bid <= Auction.current_bid:
    #         errors.append(ValidationError("Amount is low, please increase the bid"))
        
    #     if errors:
    #         raise ValidationError(errors)
            
    #     else:
    #         Auction.current_bid = bid

    #     return bid

        
class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'message']
