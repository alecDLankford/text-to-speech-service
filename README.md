# Text To Speech Service

## Description

This is a simple Flask web service that converts text to speech using the Google Text-to-Speech (gTTS) library. The service accepts a POST request with a JSON payload containing the text to be converted, and returns the generated speech as an audio stream in MP3 format.

## Features

- Convert text to speech using the gTTS library.
- Support for different languages and accents.
- Returns audio as a byte stream without saving files on the server.

## Requirements

- Python 3.7+
- Flask
- gTTS

## Installation

1\. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/flask-text-to-speech.git
   cd flask-text-to-speech
   ```
2\. **Install the required packages:**

  ```bash
  pip install -r requirements.txt
  ```
   
## Usage

1\. **Start the Flask Server:**

```bash

   python app.py

```
  By default, the application will run on http://127.0.0.1:5000/.

2\. **Send a POST request to generate voice:**

   - Open your browser or use a tool like `curl` or `Postman` to make a GET request:

## Examples

- **Example Request:**

```bash

  curl -X POST http://127.0.0.1:5000/generate-voice \
  -H "Content-Type: application/json" \
  -d '{"text": "It'\''s sunny today in Sydney with a high of 25 degrees Celsius.", "language": "en", "accent": "com.au"}' \
  -o TextToSpeech.mp3

```

## Bug Reporting

If you come across any bugs, please feel free to open an issue.


## Contact Information

For any questions or feedback, please contact Alec Lankford (alec.d.lankford@gmail.com).
