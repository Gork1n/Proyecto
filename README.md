# Proyecto Orgstock

Es una aplicación, en un principio creada en la diplomatura de Python, pero que seguí desarrollando para aprender e interiorizar los conceptos del mismo. Consiste en un cliente creado con Tkinter/Flet que permite ver el stock en una tabla y modificarlo a conveniencia. Este se conecta con un servidor socket que almacena toda su información en la base de datos SQLite usando el ORM peewee. El servidor acepta múltiples clientes al mismo tiempo y estos se actualizan en sincronía.


## Instrucciones para iniciar el programa

1. Crear el entorno virtual: python -m virtualenv venv
2. Iniciar el virtual enviroment: .\venv\Scripts\activate
3. Por último, instalar los requirements: pip install -r requirements.txt

## Errores comunes al iniciarlo

1. No tener permitido la ejecución de scripts en powershell: 
  * Iniciar Powershell como administrador
  * scribir Set-ExecutionPolicy Unrestricted
  * Elegir la opcion Si

1. First list item
   - First nested list item
     - Second nested list item

