#print("******************************************************")
#print("Curso No. 36 ... Instalacion de Paquetes..." ) 
#print("******************************************************")
from setuptools import setup

setup(name="CalculosMatematicosBasicos",
      version="1.0.0",
      description="Paquete de prueba calculos básicos",
      author="Carlos F. Ramírez Abdalla",
      author_email="carlos_205ram@hotmail.com",
      url="www.CRAneoSoftware.com",
      packages=["Paquetes"]
    )

#Al concluir con lo anterior el archivo se guarda.
#ya guardado el archivo se procede a ejecutar en shell
#la instruccion:
#    python setup.py sdist [enter]    

#para instalar el paquete generado que es extencion .tar.gz
#se tendria que ejecutar la instrucción:
#  pip3 install <nombre del paquete .tar.gt> 

#si se quiere desinstalar el paquete:}
#  pip3 uninstall {nombre del paquete que fue 
#                  colocado en la propiedad name 
#                  del paquete setup}