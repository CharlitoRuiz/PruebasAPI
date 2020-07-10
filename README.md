# PruebasAPI
Dos ejemplos en Js y Python para probar API

Dos ejemplos sencillos para poder probar nuestras API

Python:

Instalar Python 3 (asegurarse de que en la variable de ambiente de Windows, el path quede de la siguiente manera: C:\Users\NombreUsuario\AppData\Local\Programs\Python\Python38\)

Instalar PyCharm CE 

En la consola de Python o el cmd de Windows, instalar Pytest

pip install pytest

Instalar el repositorio de request:

pip install -U requests

Para ejecutar nuestras pruebas:\n
pytest test\test.py -s (importante: cambiar por la ruta deseada)


Javascript:

Instalar NodeJS (asegurarse de que en la variable de ambiente de Windows, el path quede de la siguiente manera: C:\Users\NombreUsuario\AppData\Roaming\npm)

Usar el editor de su preferencia para abrir el proyecto, yo recomiendo VS Code, pero puede usarse Atom, Sublime, etc.


Si se abre el proyecto con VS Code, abrir una terminal y escribir en la raiz del proyecto abierto: 

npm install (para que instale las dependencias)

La manera mas sencilla de correr las pruebas, es nombrar el archivo como test.js y en la consola de VS Code ejecutar:

test/mocha (el folder test va a depender del usuario)


Si quieren ejecutarlo en el CMD de Windows o CMD de NodeJS, abrir una terminal y escribir en la raiz del proyecto abierto: 

npm install (para que instale las dependencias)

La manera mas sencilla de correr las pruebas, es nombrar el archivo como test.js y en la consola ejecutar:

test/mocha (el folder test va a depender del usuario)

