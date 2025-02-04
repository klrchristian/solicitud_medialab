from flask import Flask, request, send_file, render_template, redirect, url_for
import pdfkit
import base64
from datetime import datetime

app = Flask(__name__)

def read_css_file():
    """Lee el archivo CSS y devuelve su contenido."""
    with open('styles.css', 'r', encoding='utf-8') as file:
        return file.read()

def encode_image_to_base64(image_path):
    """Convierte una imagen a base64."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def generate_pdf_filename():
    """Genera un nombre de archivo PDF con la fecha y hora actual."""
    now = datetime.now()  # Obtener la fecha y hora actual
    filename = now.strftime("%Y-%m-%d_%H-%M_solicitud-medialab.pdf")  # Formatear la fecha y hora
    return filename

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Obtener datos del formulario
        fSolicitud = request.form['fSolicitud']
        depto = request.form['depto']
        nombreSolicita = request.form['nombreSolicita']
        numTelefono = request.form['numTelefono']
        email = request.form['email']
        fechaEvento = request.form['fechaEvento']
        horaInicio = request.form['horaInicio']
        horaFin = request.form['horaFin']
        ubicacionEvento = request.form['ubicacionEvento']
        nombreEvento = request.form['nombreEvento']
        observaciones = request.form.get('observaciones', '')  # Campo nuevo
        options = request.form.getlist('options[]')

        # Obtener opciones adicionales para todas las opciones
        additional_options = {}
        for i in range(1, 10):  # Para opciones 1-9
            option_key = f'option{i}'
            if option_key in options:
                additional_options[option_key] = request.form.getlist(f'{option_key}[]')

        # Leer el archivo CSS
        css_content = read_css_file()

        # Convertir la imagen a base64
        logo_base64 = encode_image_to_base64('Galileo_300px.png')

        # Actualizar la generación del HTML para incluir observaciones
        html = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Solicitud de Servicios</title>
            <style>
                {css_content}
                .table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-bottom: 20px;
                }}
                .table th, .table td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }}
                .table th {{
                    background-color: #f2f2f2;
                }}
                .table ul {{
                    margin: 0;
                    padding-left: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <div class="title">
                    <h1>Solicitud de Servicios</h1>
                    <h2>Medialab Universidad Galileo</h2>
                </div>
                <img src="data:image/png;base64,{logo_base64}" alt="Logo">
            </div>
            <div class="content">
                <h3>Datos del Solicitante</h3>
                <p><strong>Fecha de Solicitud:</strong> {fSolicitud}</p>
                <p><strong>Nombre del Departamento:</strong> {depto}</p>
                <p><strong>Nombre:</strong> {nombreSolicita}</p>
                <p><strong>Número de Teléfono:</strong> {numTelefono}</p>
                <p><strong>Correo:</strong> {email}</p>
                
                <h3>Datos del Evento</h3>
                <p><strong>Fecha del Evento:</strong> {fechaEvento}</p>
                <p><strong>Hora de Inicio:</strong> {horaInicio}</p>
                <p><strong>Hora de Finalización:</strong> {horaFin}</p>
                <p><strong>Ubicación del Evento:</strong> {ubicacionEvento}</p>
                <p><strong>Nombre del Evento:</strong> {nombreEvento}</p>
                
                <h3>Observaciones</h3>
                <p>{observaciones}</p>

                <h3>Servicios Solicitados</h3>
                <table class="table">
                    <thead>
                        <tr>
                            <th>Servicio</th>
                            <th>Opciones Adicionales</th>
                        </tr>
                    </thead>
                    <tbody>
                    """

        # Mapeo de nombres de servicios
        service_names = {
            'option1': 'Transmisión en vivo (Público)',
            'option2': 'Opción 2',
            'option3': 'Opción 3',
            'option4': 'Opción 4',
            'option5': 'Opción 5',
            'option6': 'Opción 6',
            'option7': 'Opción 7',
            'option8': 'Opción 8',
            'option9': 'Opción 9'
        }

        for option in options:
            html += f"""
                <tr>
                    <td>{service_names.get(option, option)}</td>
                    <td>
                        <ul>
            """
            for additional in additional_options.get(option, []):
                html += f"<li>{additional}</li>"
            html += """
                        </ul>
                    </td>
                </tr>
            """

        html += """
                    </tbody>
                </table>
            </div>
        </body>
        </html>
        """

        # Generar nombre del archivo PDF con fecha y hora
        pdf_file = generate_pdf_filename()

        # Crear el PDF
        pdfkit.from_string(html, pdf_file)

        # Enviar PDF al cliente
        return send_file(pdf_file, as_attachment=True)
    except Exception as e:
        return str(e), 400

# Manejar acceso directo a /submit con GET
@app.route('/submit', methods=['GET'])
def handle_get_submit():
    return redirect(url_for('index'))  # Redirigir a la página principal

if __name__ == '__main__':
    app.run(port=5000)