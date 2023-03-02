
from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review

############################################# for Review module ###########################################
# type :serializers.Moduleserializer in the class

class ReviewSerializer(serializers.ModelSerializer):
   
   class Meta:
      model=Review
      fields="__all__"
      

############################################# for Watchlist module ###########################################
# type :serializers.Moduleserializer in the class

class WatchSerializer(serializers.ModelSerializer):
   Review=ReviewSerializer(many=True,read_only=True)     #render hole object  see all review in each movie 
   class Meta:
      model=WatchList
      fields="__all__"
      
      
      
############################################# for StreamPlatform module ###########################################

#type :serializers.ModelSerializer in the class  
class StreamPlatSerializer(serializers.ModelSerializer):
   WatchList=WatchSerializer(many=True,read_only=True)     #render hole object   
   class Meta:
      model=StreamPlatform
      fields="__all__"
      
# type :serializers.HyperlinkedModelSerializer in the class  
# class StreamPlatSerializer(serializers.HyperlinkedModelSerializer):
#    WatchList=WatchSerializer(many=True,read_only=True)     #render hole object  
#    url = serializers.HyperlinkedIdentityField(view_name="StreamPlat_Detail")
   
#    class Meta:
#       model=StreamPlatform
#       fields="__all__"
          
      
      
      
# type :serializers.Moduleserializer in the class

# class StreamPlatSerializer(serializers.ModelSerializer):
#    WatchList=WatchSerializer(many=True,read_only=True)     #render hole object  
#    # WatchList=serializers.StringRelatedField(many=True)      # render the movies __str__   *StringRelatedField*
#    # WatchList=serializers.PrimaryKeyRelatedField(many=True,read_only=True)  # render the pk for each object  *PrimaryKeyRelatedField*
   
#    # WatchList=serializers.HyperlinkedRelatedField(           # render the link for the object *HyperlinkedRelatedField*
#    #      many=True,
#    #      read_only=True,
#    #      view_name='Watch-details'
#    #  )
   
#    class Meta:
#       model=StreamPlatform
#       fields="__all__"
      
      
      




##################################################for movie module ######################################

# type :serializers.Moduleserializer in the class

# class MovieSerializer(serializers.ModelSerializer):
#    len_name=serializers.SerializerMethodField()  
   
#    class Meta:
#       model=Movie
#       fields="__all__"
#       # field=['id','name']
#       # exclude=['active ']
      
#    def get_len_name(self,object):
#       return len(object.name)
      
#    def validate(self, data):
#       if data['name'] == data['description']:
#          raise serializers.ValidationError("name and description should be diffrent")
#       return data
       
             
#    def validate_name(self, value):
#       if len(value)<2:
#          raise serializers.ValidationError("name is too short")
#       else:
#          return value
   










## type :serializers.serializer in the class

# def discreption_length(value):
#    if len(value) <2:
#       raise serializers.ValidationError("description is too short2222222222222222")


# class MovieSerializer(serializers.Serializer):
#    id=serializers.IntegerField(read_only=True)
#    name=serializers.CharField()
#    description=serializers.CharField(validators=[discreption_length])
#    active=serializers.BooleanField()
   
#    def create(self,validated_data):
#       return Movie.objects.create(**validated_data)
   
#    def update(self, instance, validated_data):
#       instance.name=validated_data.get('name',instance.name)
#       instance.description=validated_data.get('description',instance.description)
#       instance.active=validated_data.get('active',instance.active)
#       instance.save()
#       return instance
   
#    def validate(self, data):
#       if data['name'] == data['description']:
#          raise serializers.ValidationError("name and description should be diffrent")
#       return data
       
             
#    def validate_name(self, value):
#       if len(value)<2:
#          raise serializers.ValidationError("name is too short")
#       else:
#          return value
      
   # def validate_description(self, value):
   #    if len(value)<2:
   #       raise serializers.ValidationError("description is too short")
   #    else:
   #       return value