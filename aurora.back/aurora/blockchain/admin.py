from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Block, Transaction

admin.site.register(Block, MPTTModelAdmin)
admin.site.register(Transaction)
