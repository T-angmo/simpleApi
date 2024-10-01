# from flask import Flask, jsonify

# app = Flask(__name__)

# # @app.route('/getcode')
# # def getcode():
# #     return '6969 111'

# # @app.route('/plus/<int:a>/<int:b>')
# # def plus(a, b):
# #     return str(a + b)

# @app.route('/is_prime/<int:a>')
# def is_prime(a):
#     if a <= 1:
#         return False
#     for i in range(2, int(a ** 0.5) + 1):
#         if a % i == 0:
#             return False
#     return True

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/is_prime/<int:a>')
def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
