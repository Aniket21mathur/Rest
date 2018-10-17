from rest_framework import serializers
from snippets.models import Snippet,LANGUAGE_CHOICES,STYLE_CHOICES
from django.contrib.auth.models import User
from rest_framework import permissions

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
	owner=serializers.ReadOnlyField(source='owner.username')
	highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

	class Meta:
		model=Snippet
		#id is an integer field?
		fields=('url','highlight','id','title','code','linenos','language','style','owner')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
	

	class Meta:
		model=User
		fields=('url','id','username','snippets')

