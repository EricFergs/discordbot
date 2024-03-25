from google.cloud import texttospeech
import os

tts_client = texttospeech.TextToSpeechClient()

def text_to_speech(text, output_file, language_code='en-US'):

    synthesis_input = texttospeech.SynthesisInput(text=text)


    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code, ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )


    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )


    response = tts_client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )


    with open(output_file, "wb") as out:
        out.write(response.audio_content)

    print('Audio content written to file:', output_file)

def jp_to_speech(text, output_file, language_code='ja'):

    synthesis_input = texttospeech.SynthesisInput(text=text)


    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code, ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )


    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )


    response = tts_client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )


    with open(output_file, "wb") as out:
        out.write(response.audio_content)


if __name__ == "__main__":
    # Define text to be converted to speech
    text_to_convert = "Hello, world!"

    # Define the output MP3 file path
    output_file_path = "output.mp3"

    # Convert text to speech and save as MP3
    text_to_speech(text_to_convert, output_file_path)


