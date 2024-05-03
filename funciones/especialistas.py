import os
import json
import funciones.globales as fg
import modules.corefiles as cf
import main

def NewSpecialista():
  title = """
  ***************************
  * REGISTRAR ESPECIALISTA *
  ***************************
  """ 
  
  fg.borrar_pantalla()
  print(title)
  identificacion = input('ingrese tu especialidad como doctor en :')
  codespecia = input('ingrese numero de indentificacion  : ')
  nombreesp = input('ingrese tu  nombre :')
  correoim = input('ingrese correo gmail :')
  numconsul= input('ingrese numero de tu con sultorio ')
  horacon= input('ingrese horario de consulta  (mñ) , (td)')
  especialista = {
    'identificacion':identificacion,
    'codespecia' : codespecia,
    'nombreesp':nombreesp,
    'correoim' :correoim,
    'numconsul' :numconsul,
    'horacon' :horacon,
    'fronada': {
    'mñ':{},
    'td':{}
    }
  }
  cf.AddData("dataEspecialistas",identificacion,especialista)
  fg.CentroMedicoEspecialistas.get("dataEspecialistas")
  if(bool(input("desea ingresar otro pspecialista s(si) o enter(no)"))):
    NewSpecialista(0)
  else:
    main.mainmenu(0)

