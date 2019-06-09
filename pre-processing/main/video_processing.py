import json
from audio.audio_processor import AudioProcessor


def process_videos(event):
    operation = event['operation']

    operations = {
        'extract-audio': lambda x: AudioProcessor().process(**x)
    }

    if operation in operations:
        return operations[operation](event.get('payload'))
    else:
        raise ValueError('Unrecognized operation "{}"'.format(operation))


with open('../resources/video_processing.json') as f:
    data = json.load(f)

process_videos(data)