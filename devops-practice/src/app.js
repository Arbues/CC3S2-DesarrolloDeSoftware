// Importa el módulo 'express', que es un framework para aplicaciones web de Node.js
const express = require('express');

// Crea una instancia de la aplicación Express
const app = express();

// Define una ruta GET para el endpoint raíz ('/')
// Cuando se realiza una solicitud GET a esta ruta, se envía una respuesta con el mensaje "Hello, World!"
app.get('/', (req, res) => {
  // Envía una respuesta con el mensaje "Hello, World!"
  res.send('Hello, World!');
});

// Define el puerto en el que la aplicación escuchará las solicitudes
// Toma el valor de la variable de entorno 'PORT' si está definida, de lo contrario usa el puerto 3000
const port = process.env.PORT || 3000;

// Inicia el servidor y hace que escuche en el puerto definido
// Cuando el servidor esté corriendo, se imprimirá un mensaje en la consola indicando el puerto
app.listen(port, () => {
  // Imprime en la consola que el servidor está corriendo en el puerto especificado
  console.log(`Server running on port ${port}`);
});

// Exporta la instancia de la aplicación 'app' para que pueda ser utilizada en otros módulos
module.exports = app;
