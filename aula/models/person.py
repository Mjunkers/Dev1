import random
import string
from .base_model import BaseModel
from django.db import models
from django.core.validators import MinLengthValidator
from aula.validators.funcoes import validate_par
from aula.validators.cod import CodValidator
from django.core.exceptions import ValidationError

class Person(BaseModel):
    cod = models.CharField(max_length=10,
                           validators=[MinLengthValidator(10),
                                       CodValidator("4444444444"), 
                                       validate_par],
                            blank=True
                            
                            )
    
    nome = models.CharField(
        validators=[MinLengthValidator(10)], max_length=50,
        null=False, blank=False,
        help_text="Nome",
        verbose_name="Nome",

    )

    data_aniversario = models.DateField(
        null=False, blank=False,
        help_text="Data de Anivesário",
        verbose_name="Data de Aniversário",
        
    )

    cpf = models.CharField(
        validators=[MinLengthValidator(11)], max_length=11,
        null=False, blank=False,
        help_text="CPF",
        verbose_name="CPF",
    )

    #def __str__(self):
       # f"{self.cod}, {self.nome}, {self.data_aniversario}, {self.cpf}"


    def save(self, *args, **kargs):
        if self.cod is None or self.cod =='':
            letters = string.ascii_letters + string.digits
            self.cod = ''.join(random.choice(letters) for i in range(10))
        super().save(*args, **kargs)


    def clean(self):
        if not isinstance (str(self.nome), str):
            raise ValidationError (
                {"nome": "Nome informado é do tipo errado"},
                code="error001"
            )
        
        elif self.nome == "Teste":
            raise ValidationError(
                {"nome": "não é possível salvar testes!"},
                code="error002"
            )
        
        elif self.cod == "1111111111" and self.nome == "IFRS Restinga":
            raise ValidationError(
                {"nome": "Combinação de nome e código errada!",
                 "cod": "Combinação de nome e código errada!"},
                 code="error0101"
            )