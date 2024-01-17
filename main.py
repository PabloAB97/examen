from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        name = request.form['nombre']
        age = int(request.form['edad'])
        bote = int(request.form['tarros'])
        total = bote * 9000
        dscto1 = total - (total* 0.15)
        descto2 =total - (total * 0.25)
        return render_template('ejercicio1.html', nombre=name, edad=age, tarros=bote, total=total, descuento1=dscto1, descuento2=descto2)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        name2 = request.form['nombre2']
        password = request.form['contraseña']
        return render_template('ejercicio2.html', nombre2=name2, contraseña=password)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True, port=9000)