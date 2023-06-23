from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    matricula = models.IntegerField()
    data_criacao = models.DateField(auto_now_add=True)
    # esse "Auto_now_Add" ele cria automaticamente a data de registro/matricula do aluno

    class Meta:
        verbose_name_plural = "Alunos"
    
    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    professor = models.CharField(max_length=255)
    avaliacao = models.TextField()
    nota = models.DecimalField(max_digits=3, decimal_places=1)
    data_criacao = models.DateField(auto_now_add=True)
    # esse "Auto_now_Add" ele cria automaticamente a data de registro/matricula do aluno

    class Meta:
        verbose_name_plural = "Avaliações"
        unique_together = ['professor', 'aluno']
        #esse "Unique_Together" serve para ele fazer uma validação de campos (no caso ali são dois) para que o professor não repita a mesma avalicao do mesmo aluno duas vezes
    
    def __str__(self):
        return self.avaliacao
