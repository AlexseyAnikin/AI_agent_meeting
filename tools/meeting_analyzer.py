from models.task import Task
from models.meeting_report import MeetingReport


class MeetingAnalyzer:
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