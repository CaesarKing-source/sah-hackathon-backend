from rest_framework import serializers
from home.models import Hackathon
from home.models import Contact


class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = ['id', 'teamname', 'collegename', 'domain', 'leadername', 'leaderemail', 'leadernumber', 'leadergender', 
                  'branch', 'year', 
                  'member2name', 'member2gender', 
                  'member3name', 'member3gender', 
                  'member4name', 'member4gender', 
                  'member5name', 'member5gender', 
                  'amount', 'transactionid', 'date']
        
    
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'phone', 'team', 'message', 'date']
        
        

