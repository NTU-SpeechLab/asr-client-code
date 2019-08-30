"""Client module calling remote ASR """
import os, time
import json
import requests

__version__ = "1.0.0"
__author__ = "NTU"
__status__ = "Alpha"

__all__ = ['send_audio', 'check_status', 'get_transcription']


_SPEECH_URL = 'http://168.63.242.64:4040/speech'
_KEY = 'Bearer <YOUR_TOKEN>'
_HEADER = {'accept': 'application/json', 'Authorization': _KEY}

def check_status(speech_id):
    ''' Check ASR status with given id '''
    try:
        url = _SPEECH_URL + '/status/' + speech_id
        res = requests.get(url, headers=_HEADER)
        res = json.loads(res.text)
        completed = res['speech']['finished']
        return completed
    except Exception as ex:
        print('Error in getting ASR status: ', str(ex))


def download_trans(speech_id):
    try:
        url = _SPEECH_URL + '/result/' + speech_id
        res = requests.get(url, headers=_HEADER)
        with open(speech_id + '.zip', 'wb') as f:
           f.write(res.content)

        return res.ok
    except Exception as ex:
        print('Error in getting ASR status: ', str(ex))

     
     
def send_audio(audio_file):
    ''' Send an audio file to remote ASR server '''
    try:
        files = {'file': (os.path.split(audio_file)[-1], open(audio_file, 'rb')), 'server': (None, 'english')}
        res = requests.post(_SPEECH_URL, headers=_HEADER, files=files)
        res = json.loads(res.text)
        speech_id = res['speech']['_id']
        return speech_id
    except Exception as ex:
        print('Error in sending audio file: ', str(ex))


def main():
    speed_id = send_audio('speech.wav')
    print('... Getting speech id %s ...' % speed_id)
    
    _time_delay = 30.0   
    time.sleep(_time_delay)
    
    completed = check_status(speed_id)

    if not completed:
        print('*** Error: ASR did not complete the transcription')
    else:
        print('*** ASR done!')
        print('... Downloading transcription ...')
        download_trans(speed_id)
        print('*** Finish downloading transcription!')


if __name__ == '__main__':
    main()
