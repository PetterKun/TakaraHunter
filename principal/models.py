#encoding:utf-8
from django.db                  import models
from django.contrib.auth.models import User

################################################################################
#										TIPOS DE DATOS
#-------------------------------------------------------------------------------
SEXO = (
         ('h', 'Hombre'),
         ('m', 'Mujer'),
       )
################################################################################
#										CLASE USUARIO
#-------------------------------------------------------------------------------
# Atributos obligatorios de usuario
#
# NOMBRE Y APELLIDO - Ya incluidos en la clase User por defecto
#                     Son first_name y last_name
# SEXO
User.add_to_class('sexo', models.CharField(max_length=1, choices=SEXO, blank=True, verbose_name="Sexo", help_text="Tu sexo."))
# TELEFONO
User.add_to_class('telefono', models.PositiveIntegerField(null=True, blank=True, verbose_name="Número de teléfono", help_text="Tu número de teléfono."))
# DIRECCION (Debería ser una dirección escrita o una coordenada de un mapa?)

# FECHA DE NACIMIENTO
User.add_to_class('fecha_nacimiento', models.DateField(null=True, blank=True, verbose_name="Fecha de nacimiento", help_text="La fecha en que naciste."))
# PROFESION
User.add_to_class('profesion', models.CharField(max_length=30, blank=True, verbose_name="Profesión", help_text="Tu empleo actual."))
# FOTO
User.add_to_class('foto', models.ImageField(upload_to='fotos_usuario', blank=True, verbose_name="Foto", help_text="Tu fotografía."))
