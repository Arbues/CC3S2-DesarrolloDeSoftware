// Importa 'supertest', una herramienta para hacer pruebas HTTP en aplicaciones Node.js.
const request = require('supertest');

// Importa la aplicación Express desde 'src/app.js'.
const app = require('../src/app');

// Bloque de pruebas para la ruta GET '/'
describe('GET /', () => {
    let server;

    // Antes de todas las pruebas, inicia el servidor.
    beforeAll(() => {
        server = app.listen(0); // Usar 0 permite al sistema asignar automáticamente un puerto disponible.
    });

    // Después de todas las pruebas, cierra el servidor.
    afterAll(() => {
        server.close(); // Asegura que el servidor se cierra después de las pruebas.
    });

    // Prueba para verificar que el endpoint raíz ('/') responde con "Hello, World!".
    it('should return Hello, World!', async () => {
        const res = await request(app).get('/'); // Realiza una solicitud GET al endpoint raíz.
        expect(res.statusCode).toEqual(200); // Verifica que la respuesta tiene el estado 200 (OK).
        expect(res.text).toBe('Hello, World!'); // Verifica que la respuesta contiene el texto "Hello, World!".
    });
});

// Bloque de pruebas para la ruta GET '/delay'
describe('GET /delay', () => {
    let server;

    // Antes de todas las pruebas, inicia el servidor.
    beforeAll(() => {
        server = app.listen(0); // Usa 0 para asignar un puerto disponible.
    });

    // Después de todas las pruebas, cierra el servidor.
    afterAll(() => {
        server.close(); // Asegura que el servidor se cierra al final.
    });

    // Prueba para verificar que el endpoint '/delay' responde correctamente después de un retraso de 2 segundos.
    it('should return after a delay', async () => {
        const start = Date.now(); // Toma la hora de inicio.
        const res = await request(app).get('/delay'); // Realiza una solicitud GET al endpoint '/delay'.
        const end = Date.now(); // Toma la hora de finalización.
        const duration = end - start; // Calcula la duración de la solicitud.

        expect(res.statusCode).toEqual(200); // Verifica que la respuesta tiene el estado 200 (OK).
        expect(res.text).toBe('This was delayed by 2 seconds'); // Verifica que la respuesta es la esperada.
        expect(duration).toBeGreaterThanOrEqual(2000); // Verifica que el retraso fue de al menos 2 segundos.
    });
});