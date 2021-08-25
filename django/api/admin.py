from django.contrib import admin
from .models import *

admin.site.register(Clients)
admin.site.register(Bills)
admin.site.register(Products)
admin.site.register(BillsProducts)