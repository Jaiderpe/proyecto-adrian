import json
import os

MY_DATOS_ESPECIALISTAS = "data/especialistas.json"
MY_DATOS_PACIENTES = "data/pacientes.json"
  
def NewfileEspecialistas(*param):
    with open(MY_DATOS_ESPECIALISTAS, "w") as wf:
        json.dump(param[0],wf,indent=4)

def NewfilePacientes(*param):
    with open(MY_DATOS_PACIENTES, "w") as wf:
        json.dump(param[0],wf,indent=4)

def AddData(*param):
    data =list(param)
    with open(MY_DATOS_ESPECIALISTAS,"r+") as rwf:
        data_file=json.load(rwf)
        if (len(param) > 1):
            data_file[data[0]].update({data[1]:data[2]})
        else:
            data_file.update({param[0]})

        rwf.seek(0)
        json.dump(data_file,rwf,indent=4)

def readfile():
    with open(MY_DATOS_ESPECIALISTAS,'r') as rf:
        return json.load(rf)

def checkfileEspecialistas(*param):
    data = list(param)
    if(os.path.isfile(MY_DATOS_ESPECIALISTAS)):
        if(len(param)):
            data[0].update(readfile())
    else:
        if(len(param)):
            NewfileEspecialistas(data[0])

def checkfilePacientes(*param):
    data = list(param)
    if(os.path.isfile(MY_DATOS_PACIENTES)):
        if(len(param)):
            data[0].update(readfile())
    else:
        if(len(param)):
            NewfilePacientes(data[0])