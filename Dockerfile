#Paso 1 Buscar una imagen base 
FROM python:3.12-alpine

#Paso 2 Crear el directorio de trabajo en el contenedor 
WORKDIR /app

#Paso 3 Copiar el archivo de dependencias 
COPY requirements.txt /app

#Paso 4 Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt 

#Paso 5 Copiar el código fuente
COPY app.py /app

#Paso 6 Exponer el puerto
EXPOSE 5000

#Paso 7 Comando para ejecutar la aplicación
CMD ["python", "app.py"]

