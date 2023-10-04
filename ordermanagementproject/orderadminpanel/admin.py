from django.contrib import admin
from common.models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email','status','created_at')


admin.site.register(Customer, CustomerAdmin)
