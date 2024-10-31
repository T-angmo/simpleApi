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
# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route('/mul5/<a>')
# def mul5(a):
#         number = float(a)
#         return str(number * 5)


from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/power/<a>/<b>')

def power(a, b):
        number1 = float(a)
        number2 = float(b)
        num = number1**number2
        return str(num)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



