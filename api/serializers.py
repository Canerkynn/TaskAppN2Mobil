from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from api.models import Task, Gorevli


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','title','description','label','employee','status','author','publish_date')
        extra_kwargs = {'url':{'required':True}}

class GorevliSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gorevli
        fields = ('id','employee')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ('id','username','password'  )
        extra_kwargs = {'password':{'required':True, 'write_only':True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user