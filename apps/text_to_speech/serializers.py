from rest_framework import serializers

from apps.text_to_speech.models import TextToSpeechModel


class TextToSpeechModelSerializerDetails(serializers.ModelSerializer):
    class Meta:
        model = TextToSpeechModel
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if instance.audio:
            x = instance.audio.name.split("/")
            type = x[-1].split(".")
            audio = {
                "url": representation.pop("audio"),
                "size": instance.audio.size,
                "name": x[-1],
                "type": type[-1],
            }
            representation["audio"] = audio

        return representation
