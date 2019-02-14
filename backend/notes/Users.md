Backup command for Users(auth):
    python manage.py dumpdata users.User --format json --indent 4 > users/fixtures/UserData.json