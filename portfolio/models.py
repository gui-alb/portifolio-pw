from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=5)
    universidade = models.CharField(max_length=100)
    duracao_anos = models.CharField(max_length=1)

    def __str__(self):
        return self.nome

class UC(models.Model):
    nome = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=5)
    semestre = models.CharField(max_length=1)
    ano =models.IntegerField()

    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    areas = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)

    unidade_curriculares = models.ManyToManyField(UC, related_name='tecnologias_usadas')

    def __str__(self):
        return self.nome

class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)


    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)

    unidade_curricular = models.ForeignKey('UC', on_delete=models.DO_NOTHING, null=True)
    tecnologias = models.ManyToManyField(Tecnologia)
    competencia = models.ManyToManyField(Competencia, related_name='projeto')

    def __str__(self):
        return self.nome

class Formacao(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    data = models.DateField()

    competencias = models.ManyToManyField(Competencia, related_name='formacao')

    def __str__(self):
        return self.titulo

class TFC(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    rating = models.IntegerField()
    autores = models.CharField(max_length=200)
    orientadores = models.CharField(max_length=200)
    tecnologias = models.CharField(max_length=200)
    areas = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='tfcs/')
    imagem = models.ImageField(upload_to='tfcs/', null=True, blank=True)
    keyWords = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.titulo


class ContribuicaoOpenSource(models.Model):
    nome_projeto = models.CharField(max_length=100)
    descricao_projeto = models.CharField(max_length=250)
    descricao_contribuicao = models.CharField(max_length=500)
    link_repo = models.CharField(max_length=250)

    tecnologia = models.ManyToManyField(Tecnologia)

    def __str__(self):
        return self.nome_projeto