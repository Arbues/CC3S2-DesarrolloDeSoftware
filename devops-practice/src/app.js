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

// Exporta la instancia de la aplicación 'app' para que pueda ser utilizada en otros módulos
module.exports = app;
