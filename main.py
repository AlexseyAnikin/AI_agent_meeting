from pathlib import Path
from datetime import date


from models.meeting import Meeting
from tools.meeting_analyzer import MeetingAnalyzer
from tools.speech_recognizer import SpeechRecognizer

def main() -> None:
    print("Meeting AI Agent")

    file_path_text = input("Введите путь к аудиофайлу: ").strip()
    audio_path = Path(file_path_text)

    meeting_data = date.today()
    meeting = Meeting(audio_path, meeting_data)

    recognizer = SpeechRecognizer()
    analyzer = MeetingAnalyzer()

    try:
        text = recognizer.transcribe(meeting.audio_path)
        meeting.set_transcript(text)

        print("Расшифровка")
        print(meeting.transcript)

        report = analyzer.analyze(meeting.transcript)

        print("\nТема: ")
        print(report.topic)

        print("\nКраткое содержание: ")
        print(report.summary)

        print("\nЗадачи:")

        for task in report.tasks:
            print(f"Описание: {task.description}")
            print(f"Ответсвенный: {task.assignee}")
            print(f"Срок: {task.deadline}")
            print(f"Приоритет: {task.priority}")
            print()

    except FileNotFoundError as error:
        print(f"Ошибка распознавания: {error}")

    except ValueError as error:
        print(f"Некорректный путь: {error}")


if __name__ == "__main__":
    main()

