Backup Data command for Patients(residents):
    python manage.py dumpdata Patients.IdPatient --format json --indent 4 > Patients/fixtures/PatientData.json