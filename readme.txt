Preparación del ambiente para MisEstacionamientos:
a. Opcional, actualizar gestores de paquetes y librerias base del entorno.
actualizar conda:
conda update conda --yes

actualizar pip:
python -m pip install --upgrade pip


Cargar librerias base (autopep y flake8)
cargar linters y formateadores.
pip install -r base-requirements.txt

- verificar que los paquetes base fueron instalados con: 
conda list

b. crear el ambiente virtual.
conda create --name misEstacionamientos python=3.7 --yes

c. activar el ambiente virtual.
conda activate misEstacionamientos

d. Cargar las librerías necesarias, se debe estar dentro del ambiente virtual.
pip install -r requirements.txt

e. desactivar el ambiente virtual.
conda deactivate

f. Eliminar el ambiente virtual, primero debe desactivarlo antes de eliminar.
conda remove --yes --name misEstacionamientos --all

