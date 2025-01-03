
# import csv
# from django.core.management.base import BaseCommand
# from studentapp.models import Student  # Import your Student model

# class Command(BaseCommand):
#     help = 'Import student data from CSV'

#     def handle(self, *args, **kwargs):
#         with open('students.csv', newline='') as csvfile:
#             reader = csv.DictReader(csvfile)
#             for row in reader:
#                 Student.objects.create(
#                     name=row['name'],
#                     age=row['age'],
#                     email=row['email'],
#                     phone_number=row['phone_number']
#                 )
#         self.stdout.write(self.style.SUCCESS('Successfully imported student data'))


import csv
from django.core.management.base import BaseCommand
from studentapp.models import Student  # Import your Student model

class Command(BaseCommand):
    help = 'Import student data from CSV'

    def handle(self, *args, **kwargs):
        with open('students.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            students = [
                Student(
                    name=row['name'],
                    age=row['age'],
                    email=row['email'],
                    phone_number=row['phone_number']
                ) for row in reader
            ]
            Student.objects.bulk_create(students)  # Bulk insert all records at once
        self.stdout.write(self.style.SUCCESS('Successfully imported student data'))
