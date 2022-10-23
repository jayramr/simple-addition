from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html')
@app.route('/send', methods=['POST'])
def addition():
    if request.method == "POST":
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        sum = float(num1) + float(num2)
        return render_template('index.html', sum=sum)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
