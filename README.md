# MediaLab Solicitud de Servicios

Sistema de solicitud de servicios para MediaLab Universidad Galileo.

## Requisitos

- Python 3.8+
- Flask
- pdfkit
- wkhtmltopdf

## Instalación

1. Clona el repositorio:

bash
git clone https://github.com/klrchristian/solicitud_medialab.git
cd solicitud_medialab


2. Instala las dependencias:

bash
pip install -r requirements.txt


3. Instala wkhtmltopdf:
- Windows: Descarga desde https://wkhtmltopdf.org/downloads.html
- Linux: `sudo apt-get install wkhtmltopdf`
- Mac: `brew install wkhtmltopdf`

## Uso

1. Ejecuta la aplicación:

bash
python app.py


2. Abre tu navegador en `http://localhost:5000`

## Contribuir

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

   
También necesitarás un archivo `requirements.txt`:


Flask==2.0.1
pdfkit==1.0.0
