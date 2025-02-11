import sys
import logging

# Configurar logging
logging.basicConfig(level=logging.DEBUG)

try:
    from app import app
except Exception as e:
    logging.error(f"Error importing app: {e}")
    sys.exit(1)

if __name__ == "__main__":
    app.run()
