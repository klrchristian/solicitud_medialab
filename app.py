from flask import Flask, request, send_file, render_template, redirect, url_for
import pdfkit
import base64
from datetime import datetime
import io

app = Flask(__name__, 
           static_url_path='/solicitud/static', 
           static_folder='static')

# Configuración de pdfkit - Ajusta la ruta según tu sistema
path_wkhtmltopdf = r'/usr/bin/wkhtmltopdf'  # Ruta en sistemas Linux
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

def read_css_file():
    """Lee el archivo CSS y devuelve su contenido."""
    with open('static/assets/css/styles.css', 'r', encoding='utf-8') as file:
        return file.read()

def encode_image_to_base64(image_path):
    """Convierte una imagen a base64."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def generate_pdf_filename():
    """Genera un nombre de archivo PDF con la fecha y hora actual."""
    now = datetime.now()
    filename = now.strftime("%Y-%m-%d_%H-%M_solicitud-medialab.pdf")
    return filename

@app.route('/solicitud')
def index():
    return render_template('index.html')

@app.route('/solicitud/submit', methods=['POST'])
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

        # Convertir las imágenes a base64
        logo_base64 = encode_image_to_base64('Galileo_300px.png')
        mlab_logo_base64 = encode_image_to_base64('mlab_300px.png')

        # Actualizar la generación del HTML para incluir observaciones
        html = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Solicitud de Servicios</title>
            <style>
                {{ css_content }}

                /* Eliminar márgenes predeterminados */
                @page {{
                    margin: 0;
                }}

                body {{
                    margin: 0;
                    padding: 50px;
                    font-family: 'Arial', sans-serif;
                    background-color: #FFFFFF;
                    color: #2C2C2C;
                    line-height: 1.6;
                }}

                /* ===== Header Optimizado ===== */
                .header {{
                    background-color: #FFFFF;  /* Cambiar el negro sólido por un gris claro */
                    color: #1C1C1C;            /* Texto en gris oscuro para contraste */
                    padding: 15px;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    border: 2px solid #BFA980;  /* Borde sutil en lugar de fondo oscuro */
                    border-radius: 8px;
                }}

                .header-table {{
                    width: 100%;
                    border-collapse: collapse;
                    text-align: center;
                }}

                .logo {{
                    width: 80px;
                    height: auto;
                }}

                .logo.ug {{
                    width: 110px;
                    height: auto;
                }}

                .title {{
                    text-align: center;
                    flex-grow: 1;
                }}

                .title h1 {{
                    margin: 0;
                    font-size: 26px;
                    color: #BFA980;             /* Acento dorado suave */
                    letter-spacing: 1px;
                }}

                .title h2 {{
                    margin: 5px 0 0;
                    font-size: 10px;
                    font-weight: normal;
                    color: #4A4A4A;             /* Gris medio en lugar de blanco */
                }}

                /* ===== Contenido General ===== */
                .content {{
                    background: #FFFFFF;
                    padding: 15px;
                    border-radius: 8px;
                    box-shadow: none;            /* Sin sombras para impresión */
                    border: 1px solid #B0B0B0;
                    margin-top: 10px;
                }}

                h3 {{
                    border-bottom: 2px solid #BFA980;
                    padding-bottom: 5px;
                    margin-bottom: 10px;
                    color: #1C1C1C;
                }}

                p {{
                    margin: 5px 0;
                }}

                ul {{
                    margin: 0;
                    padding-left: 20px;
                }}

                /* ===== Tablas ===== */
                .table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 15px;
                }}

                .table th, .table td {{
                    border: 1px solid #B0B0B0;
                    padding: 10px;
                    text-align: left;
                }}

                .table th {{
                    background-color: #EAEAEA;  /* Gris claro en lugar de negro */
                    color: #1C1C1C;             /* Texto en gris oscuro */
                }}

                .table tr:nth-child(even) {{
                    background-color: #FFFFFF;  /* Alternancia suave para legibilidad */
                }}

                /* ===== Observaciones ===== */
                .observaciones {{
                    background-color: #F9F9F9;
                    border: 1px dashed #BFA980;
                    padding: 15px;
                    margin-top: 15px;
                    border-radius: 5px;
                }}

                /* ===== Diseño Horizontal ===== */
                .horizontal-container {{
                    display: flex;
                    gap: 20px;
                    flex-wrap: wrap;
                }}

                .horizontal-container > div {{
                    flex: 1;
                    min-width: 200px;
                }}
            </style>

        </head>
        <body>
            <div class="header">
            <table class="header-table">
                <tr>
                <td class="logo-cell">
                    <img class="logo ug" src="data:image/png;base64,{logo_base64}" alt="Logo Izquierdo">
                </td>
                <td class="title-cell">
                    <h1>Solicitud de Servicios</h1>
                    <h2>Medialab Universidad Galileo</h2>
                </td>
                <td class="logo-cell">
                    <img class="logo" src="data:image/png;base64,{mlab_logo_base64}" alt="Logo Derecho">
                </td>
                </tr>
            </table>
            </div>
            <div>
            <h3>Datos del Solicitante</h3>
            <p><strong>Fecha de Solicitud:</strong> {fSolicitud}</p>
            <p><strong>Nombre del Departamento:</strong> {depto}</p>
            <p><strong>Nombre:</strong> {nombreSolicita}</p>
            <p><strong>Número de Teléfono:</strong> {numTelefono}</p>
            <p><strong>Correo:</strong> {email}</p>
            </div>
            <div>
            <h3>Datos del Evento</h3>
            <p><strong>Fecha del Evento:</strong> {fechaEvento}</p>
            <p><strong>Hora de Inicio:</strong> {horaInicio}</p>
            <p><strong>Hora de Finalización:</strong> {horaFin}</p>
            <p><strong>Ubicación del Evento:</strong> {ubicacionEvento}</p>
            <p><strong>Nombre del Evento:</strong> {nombreEvento}</p>
            </div>
            </div>
            
            <h3>Observaciones</h3>
            <p>{observaciones}</p>

            <h3>Servicios Solicitados</h3>
            <table class="table" style="width: 100%;">
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

        # Generar PDF usando pdfkit con la configuración
        pdf = pdfkit.from_string(html, False, configuration=config, options={
            'page-size': 'Letter',
            'encoding': 'UTF-8',
            'no-outline': None,
            'margin-top': '0mm',
            'margin-right': '0mm',
            'margin-bottom': '0mm',
            'margin-left': '0mm'
        })

        # Generar nombre de archivo
        filename = generate_pdf_filename()
        
        # Crear respuesta con el PDF
        response = send_file(
            io.BytesIO(pdf),
            mimetype='application/pdf',
            as_attachment=True,
            download_name=filename
        )
        
        return response

    except Exception as e:
        print(f"Error: {str(e)}")
        return "Error al generar el PDF", 500

# Manejar acceso directo a /submit con GET
@app.route('/submit', methods=['GET'])
def handle_get_submit():
    return redirect(url_for('index'))  # Redirigir a la página principal

if __name__ == '__main__':
    app.run(debug=True)
