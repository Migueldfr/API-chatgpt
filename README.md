1. DockerFile
    
    * Open Docker Desktop to run any command in your terminal, and once you've done that, execute these commands
    
    - Create image:

        * Docker must be installed in our environment

        * Navigate to the path where the Dockerfile is located

        * Build the image in our docker repository with this code

        ``` docker build -t chatbot . ```

        * Execute the image from the Docker repository

        ``` docker run -it --publish 7000:4000 chatbot ```

        * Now we write this location in our browser
        
        ``` localhost:7000 ``` 
       
    - Pull from DockerHub API:

        * Open terminal (VSC or local)

        * Write this code and download the image
        
        ``` docker run -p 7000:4000 -t migueldfr/chatbot ```

        * We write this location in our browser

        ``` localhost:7000 ```
 
2. The executable of our app is where we developed the code to call the ChatGPT API and in turn, we store it in an Amazon Web Services (AWS) database.

    - Functionality of our app: It launches the user's question to the ChatGPT API and returns the response to the screen, with a limit of 500 tokens and using the 'davinci' intelligent text engine. Afterwards, automatically adds the date of the question, the question, and the response to a previously created AWS database.

    - Connection to ChatGPT:

        * You must have a txt file named api_key.txt that includes only the API-key, for the application to function properly. (input in progress)

        * On the home screen, you can enter the question or prompt you want as input, to which the string "Short answer, please" will be added, because we have restricted the call to 500 tokens and we do not want the answer to be cut off.

        * We change the incorrectly recognized characters (accented vowels, tabs, and line breaks) to the correct ones.

        * We convert the entered date, which is the moment the question is asked, to a string format.

    - Connection to AWS Database

        * The database where all questions and answers will be included is located in the notebooks folder, in a file called base_de_datos.ipynb.

        * It contains the database named "PreguntasGPT" and within it, the table where new data will be inserted: "GPT".

        * This table will receive three strings for the "DATE", "QUESTION", and "ANSWER" columns. If you want to access the data, you can do it from the file called base_de_datos.ipynb.

3. Here is a brief description of the development and deployment process of the application:

    - First, we defined the project's objectives and the necessary technical requirements. We wanted to create a web application that would allow users to interact with a chatbot developed with the ChatGPT API. To do this, we needed to design an architecture that would allow us to connect the API with the interface we were going to create.

    - Once we defined the objectives and requirements, we proceeded to design the system's architecture. We considered the components that would make up the application, how they would relate to each other, and how the data would be stored. We designed an architecture based on microservices that would allow us to connect different components independently and scalably.

    - When we had the ChatGPT API working, we proceeded to design and develop the interface built with HTML that would allow users to interact with the chatbot. We focused on creating an intuitive and easy-to-use user interface that would allow users to enter their API key and start interacting with the chatbot.

    - Then, we decided to integrate Docker into our project. Docker is a virtualization tool that allows packaging an application and its dependencies into a container. This way, we could ensure that the application would work identically in any environment, which facilitated the deployment process.

    - Finally, we integrated Amazon Web Services (AWS) into our project to host the application in the cloud. We had to create a database to store the queries made with the response and the time at which the API interaction was made.

    - In summary, our project consisted of designing and developing a web application that would allow users to interact with a chatbot developed with the ChatGPT API. To do this, we defined the system's architecture, developed the ChatGPT API, designed and developed the interface, integrated Docker and Amazon Web Services to host the application in the cloud.

    - As an addition, once we had the interface developed in HTML, we decided to add a touch of CSS to make the app more visually appealing. We thought it would be a good idea to add a field where the user can enter their own API key to make queries.

<h2>Our team</h2>
- [Ramón Fernández](https://github.com/RamonFCerezo)
- [Bogdan Radacina](https://github.com/BogdanBoyan92)
- [Miguel de Frutos](https://github.com/Migueldfr)
