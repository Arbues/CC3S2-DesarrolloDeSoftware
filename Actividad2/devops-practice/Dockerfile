# Usa la Imgen oficail de nodejs
FROM node:14

#Establece el directorio de trabajo en el contenedor
WORKDIR /app

#Copia el archivo package.json y package.lock al directorio de trabajo
COPY package*.json ./

#Instala Dependencias
RUN npm install

#Copia el resto de los archivos al directorio de trabajo
COPY . .

#Expone el puerto 3000
EXPOSE 3000

# Establece una variable de entorno para el puerto
ENV PORT=3000

#Comando para ejecutar la aplicacion
CMD ["node", "src/app.js"]