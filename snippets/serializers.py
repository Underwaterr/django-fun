from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Snippet

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='user_detail', read_only=True)

    class Meta:
        model = Snippet
        fields = ('id', 'created', 'title', 'code', 'user')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
