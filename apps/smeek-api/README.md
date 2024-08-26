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

### 1. Course Content
- **Endpoint**: `/coursecontents/`
- **Method**: `GET`
- **Parameters**: 
  - `topic`: (str) The subject/topic for which you want to generate course content.
- **Response**:
  - JSON array of topics and YouTube links.

### 2. Chatbot Interaction
- **Endpoint**: `/chatbot/`
- **Method**: `GET`
- **Parameters**:
  - `inp`: (str) The question or input you want to ask the chatbot.
- **Response**:
  - JSON object with the chatbot's response.

### 3. Quiz Creation from PDF
- **Endpoint**: `/quiz/`
- **Method**: `GET`
- **Parameters**:
  - `file`: (UploadFile) The PDF file from which the quiz is generated.
- **Response**:
  - JSON array of quiz questions.

### 4. Flashcard Generation from PDF
- **Endpoint**: `/flashcards/`
- **Method**: `GET`
- **Parameters**:
  - `file`: (UploadFile) The PDF file from which flashcards are generated.
- **Response**:
  - JSON array of flashcards.


