###############################################################################
# Copyright (C) 2021, created on June 19, 2021
# Written by Justin Ho
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3 as published by
# the Free Software Foundation.
#
# This source code is distributed in the hope that it will be useful and
# without warranty or implied warranty of merchantability or fitness for a
# particular purpose.
###############################################################################

import json
import random
import datetime
from string import ascii_letters, digits

from .templates import project_template, task_template


class SuperProductivity:

    chars = digits + ascii_letters + "_"

    def __init__(self, path):

        self.path = path
        self.ids = set()
        self.project_dict = {}
        self.load_data()

    def load_data(self):
        with open(self.path) as f:
            sp = json.load(f)
        self.data = sp
        self.ids = set(self.get_bookmark_ids() +
                       self.get_note_ids() +
                       self.get_reminder_ids() +
                       self.get_project_ids() +
                       self.get_task_ids())
        self.project_dict = self.load_project_dict()

    def get_bookmark_ids(self):
        ids = []
        for project_id, info in self.data["bookmark"].items():
            ids.extend(info["ids"])
        return ids

    def get_note_ids(self):
        ids = []
        for project_id, info in self.data["note"].items():
            ids.extend(info["ids"])
        return ids

    def get_reminder_ids(self):
        return [obj["id"] for obj in self.data["reminders"]]

    def get_project_ids(self):
        return self.data["project"]["ids"]

    def get_task_ids(self):
        return self.data["task"]["ids"]

    def generate_id(self):
        """Generates a new id"""
        while True:
            new_id = "".join([random.choice(self.chars) for x in range(9)])
            if new_id not in self.ids:
                self.ids.add(new_id)
                return new_id

    def get_project_names(self):
        return set((info["title"] for id_, info in self.data["project"]["entities"].items()))

    def load_project_dict(self):
        return {info["title"]: id_ for id_, info in self.data["project"]["entities"].items()}

    def add_project(self, project_name):
        project_id = self.generate_id()
        project = project_template.copy()
        project["id"] = project_id
        project["title"] = project_name

        self.data["project"]["ids"].append(project_id)
        self.data["project"]["entities"][project_id] = project
        self.project_dict[project_name] = project_id

    def add_task(self, task_name, project_name):
        task_id = self.generate_id()
        project_id = self.project_dict[project_name]
        timestamp = int(datetime.datetime.now().timestamp() * 1000000)
        task = task_template.copy()
        task["id"] = task_id
        task["projectId"] = project_id
        task["title"] = task_name
        task["created"] = timestamp

        self.data["task"]["ids"].append(task_id)
        self.data["task"]["entities"][task_id] = task
        self.data["project"]["entities"][project_id]["taskIds"].append(task_id)

    def write_json(self, path):
        with open(path, "w") as f:
            json.dump(self.data, f)
