class Meeting:
    def __init__(self, audio_path, meeting_date):
        self.audio_path = audio_path
        self.transcript = None
        self.meeting_date = meeting_date

    def set_transcript(self, text):
        self.transcript = text
