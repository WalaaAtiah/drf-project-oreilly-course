from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True) #to defind new field
    class Meta:
        model=User
        fields=['username','email','password','password2']  #password2 not create in Usermodel then need to defind it 
        extra_kwargs={
            'password':{'write_only':True}
        } 
        
    #check password==pasword2
    #check that ther is another user have the same email and username
    #create new account
    
    def save(self):
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password!=password2:
            raise serializers.ValidationError({'Error':"password and password2 should be same"})
            
        if User.objects.filter(email=self.validated_data['email']).exists():
             raise serializers.ValidationError({'Error':"the email is already exists"})
         
         #crea
        account=User(email=self.validated_data['email'],username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account