¡Nuestro equipo de desarrollo esta compuesto por 3 miembros!
- [Ramón Fernández](https://github.com/RamonFCerezo)
- [Bogdan Radacina](https://github.com/BogdanBoyan92)
- [Miguel de Frutos](https://github.com/Migueldfr)

1. DockerFile( imagen )
    
    * Abrir el DockerDesktop para ejecutar cualquier comando en nuestro terminal (ya que si no lo abres, no funcionan los comandos), y una vez asi, ejecutar estos comandos.
    
    - Creamos imagen:

        * Tenemos que instalar Docker en nuestro entorno

        * Una vez que lo tenemos ya estamos listos para ejecutar la imagen

        * Dirigirnos al Path donde esta el Dockerfile

        * Construir la imagen en mi crepositorio de Docker

        ``` docker build -t chatbot . ```

        * Ejecutar la imagen desde el repositorio de Docker

        ``` docker run -it --publish 7000:4000 chatbot ```

        * Ahora escribimos esto en nuestra web 'localhost:7000' y ya nos funciona, ya que estamos en el puerto 4000 en nuestro contenedor pero estaremos en el puerto 7000 en nuestro ordenador.
    
    - Pull desde la API DockerHub:

        * Abrimos la terminal tanto VSC o Local

        * Escribimos esto y directamente descargamos la imagen del contenedor DockerHub
        
        ``` docker run -p 7000:4000 -t migueldfr/chatbot ```
 
2. Ejecutable de nuestra app donde desarrollamos el codigo para llamar a la API de ChatGPT y a su vez lo llevamos a una BBDD de Amazon Web Services (AWS)

    - Funcionalidad de nuestra app: lanza la pregunta del usuario a la API de ChatGPT, y devuelve por pantalla la respuesta de la misma, con un límite de 500 tokens, y el motor de texto inteligente 'davinci'. Después, de forma automática, añade la fecha de la pregunta, la pregunta y la respuesta a una base de datos en AWS previamente creada para ello.

    - Conexión a ChatGPT:

        * Deberás tener un archivo txt de nombre api_key.txt que incluya sólo la clave API-key, para que la aplicación funcione correctamente. (*input en elaboración*)

        * En la pantalla inicial o home, podrás introducir como input la pregunta o prompt que quieras, a la que se le añadirá el string "Respuesta corta, por favor", porque tenemos restringida la llamada a 500 tokens y no queremos que la respuesta quede a la mitad.

        * Cambiamos los caracteres no reconocidos correctamente (vocales acentuadas, tabulaciones y saltos de línea), por los correctos.

        * Pasamos la fecha introducida, la del momento en que se lleva a cabo la pregunta, a formato string.

    - Conexión a la BBDD en AWS

        * La base de datos en la que se van a incluir todas las preguntas y respuestas se encuentra en la carpeta notebooks, en un archivo llamado base_de_datos.ipynb.

        * En ella, se encuentra la base de datos llamada "PreguntasGPT", y dentro de la misma, la tabla en la que se van a insertar los datos nuevos: "GPT".

        * Dicha tabla recibirá tres strings para las columnas "FECHA", "PREGUNTA", "RESPUESTA". Si quieres acceder a los datos puedes hacerlo desde el archivo llamado base_de_datos.ipynb

3. Una documentacion de lo mas detallada por si quieres probar tu mismo los entresijos de la misma aplicacion, que sin duda te dejara sin habla.


