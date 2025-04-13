from django.contrib import admin
from egramApp.models import Aadhar,Birth,Death,Complaint,Contacts
from .models import Transaction

admin.site.register(Aadhar)
admin.site.register(Birth)
admin.site.register(Death)
admin.site.register(Complaint)
admin.site.register(Contacts)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'amount', 'status', 'send') 