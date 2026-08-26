import json
import ollama

from models.task import Task
from models.meeting_report import MeetingReport


class MeetingAnalyzer:
    def analyze(self, transcript):
        response = ollama.chat(
            model="qwen3:14b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Ты анализатор рабочих совещаний."
                        "Твоя задача только извлекать факты из текста."
                        "Не давать советов и не придумывай отсутствующую информацию."
                        "Если значение неизвестно, верни только null."
                        "Верни только JSON со следующими полями: "
                        "topic, summary, participants, decisions, tasks, open_questions. "
                        "participants, decisions, tasks и open_questions всегда должны быть массивами. "
                        "Если элементов нет, возвращай пустой массив []. "
                        "tasks должен быть массивом объектов с полями "
                        "description, assignee, deadline, priority."
                        "Если assignee, deadline или priority неизвестны, используй null."
                        "Если в тексте указан относительный срок вроде 'до пятницы', 'завтра', "
                        "'через неделю', преобразуй его в конкретную дату в формате YYYY-MM-DD,"
                        "используя дату совещания. Если определить дату невозможно, верни исходную"
                        "формулировку."
                        
                    )
                    
                },
                {
                    "role": "user",
                    "content": (
                        "Добрый день. Начинаем рабочее совещание. "
                        "Сегодня необходимо обсудить состояние проекта Meeting AI Agent. "
                        "Алексей отвечает за разработку программы. "
                        "До пятницы необходимо завершить модуль распознавания речи. "
                        "Следующее совещание состоится на следующей неделе."
                    )
                }
            ],
            format="json",
            options={
                "temperature": 0
            }
        )

        data = json.loads(response.message.content)

        return self.create_report(data)
        

    def create_report(self, data):
        tasks = []

        for task_data in data["tasks"]:
            task = Task(
                task_data["description"],
                task_data["assignee"],
                task_data["deadline"],
                task_data["priority"]
            )

            tasks.append(task)

        report = MeetingReport(
            data["topic"],
            data["summary"],
            data["participants"],
            data["decisions"],
            tasks,
            data["open_questions"])

        return report
