import os
from datetime import datetime, timedelta
from os.path import dirname, join

import questionary
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv
from redminelib import Redmine


class Inputs:
    def __init__(self, issue_subject, start_date, interval_type, interval, days_until_deadline, project, count):
        self.issue_subject = issue_subject
        self.start_date = start_date
        self.interval_type = interval_type
        self.interval = interval
        self.days_until_deadline = days_until_deadline
        self.project = project
        self.count = count


def question(redmine):
    issue_subject = questionary.text("What is the issue subject?").ask()

    try:
        start_date = datetime.strptime(
            questionary.text("When is the start date? (write in a format like 1970-01-01)").ask(),
            "%Y-%m-%d",
        ).date()
    except ValueError:
        print("[Error] Please write in a format like 1970-01-01")
        exit()

    interval_type = questionary.select(
        "Interval type?",
        choices=[
            questionary.Choice("Daily", value="Daily"),
            questionary.Choice("Monthly", value="Monthly"),
        ]
    ).ask()

    try:
        interval = (
            int(questionary.text("How many days is the interval?").ask())
            if interval_type == "Daily"
            else int(questionary.text("How many months is the interval?").ask())
        )
    except ValueError:
        print("[Error] Please input a number")
        exit()

    try:
        days_until_deadline = int(questionary.text("How many days until the deadline?").ask())
    except ValueError:
        print("[Error] Please input a number")
        exit()

    project_choices = [
        questionary.Choice(project.name, value=project)
        for project in redmine.project.all()
    ]
    project = questionary.select(
        "Which project?",
        choices=project_choices
    ).ask()

    try:
        count = int(questionary.text("How many issues do you want to create?").ask())
    except ValueError:
        print("[Error] Please input a number")
        exit()

    return Inputs(issue_subject, start_date, interval_type, interval, days_until_deadline, project, count)


def create_issue_params(inputs):
    params = []

    for i in range(inputs.count):
        start_date = inputs.start_date + (
            relativedelta(days=inputs.interval * i)
            if inputs.interval_type == "Daily"
            else relativedelta(months=inputs.interval * i)
        )
        due_date = start_date + timedelta(days=(inputs.days_until_deadline - 1))
        params.append({
            'subject': inputs.issue_subject,
            'start_date': start_date,
            'due_date': due_date,
            'project_id': inputs.project.id,
        })
    return params


def init_env():
    dotenv_path = join(dirname(__file__), '../.env')
    load_dotenv(dotenv_path)


def main():
    init_env()
    redmine = Redmine(os.environ.get("REDMINE_URL"), key=os.environ.get("REDMINE_API_KEY"))
    inputs = question(redmine)
    params = create_issue_params(inputs)
    for param in params:
        issue = redmine.issue.create(**param)
        print(f'Created: #{issue.id} {issue.subject}')
    print("Created all issues.")


if __name__ == '__main__':
    main()
