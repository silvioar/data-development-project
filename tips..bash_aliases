#!/bin/bash

# install python
sudo yum update -y
sudo yum install python3 -y

# Creo la carpeta project
mkdir project

# create venv and activate
python3 -m venv python_env
source python_env/bin/activate

#Install git in your EC2 instance
sudo yum install git -y

# Clono el codigo de github que pushee antes (la primera vez que lo meto a la VM)
git clone https://github.com/silvioar/project.git

# Para ir actualizando eso, git pull


##############
# Crear localhost con SQLectron --> Me anduvo con SQLite
#############
Para crear el localhost en sqlectron, tuve que ponerlo en SQLite y luego crear un archivo .db y llamarlo en los settings de sqlectron.com

Dentro del entorno virtual de la VM, instalar los paquetes: pip install -r requirements.txt

salir de crontab = esc + q!

Pegar en el crontab = Shift+right mouse click

PBI : 82SA36321831@campus.economicas.uba.ar 61092
https://app.powerbi.com/groups/me/reports/d1e356d3-0233-44e8-8942-c3c7af03e671?ctid=4c818f79-ab84-4552-9b7c-2fe715b0d0d5&pbi_source=linkShare