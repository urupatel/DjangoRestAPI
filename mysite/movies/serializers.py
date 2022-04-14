from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Moviedata


#take a look for what model and look for the field and generate the JSON and send back to us 
class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length = None, use_url= True)
    class Meta:
        model = Moviedata
        fields = ["id","name","duration","rating","typ", 'image']