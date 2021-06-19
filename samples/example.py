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

# This script reads the super-productivity-sample and adds as new project
# and additional tasks. The output is then saved and can be imported by
# super productivity.

# A user will be export their super productivity file and use the below
# sample script to programatically add projects and tasks

import os
import sys

# add the root dir to path to allow this script run without
# additional settings to environment variables
current_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(current_dir)
sys.path.insert(0, root_dir)

from productivity import SuperProductivity

project_name = "New Project"
sample_file = "super-productivity-sample.json"
output_file = "super-productivity-sample-output.json"

sp = SuperProductivity(f"{current_dir}/{sample_file}")


sp.add_project(project_name)
sp.add_task("new task 1", project_name)
sp.add_task("new task 2", project_name)
sp.add_task("new task 3", project_name)

sp.write_json(f"{current_dir}/{output_file}")
