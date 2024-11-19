from flask import Flask, request, jsonify

app = Flask(__name__)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    return [x for x in range(2, n+1) if is_prime(x)]

@app.route('/limit', methods=['GET'])
def get_primes():
    try:
        n = request.args.get('n', type=int)
        if n is None:
            return jsonify({"error": "Parameter 'n' is required"}), 400
        if n < 2:
            return jsonify({"message": "There are no prime numbers less than 2"}), 200

        primes = generate_primes(n)
        return jsonify({"primes": primes})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
/* Chinh sua tren server may client */