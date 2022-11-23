# imagen base de docker
FROM debian

# instala y actualiza la base de docker, con sus respectivas carpetas
RUN	apt update && \	
	apt install -y python && \
	apt install -y pip && \
	mkdir -p /app/static/css && \
	mkdir /app/templates

#crea el directorio de trabajo
WORKDIR /app

#copia los archivos
COPY app.py .
COPY requirements.txt .
COPY RF_final_model.joblib .
COPY bootstrap.min.css ./static/css
COPY main.css ./static/css
COPY base.html ./template
COPY index.html ./template

#Instala los paquetes pip
RUN pip install -r requirements.txt

#ejecuta el servidor
ENTRYPOINT [ "python3", "/app/app.py" ]
