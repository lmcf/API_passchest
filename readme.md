# Como crear un entorno virtual python en VSCODE (windows)
Para crear un entorno virtual de Python en Windows, siga estos pasos:

Instale virtualenv: Abra el terminal de comandos de VSCode y escriba "pip install virtualenv" para instalar virtualenv.

Cree una carpeta para el entorno virtual: En VSCode, seleccione "Archivo" -> "Nueva carpeta" y cree una nueva carpeta para su entorno virtual de Python.

Cree el entorno virtual: Abra el terminal de comandos de VSCode y navegue hasta la carpeta que creó en el paso 2. Luego escriba "virtualenv nombre_del_entorno" (reemplace "nombre_del_entorno" con el nombre que desee para su entorno virtual).

Active el entorno virtual: En el terminal de comandos, escriba "nombre_del_entorno\Scripts\activate" (reemplace "nombre_del_entorno" con el nombre que eligió para su entorno virtual).

Verifique la activación del entorno virtual: Una vez que el entorno virtual esté activado, el nombre del entorno virtual aparecerá antes de la ruta en la línea de comandos.

Instale Flask en el entorno virtual: En el terminal de comandos, escriba "pip install flask" para instalar Flask en el entorno virtual.

Verifique la instalación de Flask: Abra un archivo Python en VSCode y escriba "import flask" para verificar que Flask se ha instalado correctamente en el entorno virtual.

Ahora puede usar Flask en su entorno virtual de Python y estar seguro de que las dependencias no afectarán a otros proyectos en su sistema.