import os
import json
import funciones.globales as gf
import modules.corefiles as cf
import main


def newpaciente():
        gf.borrar_pantalla()
        title = """

        ***************************
        *  REGISTRO DE PACIENTES  *
        ***************************
        """
        gf.borrar_pantalla
        print(title)
        identificacion = input("ingrese el numero de identificacion : ")
        nombredelpaciente = input("ingrese su nombre :")
        phone = input("ingrese el numero de telefono :")
        fecha = input("ingrese la fecha de nacimiento")
        edad = input("ingrese la edad")
        genero = input("ingrese el genero")
        pacient = {
                "identificaacion" : identificacion,
                "nombredelpaciente" : nombredelpaciente,
                "phone" : phone,
                "fecha" : fecha,
                "edad": edad,
                "genero": genero,
                "fecha": {
                "dia":{},
                "mes":{},
                "año":{}
                }
        }
        cf.AddData("dataPacientes",identificacion,pacient)
        gf.CentroMedicoPacientes.get("dataPacientes")
        if(bool(input("desea ingresar otro paciente s(si) o enter(no)"))):
          newpaciente(0)
        else:
         main.mainmenu(0)
