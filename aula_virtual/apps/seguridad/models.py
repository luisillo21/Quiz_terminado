from django.db import models

# Create your models here.

class Personas(models.Model):
    ESTADO_CHOICES = [
        ('INACTIVO', 'Inactivo'),
        ('ACTIVO', 'Activo')
    ]

    id_persona = models.AutoField(primary_key=True)
    nombres = models.CharField(null=False, max_length=50,blank=False)
    apellidos = models.CharField(null=False, max_length=50,blank=False)
    cedula = models.CharField(blank=False,null=False,unique=True,max_length=50)
    estado = models.CharField(blank=True,max_length=50,choices=ESTADO_CHOICES,null=True,default='ACTIVO')
    foto = models.ImageField(upload_to='usuarios_avatar',default='default/default_avatar.png')

    class Meta:
        verbose_name ='Persona'
        verbose_name_plural='Personas',
        db_table ='persona'
    
    def __unicode__(self):
        return self.id_persona

    def __str__(self):
        return '{} {} Identificación: {}'.format(self.nombres,self.apellidos,self.cedula)


class Roles(models.Model):
    ESTADO_CHOICES = [
        ('INACTIVO', 'Inactivo'),
        ('ACTIVO', 'Activo')
    ]

    TIPO_CHOICES = [
        ('PROFESOR', 'Profesor'),
        ('ADMINISTRADOR','Administrador'),
        ('ALUMNO', 'Alumno'),
        ('EMPLEADO ADMINITRATIVO', 'Empleado administrativo')
    ]

    id_rol = models.AutoField(primary_key=True)
    rol_nombre = models.CharField(max_length=45,null=False,blank=False,choices=TIPO_CHOICES)
    rol_estado = models.CharField(max_length=45,choices=ESTADO_CHOICES,null= False,blank=False)


    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles',
        db_table = 'rol'
    

    def __unicode__(self):
        return self.id_rol
    
    def __str__(self):
        return self.rol_nombre
    

class Usuario(models.Model):
    
    ESTADO_CHOICES = [
        ('INACTIVO', 'Inactivo'),
        ('ACTIVO', 'Activo')
    ]

    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=45,  blank=False, null=False)
    correo = models.EmailField(blank=True,max_length=80,null=True,default='example@gmail.com')
    clave = models.CharField(max_length=45, blank=False,null=False)
    id_persona = models.ForeignKey(
        Personas, on_delete=models.CASCADE,unique=True,db_column='id_persona')
    rol_usuario = models.ForeignKey(Roles,null=False,blank=False,on_delete=models.CASCADE,db_column='rol_usuario')
    estado = models.CharField(blank=False,max_length=50,choices=ESTADO_CHOICES,null=True,default='ACTIVO')


    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios',
        db_table = 'usuario'

    def __unicode__(self):
        return self.id_usuario

    def __str__(self):
        return self.usuario

class Menu(models.Model):

    ESTADO_CHOICES = [
        ('INACTIVO', 'Inactivo'),
        ('ACTIVO', 'Activo')
    ]

    TIPO_CHOICES = [
        ('PADRE', 'padre'),
        ('HIJO', 'hijo')
    ]

    id_menu = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=False, unique=True, null=False)
    tipo_menu = models.CharField(max_length=45,blank=False,null=False, choices=TIPO_CHOICES)
    menu_padre = models.ForeignKey('self',on_delete=models.SET_NULL,null=True, blank=True, db_column='menu_padre')
    estado = models.CharField(blank=False,max_length=50,choices=ESTADO_CHOICES,null=False)
    orden = models.IntegerField(blank=False, null=False)
    url = models.CharField(blank=False, null=False, max_length=60,default='#')

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'
        db_table = 'menu'
        ordering = ['orden']

    def __str__(self):
        return self.nombre 
    
    
    def __int__(self):
        return self.id_menu
    
    def __int__(self):
        return self.menu_padre

class Permisos(models.Model):

    ESTADO_CHOICES = [
        ('INACTIVO', 'Inactivo'),
        ('ACTIVO', 'Activo')
    ]

    id_permiso = models.AutoField(primary_key=True)
    menu = models.ManyToManyField(Menu, related_name="fk_menu", db_table='permiso_menu')
    rol = models.ForeignKey(Roles, on_delete=models.CASCADE,related_name="fk_rol",unique=True,db_column='id_rol',blank=False, null=False)
    estado = models.CharField(blank=True,max_length=50,choices=ESTADO_CHOICES,null=True,default='ACTIVO')

    class Meta:
        verbose_name = 'Permiso'
        verbose_name_plural = 'Permisos',
        db_table = 'permisos'
    

    def __int__(self):
        return self.id_permiso


