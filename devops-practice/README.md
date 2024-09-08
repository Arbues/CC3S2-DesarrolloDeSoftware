# Actividad 1 
## Preguntas de Reflexion:
#### Pregunta 1: ¿Por qué surgió la necesidad de DevOps en el desarrollo de software?
La necesidad de DevOps surgió debido a la falta de comunicación y coordinación entre los equipos de desarrollo y operaciones (o IT), lo que generaba ineficiencias, retrasos en los lanzamientos/deployment (genera perdidas en la emprea) y productos de baja calidad (generando desconfianza en el cliente).

#### Pregunta 2: Explica cómo la falta de comunicación y coordinación entre los equipos de desarrollo y operaciones en el pasado ha llevado a la creación de DevOps.
La falta de comunicación resultaba en que los equipos de desarrollo lanzaban código que no siempre funcionaba correctamente en los entornos de producción gestionados por operaciones (ósea entornos reales). Esta falta de coordinación hacía que los equipos de operaciones tuvieran que lidiar con problemas inesperados, aumentando la fricción y el tiempo de implementación y arreglo.

#### Pregunta 3: Describe cómo el principio de mejora continua afecta tanto a los aspectos técnicos como culturales de una organización.
En el aspecto técnico, la mejora continua permite optimizar procesos, asegurando que el software sea más robusto y eficiente. Culturalmente, fomenta una mentalidad de aprendizaje constante y colaboración entre los equipos, reduciendo los silos y mejorando la satisfacción del equipo.Esto se ve muy claro en los ciclos de retroalimentaicion, donde optienes los KPI (indicadores claves de rendimiento) y asi puedes mejorar rapidamente estrategias para el exito.

#### Pregunta 4: ¿Qué significa que DevOps no se trata solo de herramientas, individuos o procesos?
Significa que DevOps es más que la suma de sus partes; es una transformación cultural que requiere un cambio en la mentalidad y en la forma en que las personas trabajan juntas, más allá de simplemente implementar nuevas herramientas o procesos.

#### Pregunta 5: Según el texto, ¿cómo contribuyen los equipos autónomos y multifuncionales a una implementación exitosa de DevOps?
Los equipos autónomos y multifuncionales eliminan los cuellos de botella al ser capaces de manejar todas las fases del ciclo de vida del producto (SDLC) desde la codificacion asta y pruebas asta la implementacion y diseño, lo que acelera la compresion matizada del negocio, la toma de decisiones y mejora la colaboración, haciendo que los procesos sean más eficientes y efectivos.


## Documentacion DevOps-Practice: CI/CD Pipeline and Docker Automation

### Descripción General
En esta actividad se aplican los conceptos de DevOps en un entorno práctico. Se configurará un pipeline básico de CI/CD para un proyecto de software y se automatizarán procesos en un entorno local utilizando Docker. Además, se implementará una API REST con Node.js y se realizarán pruebas automáticas.

### 1. Configuración del entorno

#### 1.1. Instalación de herramientas previas
Antes de comenzar, asegúrate de tener las siguientes herramientas instaladas en tu sistema:
- **Node.js y npm**:
  ``` bash
  sudo apt update
  sudo apt install nodejs npm
  ```
- **Git**:
  ``` bash
  sudo apt install git
  ```
- **Docker y Docker Compose**:
  ``` bash
  sudo apt install docker-ce docker-ce-cli containerd.io
  sudo systemctl enable docker
  sudo systemctl start docker

  ```

Verifica la instalación de las herramientas con los siguientes comandos:
``` bash
node -v
npm -v
git --version
docker --version
docker compose version
```

#### 1.2. Inicialización del proyecto Node.js
Primero, se creará una aplicación Node.js básica con un endpoint REST. Sigue los pasos a continuación para configurar el entorno:

1. **Inicializa el proyecto de Node.js**:
    ``` bash
    mkdir devops-practice
    cd devops-practice
    npm init -y
    ```

2. **Instala las dependencias necesarias**:
    ``` bash
    npm install express jest
    ```

3. **Crea la estructura del proyecto**:
    ``` bash
    mkdir src tests
    touch src/app.js tests/app.test.js
    ```

#### 1.3. Implementación de la API REST

En el archivo `src/app.js`, se implementa una API REST sencilla con dos endpoints. Uno devuelve "Hello, World!" y otro simula un retraso de 2 segundos.

``` javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Hello, World!');
});

app.get('/delay', (req, res) => {
    setTimeout(() => {
        res.send('This was delayed by 2 seconds');
    }, 2000);
});

module.exports = app;

if (require.main === module) {
    const port = process.env.PORT || 0; 
    app.listen(port, () => {
        console.log(`Server running on port ${port}`);
    });
}
```

#### 1.4. Pruebas automáticas con Jest

En el archivo `tests/app.test.js`, se definen las pruebas automáticas para los endpoints de la API.

``` javascript
const request = require('supertest');
const app = require('../src/app');

describe('GET /', () => {
    let server;

    beforeAll(() => {
        server = app.listen(0);
    });

    afterAll(() => {
        server.close();
    });

    it('should return Hello, World!', async () => {
        const res = await request(app).get('/');
        expect(res.statusCode).toEqual(200);
        expect(res.text).toBe('Hello, World!');
    });
});

describe('GET /delay', () => {
    let server;

    beforeAll(() => {
        server = app.listen(0);
    });

    afterAll(() => {
        server.close();
    });

    it('should return after a delay', async () => {
        const start = Date.now();
        const res = await request(app).get('/delay');
        const end = Date.now();
        const duration = end - start;

        expect(res.statusCode).toEqual(200);
        expect(res.text).toBe('This was delayed by 2 seconds');
        expect(duration).toBeGreaterThanOrEqual(2000);
    });
});
```

#### 1.5. Configura el script de test en package.json

``` json
{
  "name": "devops-practice",
  "version": "1.0.0",
  "main": "src/app.js",
  "scripts": {
    "test": "jest --detectOpenHandles"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "express": "^4.19.2"
  },
  "devDependencies": {
    "jest": "^29.7.0",
    "supertest": "^6.3.4"
  }
}
```

---

### 2. Pipeline CI/CD

#### Parte 1: Configura integración continua (CI) con GitHub Actions

Para automatizar la integración continua y las pruebas, se utilizarán los workflows de GitHub Actions.

1. **Crea la estructura para GitHub Actions**:
    ``` bash
    mkdir -p .github/workflows
    touch .github/workflows/ci.yml
    ```

2. **Define el flujo de trabajo en `.github/workflows/ci.yml`**:

``` yml
name: CI Pipeline
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v2
    - name: Set up Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '14'
    - name: Install dependencies
      run: npm install
      working-directory: devops-practice
    - name: Check Docker and Docker Compose versions
      run: |
        docker --version
        docker compose version  # Usa docker compose en lugar de docker-compose
    - name: Build and run Docker Compose
      run: |
        docker compose up --build -d  # Cambiar docker-compose a docker compose
      working-directory: devops-practice
    - name: Run tests
      run: npm test
      working-directory: devops-practice
    - name: Stop and clean Docker Compose
      run: |
        docker compose down  # Cambiar docker-compose a docker compose
      working-directory: devops-practice
```
#### Parte 2: Configura entrega continua (CD) con Docker

Docker Compose se utiliza para automatizar la configuración y la gestión del entorno local con contenedores Docker.

1. **Crea el archivo `docker-compose.yml`**:

    El siguiente archivo define un servicio llamado `app` que se construye a partir del directorio donde está el `Dockerfile`, mapea los puertos y establece las variables de entorno necesarias.

    ``` yml
    version: '3.8'

    services:
      app:
        build: devops-practice
        ports:
          - "3001:3001"
        environment:
          - NODE_ENV=production
        container_name: devops-practice-container
    ```

2. **Corre la aplicación usando Docker Compose**:

    El siguiente comando construye la imagen de Docker y corre los contenedores en segundo plano:

    ``` bash
    docker compose up --build -d
    ```

   - **`--build`**: Fuerza la construcción de la imagen Docker, asegurando que cualquier cambio en los archivos o dependencias se refleje.
   - **`-d`**: Ejecuta los contenedores en modo "detached", es decir, en segundo plano.

   Ahora tu aplicación estará corriendo en `http://localhost:3001`.
---
#### **3 Convertir el proyecto en un repositorio Git y subirlo a GitHub**

1. **Inicializa Git en tu proyecto**: Asegúrate de estar en el directorio raíz del proyecto (en este caso, `devops-practice`):
    
    ``` bash
    git init 
    ```
    
2. **Añade los archivos al repositorio**:
    
    ``` bash
    git add . 
    ```
    
    Esto añadirá todos los archivos al área de "stage" para ser comiteados.
    
3. **Haz un commit inicial**:
    
    ``` bash
    git commit -m "Initial commit of the DevOps practice project" 
    ```
    
4. **Crea un nuevo repositorio en GitHub**:
    
    - Ve a tu cuenta de GitHub y crea un nuevo repositorio (puede ser público o privado).
    - Copia la URL del repositorio remoto que acabas de crear.
5. **Conecta tu repositorio local con el repositorio remoto**:
    
    ``` bash
    git remote add origin <your-repo-url> 
    ```
    
6. **Sube los cambios al repositorio remoto en GitHub**:
    
    ``` bash
    git push -u origin main 
    ```
    
    Esto subirá todos los archivos y commits a GitHub.
---

### 4. Evaluación de la experiencia


**Beneficios del pipeline automatizado:**

- **Eficiencia**: La integración continua asegura que los cambios en el código son validados automáticamente mediante pruebas y la construcción de contenedores Docker.
- **Reducción de errores manuales**: Al automatizar tanto las pruebas como el despliegue, se minimiza la posibilidad de cometer errores al realizar tareas manuales repetitivas.
- **Facilidad de colaboración**: Con GitHub Actions, cualquier colaborador del equipo puede realizar cambios, sabiendo que estos serán probados automáticamente antes de ser integrados.
- **Portabilidad**: Docker y Docker Compose facilitan la portabilidad del proyecto, permitiendo a los desarrolladores ejecutar la misma aplicación en diferentes entornos sin configuraciones adicionales.