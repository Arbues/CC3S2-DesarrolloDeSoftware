# Actividad 2 - Desarrollo de Software

## Preguntas de Reflexión
1. ¿Qué significa "desplazar a la izquierda" en el contexto de DevSecOps y por qué es importante?
2. Explica cómo IaC mejora la consistencia y escalabilidad en la gestión de infraestructuras.
3. ¿Cuál es la diferencia entre monitoreo y observabilidad? ¿Por qué es crucial la observabilidad en sistemas complejos?
4. ¿Cómo puede la experiencia del desarrollador impactar el éxito de DevOps en una organización?
5. Describe cómo InnerSource puede ayudar a reducir silos dentro de una organización.
6. ¿Qué rol juega la ingeniería de plataformas en mejorar la eficiencia y la experiencia del desarrollador?

## Descripción del Proyecto

Este proyecto forma parte del curso de Desarrollo de Software, cuyo objetivo es aplicar y comprender los conceptos clave relacionados con DevSecOps, Infraestructura como Código (IaC), y Observabilidad.

El repositorio contiene una aplicación sencilla de Node.js con una API REST básica, pruebas automatizadas, y configuraciones de infraestructura y monitoreo. Se han implementado prácticas de seguridad y automatización usando GitHub Actions y Docker.

### Estructura del Proyecto

```
.
└── devops-practice
    ├── Dockerfile
    ├── docker-compose.yml
    ├── package-lock.json
    ├── package.json
    ├── prometheus.yml
    ├── src
    │   └── app.js
    └── tests
        └── app.test.js
```

### Objetivos de la Actividad

- **DevSecOps**: Integración de la seguridad en el ciclo de vida de desarrollo mediante análisis automatizado de vulnerabilidades.
- **Infraestructura como Código (IaC)**: Contenerización y gestión automatizada del entorno usando Docker y Docker Compose.
- **Observabilidad**: Configuración de herramientas de monitoreo como Prometheus y Grafana para mejorar la visibilidad del sistema.

## Instrucciones para el Uso

### 1. Clonar el Repositorio

```
git clone https://github.com/Arbues/CC3S2-DesarrolloDeSoftware.git
cd CC3S2-DesarrolloDeSoftware/Actividad2/devops-practice
```

### 2. Instalación de Dependencias

```
npm install
```

### 3. Ejecutar la Aplicación Localmente

```
node src/app.js
```

La aplicación estará disponible en `http://localhost:3001`.

### 4. Pruebas Automatizadas

Para ejecutar las pruebas, usa el siguiente comando:

```
npm test
```

Las pruebas verifican el correcto funcionamiento de la API en los endpoints `/` y `/delay`.

### 5. Contenerización con Docker

Construir la imagen de Docker:

```
docker build -t devops-practice .
```

Correr el contenedor:

```
docker run -p 3001:3001 devops-practice
```

### 6. Usar Docker Compose para el Despliegue

Para ejecutar la aplicación, junto con los servicios de Prometheus y Grafana, usa el siguiente comando:

```
docker compose up --build -d
```

Este comando ejecutará los tres servicios:

- **Node.js App**: Expuesta en `http://localhost:3001`.
- **Prometheus**: Disponible en `http://localhost:9090`.
- **Grafana**: Disponible en `http://localhost:3000`.

### 7. Auditoría de Seguridad

Para realizar un análisis de seguridad de las dependencias del proyecto:

```
npm audit
```

### 8. Pipeline de GitHub Actions

Se ha configurado un pipeline CI/CD en GitHub Actions que automatiza las siguientes tareas:

- Instalación de dependencias.
- Ejecución de pruebas.
- Auditoría de seguridad.
- Gestión de contenedores con Docker.

El archivo de configuración se encuentra en la ruta: `.github/workflows/ci.yml`.

## Ubicación de los Archivos

- **Código fuente de la aplicación**: [`devops-practice/src/app.js`](https://github.com/Arbues/CC3S2-DesarrolloDeSoftware/tree/main/Actividad2/devops-practice/src/app.js)
- **Pruebas automatizadas**: [`devops-practice/tests/app.test.js`](https://github.com/Arbues/CC3S2-DesarrolloDeSoftware/tree/main/Actividad2/devops-practice/tests/app.test.js)
- **Pipeline de CI/CD**: [`devops-practice/.github/workflows/ci.yml`](https://github.com/Arbues/CC3S2-DesarrolloDeSoftware/.github/workflows/ci.yml)
