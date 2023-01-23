from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    document_type = serializers.CharField(required=True)
    document = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all(), message="Document is already used")]
    )
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    hobbie = serializers.CharField(required=True)


    class Meta:
        model = CustomUser
        fields = ('id', 'document_type', 'document', 'first_name', 'last_name', 'email', 'hobbie')
        
        
    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
