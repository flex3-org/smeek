# Education - AI

This application provides various educational services, including course content generation, chatbot interactions, quiz creation from PDFs, and flashcard generation. It uses LLMs to extract and generate relevant educational materials based on user input.

## Features

1. **Course Content Generation**: 
   - Generates course topics based on a given subject and provides related YouTube links for further learning.

2. **Chatbot Interaction**:
   - Interact with a chatbot to ask any questions related to the course content.

3. **Quiz Creation from PDF**:
   - Upload a PDF, and the application will extract text, split it into chunks, and generate quiz questions based on the content.

4. **Flashcard Generation from PDF**:
   - Upload a PDF, and the application will generate flashcards with key points extracted from the text.

5. **YouTube Video Summarization**:
   - Summarizes the content of a YouTube video based on the provided URL.


## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/flex3-org/education-ai.git
    cd education-ai
    ```
    
2. **Set up and run Ollama locally**:

   - **Install Ollama**: Visit the [Ollama website](https://ollama.com/download) to download and install the appropriate version for your OS.

   - **Pull the Llama3 Model**: After installing Ollama, you need to pull the Llama3 model by running the following command:

     ```bash
     ollama pull llama3
       ```
   - **Start Ollama**: Ensure Ollama is running and accessible at `http://localhost:11434`
    
3. **Create and activate a virtual environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the application**:

    ```bash
    uvicorn main:app --reload
    ```

## API Endpoints

### 1. Course Content Generation
- **Endpoint**: `/coursecontents/`
- **Method**: `GET`
- **Query Parameter**: `topic` (e.g., `"Python"`)
- **Response**: JSON containing a list of topics and corresponding YouTube links.

### 2. Chatbot Interaction
- **Endpoint**: `/chat/`
- **Method**: `POST`
- **Request Body**: JSON containing `user_input` (e.g., `{"user_input": "Explain neural networks"}`)
- **Response**: JSON containing the chatbot's response.

### 3. Quiz Generation from PDF
- **Endpoint**: `/quiz/`
- **Method**: `POST`
- **Request Body**: Upload a PDF file.
- **Response**: JSON containing generated quiz questions.

### 4. Flashcard Generation from PDF
- **Endpoint**: `/flashcards/`
- **Method**: `POST`
- **Request Body**: Upload a PDF file.
- **Response**: JSON containing generated flashcards.

### 5. YouTube Video Summarization
- **Endpoint**: `/summary/`
- **Method**: `GET`
- **Query Parameter**: `url` (e.g., `"https://www.youtube.com/watch?v=dQw4w9WgXcQ"`)
- **Response**: JSON containing the summary of the video.



