from rest_framework import serializers
from .models import Note
from django.contrib.auth import get_user_model

User = get_user_model()


class NoteSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Note
        fields = ['user_id', 'title', 'text_content', 'audio_content', 'video_content', 'created_at']

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise serializers.ValidationError('User not found')

        validated_data['user'] = user
        note = Note.objects.create(**validated_data)
        return note
