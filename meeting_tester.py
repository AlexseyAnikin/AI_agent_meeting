from tools.meeting_analyzer import MeetingAnalyzer

data = {
    "topic": "Meeting AI Agent",
    "summary": "Обсудили разработку проекта",
    "participants": ["Алексей", "Иван"],
    "decisions": [
        "Продолжить разработку локальной версии"
    ],
    "tasks": [
        {
            "description": "Завершить распознавание речи",
            "assignee": "Алексей",
            "deadline": "2026-08-28",
            "priority": "HIGH"
        },
        {
            "description": "Выбрать локальную LLM",
            "assignee": "Иван",
            "deadline": "2026-09-01",
            "priority": "MEDIUM"
        }
    ],
    "open_questions": [
        "Какую LLM использовать?"
    ]
}

analyzer = MeetingAnalyzer()

report = analyzer.create_report(data)

print(report.topic)

for task in report.tasks:
    print(task.description)
    print(task.assignee)
