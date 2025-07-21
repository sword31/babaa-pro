from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

messages = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mesaj = request.form.get('mesaj')
        if mesaj:
            zaman = datetime.datetime.now().strftime('%H:%M')
            messages.append(f"{zaman} - {mesaj}")
        return redirect(url_for('index'))
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
