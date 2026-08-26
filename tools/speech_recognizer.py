from pathlib import Path
from faster_whisper import WhisperModel

class SpeechRecognizer:
    def __init__(self):
        self.model = WhisperModel(
            "small",
            device="cpu",
            compute_type='int8'
        )

    def transcribe(self, audio_path):
        path = Path(audio_path)

        if not path.exists():
            raise FileNotFoundError(f"Файл не найден: {audio_path}")

        if not path.is_file():
            raise ValueError(f"Ошибка: указанный путь не является файлом: {audio_path}")

        segments, info = self.model.transcribe(str(path), language="ru")

        text_parts = []

        for segment in segments:
            text_parts.append(segment.text)

        return " ".join(text_parts).strip()