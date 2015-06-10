Django branch database hook
---------------------------

Why
---

This hook work on post-checkout. It reuse or create a copy of the main
database each time you switch branch.

How
---

Let say you are on master and create the branch "testing". A new
database, copy of the base database will be created named
<main_database_name>_testing and used by Django

If you checkout back to master, Django will use your main database, no
more migrations or schemamigrations clashes.

Install
-------

mv django_branch_database/post-checkout .git/hooks/post-checkout
chmod +x .git/hooks/post-checkout

Add this snippet to your setup.py::

    import os
    DATABASE_SETTINGS = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        "<project_path>",
        "settings.py")

changing <project_path> according to your configuration

add django_branch_database_settings.py to your settings

and... that's it!
