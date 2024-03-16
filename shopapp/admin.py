from django.contrib import admin
from .models import *

admin.site.register(category)
admin.site.register(product)
admin.site.register(Buyer)
admin.site.register(order)

# Register your models here.
