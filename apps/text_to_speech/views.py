import uuid

from bark import generate_audio
from django.core.files.base import ContentFile
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.text_to_speech.models import TextToSpeechModel
from apps.text_to_speech.serializers import TextToSpeechModelSerializerDetails


# @api_view(["GET"])
# @permission_classes([AllowAny])
# def txt_to_audio_view(request):
#     text = request.GET.get("text")
#     # text_prompt = """
#     #      Hello, my name is Suno. And, uh — and I like pizza. [laughs]
#     #      But I also have other interests such as playing tic tac toe.
#     # """
#     text_prompt = text
#     audio_array = generate_audio(text_prompt)
#
#     # save audio to disk
#     write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)
#
#     # play text in notebook
#     Audio(audio_array, rate=SAMPLE_RATE)
#
#     return Response(
#         {"message": "This is an asynchronous view!"}, status=status.HTTP_200_OK
#     )


@api_view(["POST"])
@permission_classes([AllowAny])
def txt_to_audio_view(request):
    text = request.data.get("text")

    if text:
        text_prompt = text
        audio_array = generate_audio(text_prompt)

        # Generate a unique filename
        unique_filename = f"{uuid.uuid4().hex[:10]}_generated_audio.wav"

        # Create an instance of TextToSpeech model and save it
        text_to_speech_instance = TextToSpeechModel(text=text)
        audio_content = ContentFile(audio_array.tobytes())
        text_to_speech_instance.audio.save(unique_filename, audio_content)

        serialize_obj = TextToSpeechModelSerializerDetails(text_to_speech_instance, context={"request": request})

        return Response(
            serialize_obj.data,
            status=status.HTTP_201_CREATED
        )
    else:
        return Response(
            {"message": "Text not provided."},
            status=status.HTTP_400_BAD_REQUEST
        )
