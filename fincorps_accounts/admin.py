from django.contrib import admin
from fincorps_accounts. models import User, General_Ledger

# Register your models here.
admin.site.register(User)
admin.site.register(General_Ledger)
