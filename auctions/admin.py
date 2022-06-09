from django.contrib import admin

# Register your models here.
from .models import Auction, Comment, Category, Bid, Watchlist


admin.site.register(Auction)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Bid)
admin.site.register(Watchlist)
