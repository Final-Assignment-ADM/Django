from rest_framework import serializers
from .models import Item
  
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id','Image',"Firstname","Lastname","Gender","Age","Location","Occupation","Uploded_by","Uploded_on","No_of_download")