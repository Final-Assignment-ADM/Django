from django.contrib import admin
# import the model Todo
from .models import Item
 
# creating a class for the admin-model integration
class ItemAdmin(admin.ModelAdmin):
 
    #the fields of the model
    list_display = ['Image',"Firstname","Lastname","Gender","Age","Location","Occupation","Uploded_by","Uploded_on","No_of_download"]
 
# we will need to register the
# model class and the Admin model class
# using the register() method
# of admin.site class
admin.site.register(Item,ItemAdmin)