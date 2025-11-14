from django.test import TestCase
from .models import Tarefa
class TarefaModelTest(TestCase):
    def test_create_tarefa(self):
        t = Tarefa.objects.create(titulo='Teste', descricao='Desc')
        self.assertEqual(str(t), 'Teste')
