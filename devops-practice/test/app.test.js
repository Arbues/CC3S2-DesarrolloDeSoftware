// Importa el módulo 'supertest', que es una herramienta para realizar pruebas HTTP en aplicaciones Node.js
const request = require('supertest');

// Importa la aplicación 'app' desde el archivo 'src/app.js'
const app = require('../src/app');

// Variable para almacenar el servidor
let server;

// Define un bloque de pruebas para el endpoint GET '/'
describe('GET /', () => {
  // Antes de que se ejecute la prueba, inicia el servidor
  beforeAll((done) => {
    server = app.listen(3000, () => {
      done();
    });
  });

  // Después de que la prueba termine, cierra el servidor
  afterAll((done) => {
    server.close(done);
  });

  // Define una prueba que verifica que la respuesta del endpoint es "Hello, World!"
  it('should return Hello, World!', async () => {
    // Realiza una solicitud GET al endpoint raíz ('/')
    const res = await request(app).get('/');
    
    // Verifica que el código de estado HTTP de la respuesta sea 200 (OK)
    expect(res.statusCode).toEqual(200);
    
    // Verifica que el texto de la respuesta sea "Hello, World!"
    expect(res.text).toBe('Hello, World!');
  });
});
