from .views import *
from django.urls import path

urlpatterns = [

#-- Url de PERMISOS   eliminar_permiso
    path('opciones/',Opcion,name='opciones'),
    path('agregar_opciones/',AddOpciones.as_view(),name='agregar_opciones'),
    path('edit_opciones/<int:pk>',EditOpciones.as_view(),name='editar_opciones'),
    path('eliminar_opciones/<int:id>/',eliminar_opciones,name='eliminar_opciones'),

    path('preguntas/', Preguntas, name='preguntas'),
    path('agregar_preguntas/', Addpreguntas.as_view(), name='agregar_preguntas'),
    path('edit_preguntas/<int:pk>', EditPreguntas.as_view(), name='editar_preguntas'),
    path('eliminar_preguntas/<int:id>/', eliminar_preguntas, name='eliminar_preguntas'),

    path('examenes/', Examenes, name='examenes'),
    path('agregar_examenes/', AddExamenes.as_view(), name='agregar_examenes'),
    path('edit_examenes/<int:pk>', EditExamenes.as_view(), name='editar_examenes'),
    path('eliminar_examenes/<int:id>/', eliminar_examenes, name='eliminar_examenes'),


#--Realizar evaluacion
    path('realizar_examen/<int:id>',realizar_examen,name='realizar_examen'),
]