# online-asr-client-code

This repo including sample clients to connect with NTU AISpeechLab server
The audio format should be either in .wav, .mp3 or raw.

Online scripts
    python <script> -m <mode> -u <server_url> -r <rate> -t <your_token> <path_to_audio_file>

    Where
    <mode>: must be 'file' or 'stream'
    <path_to_audio_file>: is required in file mode, but for stream it isn't required
    <your_token>: Please get the token from AISpeechLab
    <user_url>: ws://HOST:PORT/client/ws/speech


* client.py
     * Connect with AISpeechLab online ASR via websocket, simulate streaming audio from file
     * Example usage:
         python client.py -u <server_url> -r <rate> -t <your_token> <path_to_audio_file>

* client2.py
     * Connect with AISpeechLab online ASR via websocket, simulate streaming audio from file 
       or microphone, using Python2.
     * Example usage:
         python client2.py -m <mode> -u <server_url> -r <rate> -t <your_token> <path_to_audio_file>
       
* client3.py
     * Connect with AISpeechLab online ASR via websocket, simulate streaming audio from file 
       or microphone, using Python3.
     * Example usage:
         python client3.py -m <mode> -u <server_url> -r <rate> -t <your_token> <path_to_audio_file>

* offline_client.py
     * Connect with AISpeechLab offline ASR via HTTP POST request, including 3 steps
         - Upload your audio file -> get the speechId
         - Check the processing status based on returned speechId
         - Download the transcription when the processing is done
     * Example usage
        

