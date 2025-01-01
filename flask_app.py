from flask import Flask, request, render_template
import math

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/factorial', methods=['POST'])
def factorial():
    try:
        # Kullanıcıdan sayıyı al
        number = request.form.get('number', type=int)

        if number is None:
            return render_template('index.html', result="Lütfen bir sayı girin!", error=True)

        if number < 0:
            return render_template('index.html', result="Negatif sayılar için faktöriyel tanımlı değildir.", error=True)

        # Faktöriyel hesapla
        result = math.factorial(number)

        return render_template('index.html', result=f"{number}! = {result}", error=False)

    except Exception as e:
        return render_template('index.html', result=f"Bir hata oluştu: {str(e)}", error=True)

if __name__ == '__main__':
    app.run(debug=True)
