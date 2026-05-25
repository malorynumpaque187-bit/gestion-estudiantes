# Usamos Python 3.11 como base del contenedor
FROM python:3.11-slim

# Creamos una carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de dependencias primero (optimización)
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código fuente al contenedor
COPY . .

# Le decimos a Docker que la app usa el puerto 5000
EXPOSE 5000

# Comando que se ejecuta cuando el contenedor inicia
CMD ["python", "app.py"]