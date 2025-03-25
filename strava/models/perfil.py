from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, URLValidator
from .base_models import BaseModel
from django.db import models
from strava.enumerations import Genero

class Perfil(BaseModel):
    nome = models.CharField(
        max_length=100, validators=[MinLengthValidator(10)],
        null=False, blank=False,
        help_text="Nome.",
        verbose_name="Nome",
    )

    email = models.EmailField(
        max_length=254, null=False, blank=False, unique=True,
        help_text="E-mail",
        verbose_name="E-mail",        
    )

    generos = models.CharField(
        max_length=10, null=False, blank=False,
        choices=Genero,
        help_text="Genero",
        verbose_name="Genero"
    )

    cpf = models.CharField(
        null=False, blank=False,
        max_length=11, validators=[MinLengthValidator(11)],
        help_text="CPF",
        verbose_name="CPF",
    )
    senha = models.CharField(
        null=False, blank=False,
        max_length=20, validators=[MinLengthValidator(5)],
        help_text="Senha",
        verbose_name="Senha",
    )

    data_nascimento = models.DateField(
        null=False, blank=False,
        help_text="Data de Nascimento.",
        verbose_name="Data de Nascimento"   
    )

    local = models.CharField(
        null=False, blank=False,
        max_length=100, validators=[MinLengthValidator(3)],
        help_text="Cidade",
        verbose_name="Cidade",
        
    )

    pais = models.CharField(
        null=False, blank=False,
        max_length=100, validators=[MinLengthValidator(3)],
        help_text="País",
        verbose_name="País",
        
    )

    peso = models.FloatField(
        null=False, blank=False,
        validators=[MinValueValidator(20)],
        help_text="Peso",
        verbose_name="Peso",
        
    )

    pagina_pessoal = models.URLField(
        null=False, blank=False,
        validators=[URLValidator(), MinLengthValidator(15)],
        max_length=150,
        help_text="Página Pessoal",
        verbose_name="Página Pessoal",
        
    )

    biografia = models.TextField(
        null=False, blank=True,
        help_text="Biografia - Campo Opicional",
        verbose_name="Biografia",
    )

    premium = models.BooleanField(
        null=False, blank=False,
        default=False,
        help_text="Premiun",
        verbose_name="Conta Premiun"
    )

    membro_desde = models.DateField(
        null=False, blank=False,
        auto_now_add=True, 
    )
   
    def __str__ (self):
        return f"{self.email}, {self.nome}, {self.cpf}, {self.data_nascimento}, {self.local} - {self.pais}, {self.generos}, {self.peso}, {self.membro_desde}, {self.premium}"
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"
        