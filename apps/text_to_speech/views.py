import os
import uuid

from bark import generate_audio, SAMPLE_RATE
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from scipy.io.wavfile import write as write_wav

from apps.text_to_speech.models import TextToSpeechModel
from apps.text_to_speech.serializers import TextToSpeechModelSerializerDetails


@api_view(["GET"])
@permission_classes([AllowAny])
def get_voice_list(request):
    promot_name_list = [
        "v2/en_speaker_0",
        "v2/en_speaker_1",
        "v2/en_speaker_2",
        "v2/en_speaker_3",
        "v2/en_speaker_4",
        "v2/en_speaker_5",
        "v2/en_speaker_6",
        "v2/en_speaker_7",
        "v2/en_speaker_8",
        "v2/en_speaker_9",
    ]

    return Response(
        promot_name_list,
        status=status.HTTP_200_OK
    )


@api_view(["POST"])
@permission_classes([AllowAny])
def txt_to_audio_view(request):
    text = request.data.get("text")
    voice = request.data.get("voice", None)

    if text:
        text_prompt = text
        if voice is not None:
            # history_prompt
            promot_name_list = [
                "v2/en_speaker_0",
                "v2/en_speaker_1",
                "v2/en_speaker_2",
                "v2/en_speaker_3",
                "v2/en_speaker_4",
                "v2/en_speaker_5",
                "v2/en_speaker_6",
                "v2/en_speaker_7",
                "v2/en_speaker_8",
                "v2/en_speaker_9",
            ]

            if voice in promot_name_list:
                audio_array = generate_audio(text_prompt, history_prompt=voice)
            else:
                return Response(
                    {
                        "message": "voice is not valid. Must be from this list",
                        "voice_list": promot_name_list,
                    }
                )

        else:
            audio_array = generate_audio(text_prompt)

        # Generate a unique filename
        audio_filename = f"{uuid.uuid4().hex[:10]}_generated_audio.wav"

        # Save audio to disk
        write_wav(audio_filename, SAMPLE_RATE, audio_array)

        # # Create an instance of TextToSpeech model and save it
        # text_to_speech_instance = TextToSpeechModel.objects.create(text=text)
        # text_to_speech_instance.audio.save(audio_filename, open(audio_filename, 'rb'))
        # text_to_speech_instance.save()

        # Create an instance of TextToSpeech model and save it
        text_to_speech_instance = TextToSpeechModel.objects.create(text=text)
        audio_content = open(audio_filename, 'rb')
        text_to_speech_instance.audio.save(audio_filename, audio_content)
        audio_content.close()

        # Delete the temporary audio file
        os.remove(audio_filename)

        # Create an instance of TextToSpeech model and save it
        # text_to_speech_instance = TextToSpeechModel.objects.create(text=text)
        # audio_content = ContentFile(audio_array.tobytes())
        # text_to_speech_instance.audio.save(unique_filename, audio_content)
        # text_to_speech_instance.save()

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
