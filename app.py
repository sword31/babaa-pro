from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'gizli_anahtar'  # Kendine göre değiştir

messages = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        isim = request.form.get('isim')
        if isim and isim.strip():
            session['isim'] = isim.strip()
            return redirect(url_for('chat'))
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if 'isim' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        metin = request.form.get('message')  # chat.html'deki input name 'message'
        if metin and metin.strip():
            zaman = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            mesaj = {
                'name': session['isim'],
                'text': metin.strip(),
                'time': zaman
            }
            messages.append(mesaj)
            return redirect(url_for('chat'))

    return render_template('chat.html', messages=messages, isim=session['isim'])

@app.route('/logout')
def logout():
    session.pop('isim', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
