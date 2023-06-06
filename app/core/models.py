from django.db import models
from users.models import User

STATUS_CARGA = (
    ('Pendente', 'Pendente'),
    ('Progresso', 'Progresso'),
    ('Armazenada', 'Armazenada'),
    ('Levantada', 'Levantada'),
)

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    contacto = models.CharField(max_length=15)

class Transportador(Pessoa):
    pass

    def __str__(self) -> str:
        return self.nome
    
class Remetente(Pessoa):
    pass

class Receptor(Pessoa):
    pass
    
class Viatura(models.Model):
    matricula = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.matricula

class Rota(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.descricao 
    
class CategoriaCarga(models.Model):
    descricao = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categorias Carga'

    def __str__(self) -> str:
        return self.descricao
    
class TarifaPeso(models.Model):
    categoria_carga = models.ForeignKey(CategoriaCarga, related_name='tarifa_peso', on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Tarifas por Peso'

    def __str__(self) -> str:
        return self.categoria_carga.descricao

class TarifaVolume(models.Model):
    categoria_carga = models.ForeignKey(CategoriaCarga, related_name='tarifa_carga', on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Tarifas por Volume'

class Servico(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name

class Carga(models.Model):
    codigo = models.CharField(max_length=255)
    descricao = models.TextField()
    valor_comercial = models.DecimalField(max_digits=10, decimal_places=2)
    peso = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    volume = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tarifa_peso = models.ForeignKey(TarifaPeso, on_delete=models.CASCADE, null=True, blank=True)
    tarifa_volume = models.ForeignKey(TarifaVolume, on_delete=models.CASCADE, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    data_partida = models.DateField()
    data_chegada = models.DateField()
    status = models.CharField(max_length=100, choices=STATUS_CARGA)
    remetente = models.ForeignKey(Remetente, on_delete=models.CASCADE)
    receptor = models.ForeignKey(Receptor, on_delete=models.CASCADE)
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE)
    transportador_principal = models.ForeignKey(Transportador, on_delete=models.CASCADE, related_name='transportes_principais')
    viatura_principal = models.ForeignKey(Viatura, on_delete=models.CASCADE, related_name='transportes_principais')
    transportador_secundario = models.ForeignKey(Transportador, on_delete=models.CASCADE, null=True, blank=True, related_name='transportes_secundarios')
    viatura_secundaria = models.ForeignKey(Viatura, on_delete=models.CASCADE, null=True, blank=True, related_name='transportes_secundarios')
    criado_por = models.DateTimeField(auto_now_add=True)
    modificado_por = models.DateTimeField(auto_now=True)



class Notificacao(models.Model):
    carga = models.ForeignKey(Carga, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=50)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.carga.codigo


