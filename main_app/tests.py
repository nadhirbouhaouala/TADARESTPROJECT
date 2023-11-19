from django.test import TestCase
from .models import *

class TaskTestCase(TestCase):
    def setUp(self):
        Task.objects.create(comment="hello world !")
        Task.objects.create(comment="hello nadhir")

    def test_task_say_hello_to_nadhir(self):
        task = Task.objects.get(id=1)
        self.assertEqual(task.comment, "hello world !")


"""
# Create your tests here.
def test_exemple():
    assert 1 == 1


from django.test import Client



def test_polls():

    client = Client()

    response = client.get('/polls/')

    assert response.status_code == 200

"""

