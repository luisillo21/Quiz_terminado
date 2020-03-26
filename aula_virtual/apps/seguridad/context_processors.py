
from .models import *

def permisos(request):
    contexto = {}
    if 'usuario' in request.session:
         contexto = {}
         menu_padre = Menu.objects.filter(tipo_menu = 'PADRE')
         datos_usuarios = Usuario.objects.get(id_usuario = request.session.get('usuario'))

         #pregunto si el usuario es un ALUMNO

         #ANTES DE TRAER LOS PERMISOS VALIDO SI EXISTE ALGUN REGISTRO 
         if Permisos.objects.filter(rol=datos_usuarios.rol_usuario,estado='ACTIVO').exists():
            #TRAIGO LOS PERMISOS QUE TIENE EL USUARIO LOGONEADO SEGUN SU ROL 
            contexto['permisos'] = Permisos.objects.get(rol=datos_usuarios.rol_usuario,estado='ACTIVO')
        #TRAIGO TODOS LOS MENU DE TIPO PADRE
         contexto['lista_padre'] = menu_padre
         #TRAIGO TODOS LOS DATOS DEL USUARIO
         contexto['datos_usuario'] = datos_usuarios
         return contexto
    else:
        return contexto