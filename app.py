from flask import Flask, render_template_string, request
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Aplicación Flask</title>
    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family: Arial, sans-serif;
        }

        body{
            background: linear-gradient(135deg, #667eea, #764ba2);
            min-height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;
        }

        .container{
            background:white;
            padding:30px;
            border-radius:15px;
            width:400px;
            text-align:center;
            box-shadow:0 10px 25px rgba(0,0,0,.2);
        }

        h1{
            margin-bottom:20px;
            color:#333;
        }

        input{
            width:100%;
            padding:12px;
            margin:10px 0;
            border:1px solid #ccc;
            border-radius:8px;
        }

        button{
            width:100%;
            padding:12px;
            border:none;
            border-radius:8px;
            background:#667eea;
            color:white;
            cursor:pointer;
            font-size:16px;
        }

        button:hover{
            background:#5563d6;
        }

        .resultado{
            margin-top:20px;
            padding:15px;
            background:#f4f4f4;
            border-radius:8px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Aplicación Flask</h1>

    <form method="POST">
        <input type="text" name="nombre" placeholder="Ingrese su nombre" required>
        <button type="submit">Enviar</button>
    </form>

    {% if nombre %}
    <div class="resultado">
        <h3>Hola, {{ nombre }} 👋HolaASDASD </h3>
        <p>Bienvenido a Flask.</p>
    </div>
    {% endif %}
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def inicio():
    nombre = None

    if request.method == "POST":
        nombre = request.form.get("nombre")

    return render_template_string(HTML, nombre=nombre)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)





