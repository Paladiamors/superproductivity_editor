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

project_template = {
    "id": "$REQUIRED",
    "title": "$REQUIRED",
    "isArchived": False,
    "issueIntegrationCfgs": {
        "JIRA": {
            "isEnabled": False,
            "_isBlockAccess": False,
            "host": None,
            "userName": None,
            "password": None,
            "isWonkyCookieMode": False,
            "isAutoPollTickets": True,
            "searchJqlQuery": "",
            "isAutoAddToBacklog": True,
            "autoAddBacklogJqlQuery": "assignee = currentUser() AND sprint in openSprints() AND resolution = Unresolved",
            "isWorklogEnabled": True,
            "isAutoWorklog": False,
            "isAddWorklogOnSubTaskDone": True,
            "isAllowSelfSignedCertificate": False,
            "isUpdateIssueFromLocal": False,
            "isShowComponents": True,
            "isCheckToReAssignTicketOnTaskStart": False,
            "storyPointFieldId": None,
            "isTransitionIssuesEnabled": True,
            "availableTransitions": [],
            "transitionConfig": {"OPEN": "DO_NOT", "IN_PROGRESS": "ALWAYS_ASK", "DONE": "ALWAYS_ASK"},
            "userToAssignOnDone": None
        },
        "GITHUB": {
            "repo": None,
            "token": None,
            "isSearchIssuesFromGithub": False,
            "isAutoPoll": False,
            "isAutoAddToBacklog": False,
            "filterUsername": None
        },
        "GITLAB": {
            "project": None,
            "gitlabBaseUrl": None,
            "token": None,
            "isSearchIssuesFromGitlab": False,
            "isAutoPoll": False,
            "isAutoAddToBacklog": False,
            "filterUsername": None
        },
        "CALDAV": {
            "caldavUrl": None,
            "resourceName": None,
            "username": None,
            "password": None,
            "isAutoAddToBacklog": False,
            "isAutoPoll": False,
            "isSearchIssuesFromCaldav": False,
            "isTransitionIssuesEnabled": False,
            "categoryFilter": None
        }
    },
    "taskIds": [],
    "backlogTaskIds": [],
    "advancedCfg": {
        "worklogExportSettings": {
            "cols": ["DATE", "START", "END", "TIME_CLOCK", "TITLES_INCLUDING_SUB"],
            "roundWorkTimeTo": None,
            "roundStartTimeTo": None,
            "roundEndTimeTo": None,
            "separateTasksBy": " | ",
            "groupBy": "DATE"
        }
    },
    "theme": {
        "isAutoContrast": True,
        "isDisableBackgroundGradient": False,
        "primary": "#29a1aa",
        "huePrimary": "500",
        "accent": "#ff4081",
        "hueAccent": "500",
        "warn": "#e11826",
        "hueWarn": "500",
        "backgroundImageDark": None,
        "backgroundImageLight": None
    },
    "workStart": {"2021-06-06": 1622986726182},
    "workEnd": {"2021-06-06": 1622986728182},
    "breakTime": {"2021-06-06": 300000},
    "breakNr": {"2021-06-06": 1}
}

task_template = {
    "id": "$REQUIRED",
    "projectId": "REQUIRED",
    "subTaskIds": [],
    "timeSpentOnDay": {},
    "timeSpent": 0,
    "timeEstimate": 0,
    "isDone": False,
    "doneOn": None,
    "title": "$REQUIRED",
    "notes": "",
    "tagIds": [],
    "parentId": None,
    "reminderId": None,
    "created": 1622993789204,
    "repeatCfgId": None,
    "plannedAt": None,
    "_showSubTasksMode": 2,
    "attachments": [],
    "issueId": None,
    "issuePoints": None,
    "issueType": None,
    "issueAttachmentNr": None,
    "issueLastUpdated": None,
    "issueWasUpdated": None
}
