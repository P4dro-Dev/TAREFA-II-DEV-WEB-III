from django.test import TestCase
from .models import Tarefa

class TarefaModelTest(TestCase):
    def setUp(self):
        Tarefa.objects.create(titulo="Teste", descricao="Descrição de teste", concluida=False)

    def test_tarefa_criada_com_sucesso(self):
        tarefa = Tarefa.objects.get(titulo="Teste")
        self.assertEqual(tarefa.descricao, "Descrição de teste")
        self.assertFalse(tarefa.concluida)
