from flask import Flask, request, send_file, jsonify
from gtts import gTTS
from io import BytesIO

app = Flask(__name__)

@app.route('/generate-voice', methods=['POST'])
def generate_voice():
    try:
        data = request.json
        text_data = data.get('text', '')
        language = data.get('language', 'en')
        accent = data.get('accent', 'com.au')


        if not text_data:
            return jsonify({"error": "No text was provided"}), 400

        text_to_speech = gTTS(text = text_data, lang=language, tld=accent)
        audio_buff = BytesIO()
        text_to_speech.write_to_fp(audio_buff)
        audio_buff.seek(0)

        return send_file(audio_buff, mimetype='audio/mpeg', as_attachment=False, download_name="TextToSpeech.mp3")
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == "__main__":
    app.run()
            