¡Nuestro equipo de desarrollo esta compuesto por 3 miembros!
- [Ramón Fernández](https://github.com/RamonFCerezo)
- [Bogdan Radacina](https://github.com/BogdanBoyan92)
- [Miguel de Frutos](https://github.com/Migueldfr)

1. DockerFile( imagen )
    
    - Creamos imagen:

        * Tenemos que instalar Docker en nuestro entorno

        * Una vez que lo tenemos ya estamos listos para ejecutar la imagen

        * Construir la imagen en mi crepositorio de Docker

        ``` docker build -t chatbot . ```

        * Ejecutar la imagen desde el repositorio de Docker

        ``` docker run -it --publish 7000:4000 chatbot ```

        * Ahora escribimos esto en nuestra web 'localhost:7000' y ya nos funciona, ya que estamos en el puerto 4000 en nuestro contenedor pero estaremos en el puerto 7000 en nuestro ordenador.
    
    - Pull desde la API DockerHub:

        * Abrimos la terminal tanto VSC o Local

        * Escribimos esto y directamente descargamos la imagen del contenedor 
        
        ``` docker run -p 7000:4000 -t migueldfr/chatbot ```
 
2. Ejecutable de nuestra app donde desarrollamos el codigo para llamar a la API de Chat GPT y a su vez lo llevamos a una BBDD de Amazon Web Services (AWS)

3. Una documentacion de lo mas detallada por si quieres probar tu mismo los entresijos de la misma aplicacion, que sin duda te dejara sin habla.


