from django.db import models
from django.contrib.auth.models import AbstractBaseUser #edicion o sobrescritura del modelo usuario predeterminado
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager para perfiles de usuario """
    
    def create_user(self, email, name, password=None):
        """Crear Nuevo User Profile """
        
        if not email:
            raise ValueError('Usuario debe tener un email')
        
        email = self.normalize_email

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Modelo Base de datos para usuario en el sistema"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default= False) 
    
    #Modo manager para los objetos
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRES_FIELD = ['name']
    
    def get_full_name(self):
        """Obtener nombre completo"""
        return self.name
    
    
    def get_short_name(self):
        """Obtener nombre corto del usuario"""
        return self.name
    
    def __str__(self):
        """Retornar cadena Representando Nuestro Usario"""
        return self.email