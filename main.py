import modules.corefiles as cf
import funciones.globales as fg
import funciones.especialistas as st
import funciones.paciente as fp

def mainmenu(op):
   fg.borrar_pantalla()
   tittle = """
   *************
   ** CENTRO CLINICO  ****
   *************
   """   
   mainmenuop = "1. tipos de especialistas\n2. datos de pacientes\n3. historial clinico\n4. salir"
   if (op !=4):
      print(tittle)
      print(mainmenuop)
      try:
         opcion = int(input('~ '))
      except ValueError:
         input("Error en la opcion ingresada")  
         fg.pausar_pantalla
         mainmenu(0)
      else:
         match(opcion):
            case 1:
               st.NewSpecialista()
            case 2:
               fp.newpaciente()
            case 3:
               pass
            case 4:
               print("hasta luego")
               fg.pausar_pantalla()
            case _:
               print("opcion no valida")
               fg.pausar_pantalla
               mainmenu(0)
if __name__=='__main__':
   cf.checkfileEspecialistas(fg.CentroMedicoEspecialistas)
   cf.checkfilePacientes(fg.CentroMedicoPacientes)
   cf.MY_DATOS_ESPECIALISTAS = 'data/especialistas.json'
   cf.MY_DATOS_PACIENTES = 'data/pacientes.json'
   mainmenu(0)

