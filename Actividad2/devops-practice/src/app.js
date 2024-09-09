// Importa el módulo 'express', que es un framework para crear servidores web en Node.js.
const express = require('express');

// Crea una instancia de la aplicación Express.
const app = express();

// Define una ruta GET para la raíz ('/'). Cuando se accede a esta ruta, responde con "Hello, World!".
app.get('/', (req, res) => {
    res.send('Hello, World!');
});

// Define una ruta GET para '/delay'. Esta ruta simula un retraso de 2 segundos antes de responder.
app.get('/delay', (req, res) => {
    setTimeout(() => {
        res.send('This was delayed by 2 seconds');
    }, 2000); // Retraso de 2000 ms (2 segundos)
});

// Exporta la aplicación Express para que pueda ser utilizada en otros archivos como en los tests.
module.exports = app;

// Si este archivo es ejecutado directamente (no importado como módulo), inicia el servidor.
if (require.main === module) {
    // Obtiene el puerto de la variable de entorno 'PORT', o usa cualquier puerto disponible asignado por el sistema.
    const port = process.env.PORT || 0; 
    // Inicia el servidor escuchando en el puerto especificado.
    app.listen(port, () => {
        console.log(`Server running on port ${port}`);
    });
}