from django.test import TestCase
from .models import Employee


class EmployeeTestCase(TestCase):
    def test_create_employee(self):
        data = {
            'firstname' : 'Misha',
            'lastname' : 'Ivanov',
            'birthday' : '1991-12-21',
            'position' : 'staff',
            'education' : 'высшее',
        }
        
        employee = Employee.objects.create(**data)
        self.assertEqual(employee.lastname, 'Ivanov')





def simple_function(text):
    return len(text)

class TestSimpleFunction(TestCase):
    def test_simple_function(self):
        text = 'hello'
        self.assertEqual(simple_function('hello'), 5)
        self.assertGreater(simple_function('hello'), 5)


