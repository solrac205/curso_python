from MDVehiculos import Vehiculos
#Los nombres de los modulos siempre los buscará en el directorio donde se encuetra el codigo que importa el Modulo.
#los que no encuentra en el mismo directorio los busca en syspath incluido el path de instalacion de python
#los nombres de los modulos son los nombres de los archivos sin las extenciones las cuales pueden  ser .py
#.pyc(python compilado) y archivos de c también. cuando queremos utilizar modulos fuera de los directorios antes mencionados
#se debera utilizar mediante la creación de paquetes.

miCoche=Vehiculos("Chevrolet","2011")
miCoche.Estado()
