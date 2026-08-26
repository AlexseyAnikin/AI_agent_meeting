from pathlib import Path
from models.meeting import Meeting
from tools.speech_recognizer import SpeechRecognizer

def main() -> None:
    print("Meeting AI Agent")

    file_path_text = input("Введите путь к аудиофайлу: ").strip()
    audio_path = Path(file_path_text)

    meeting = Meeting(audio_path)
    recognizer = SpeechRecognizer()

    try:
        text = recognizer.transcribe(meeting.audio_path)
        meeting.set_transcript(text)

        print("Расшифровка")
        print(meeting.transcript)

    except FileNotFoundError as error:
        print(f"Ошибка распознавания: {error}")

    except ValueError as error:
        print(f"Некорректный путь: {error}")


if __name__ == "__main__":
    main()

