from flask import Flask, request, jsonify

app = Flask(__name__)

def fibonacci_series(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci_series():
    n = int(request.args.get('n', default=5))
    fib_series = fibonacci_series(n)
    return jsonify(fib_series)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

