from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            code = ord(char)
            if char.islower():
                result.append(
                    chr(((code - 97 + shift_amount) % 26 + 26) % 26 + 97))
            elif char.isupper():
                result.append(
                    chr(((code - 65 + shift_amount) % 26 + 26) % 26 + 65))
        else:
            result.append(char)
    return ''.join(result)


def caesar_decipher(text, shift):
    # Đảo ngược shift để giải mã
    return caesar_cipher(text, -shift)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/encode', methods=['POST'])
def encode():
    data = request.json
    text = data.get('text')
    shift = int(data.get('shift'))
    encoded_text = caesar_cipher(text, shift)
    return jsonify({'encoded_text': encoded_text})


@app.route('/decode', methods=['POST'])
def decode():
    data = request.json
    text = data.get('text')
    shift = int(data.get('shift'))
    decoded_text = caesar_decipher(text, shift)
    return jsonify({'decoded_text': decoded_text})


if __name__ == '__main__':
    app.run(debug=True)
