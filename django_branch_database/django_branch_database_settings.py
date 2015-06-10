import setup
import os
import imp
import settings

file_path = os.path.join(
    os.path.dirname(os.path.abspath(setup.__file__)),
    "branch_settings.py")

if os.path.exists(file_path):
    branch_settings = imp.load_source('branch_settings', file_path)
    for alias, database in settings.DATABASES.iteritems():
        if hasattr(branch_settings, alias):
            database["NAME_OLD"] = database["NAME"]
            database["NAME"] = getattr(branch_settings, alias)
