class Meeting:
    def __init__(self, audio_path):
        self.audio_path = audio_path
        self.transcript = None

    def set_transcript(self, text):
        self.transcript = text
