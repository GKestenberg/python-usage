from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/lag')
def lag():
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    # Calculate fibonacci(35) which takes about 1 second on modern machines
    result = fibonacci(35)
    return f"Fibonacci(35) = {result}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
