# Actividad 2 - Desarrollo de Software

## Preguntas de Reflexión
1. **¿Qué significa "desplazar a la izquierda" en el contexto de DevSecOps y por qué es importante?** Desplazar a la izquierda significa integrar medidas de seguridad desde las primeras etapas del ciclo de desarrollo, como el diseño y la codificación, en lugar de al final. Es importante porque permite detectar y corregir vulnerabilidades antes, reduciendo costos y riesgos.
    
2. **Explica cómo IaC mejora la consistencia y escalabilidad en la gestión de infraestructuras.** IaC automatiza la configuración y gestión de la infraestructura mediante código, asegurando que los entornos sean reproducibles y consistentes. Esto elimina errores humanos y facilita la escalabilidad, ya que los sistemas se pueden gestionar de manera más eficiente y fiable.
    
3. **¿Cuál es la diferencia entre monitoreo y observabilidad? ¿Por qué es crucial la observabilidad en sistemas complejos?** El monitoreo se enfoca en observar problemas predefinidos mediante métricas y alertas, mientras que la observabilidad permite entender el estado completo del sistema utilizando datos como logs, métricas y trazas. La observabilidad es crucial en sistemas complejos porque proporciona una visión profunda del comportamiento del sistema, facilitando la resolución de problemas no predefinidos.
    
4. **¿Cómo puede la experiencia del desarrollador impactar el éxito de DevOps en una organización?** Una buena experiencia del desarrollador, que incluye herramientas efectivas y flujos de trabajo fluidos, aumenta la productividad y satisfacción del equipo. Esto reduce silos organizacionales y mejora la colaboración, lo que es esencial para el éxito de DevOps.
    
5. **Describe cómo InnerSource puede ayudar a reducir silos dentro de una organización.** InnerSource permite a los desarrolladores de diferentes equipos colaborar en proyectos compartidos, promoviendo la transparencia y el intercambio de conocimientos. Esto reduce los silos organizacionales y fomenta una cultura de trabajo más abierta y colaborativa.
    
6. **¿Qué rol juega la ingeniería de plataformas en mejorar la eficiencia y la experiencia del desarrollador?** La ingeniería de plataformas crea herramientas y plataformas internas que permiten a los desarrolladores enfocarse en escribir código sin preocuparse por la infraestructura. Al automatizar tareas operativas, mejora la eficiencia y reduce la carga cognitiva de los desarrolladores, optimizando su experiencia y productividad.

## Documentación del Laboratorio

Este documento detalla todos los pasos seguidos durante el laboratorio de la Actividad 2, utilizando las modificaciones necesarias para el correcto funcionamiento.

### 1. Configuración del Proyecto

Primero, se creó el proyecto básico de Node.js con el siguiente comando:

```
mkdir devops-practice
cd devops-practice
npm init -y
```

Luego, se instalaron las dependencias necesarias:

```
npm install express jest
```

### 2. Estructura del Proyecto

Se crearon las carpetas y archivos necesarios para organizar el código fuente y las pruebas:

```
mkdir src tests
touch src/app.js tests/app.test.js
```

El código fuente de la API en `app.js` se encuentra en la ruta `src/app.js` del repositorio [enlace aquí](https://github.com/Arbues/CC3S2-DesarrolloDeSoftware/tree/main/Actividad2/devops-practice/src/app.js), mientras que las pruebas automatizadas en `app.test.js` se encuentran en `tests/app.test.js` [enlace aquí](https://github.com/Arbues/CC3S2-DesarrolloDeSoftware/tree/main/Actividad2/devops-practice/tests/app.test.js).

### 3. Implementación de la API

Se implementó una API básica en Node.js con los siguientes endpoints:

- GET `/`: Responde con "Hello, World!".
- GET `/delay`: Responde después de un retraso de 2 segundos.

### 4. Pruebas Automatizadas

Las pruebas para ambos endpoints fueron implementadas en el archivo `tests/app.test.js`. Las pruebas utilizan `supertest` y validan tanto el funcionamiento del endpoint básico como el de delay.

Para correr las pruebas, se utilizó el siguiente comando:

```
npm test
```

El archivo de configuración de los scripts de prueba (`package.json`) también fue modificado para que las pruebas se ejecuten correctamente.

### 5. Implementación de DevSecOps

Se integró una herramienta de auditoría de seguridad utilizando `npm audit`. El análisis de seguridad se automatizó a través de GitHub Actions.

#### Auditoría de seguridad manual:

```
npm audit
```

#### Pipeline en GitHub Actions

El archivo de configuración del pipeline se encuentra en la ruta `.github/workflows/ci.yml` [enlace aquí](https://github.com/Arbues/CC3S2-DesarrolloDeSoftware/tree/main/Actividad2/devops-practice/.github/workflows/ci.yml).

El pipeline realiza las siguientes tareas:
- Instala las dependencias.
- Ejecuta las pruebas.
- Realiza un análisis de seguridad con `npm audit`.
- Construye y ejecuta los contenedores de Docker.

### 6. Infraestructura como Código (IaC)

Para contenerizar la aplicación, se creó un archivo `Dockerfile`. El archivo Docker expone el puerto 3001 y configura la aplicación para ejecutarse en un entorno de producción.

Se utilizó Docker Compose para automatizar el despliegue de la aplicación y los servicios de monitoreo. El archivo `docker-compose.yml` define los servicios de la aplicación, Prometheus y Grafana, los cuales son ejecutados en sus respectivos puertos.

#### Construir y correr la imagen de Docker:

```
docker build -t devops-practice .
docker run -p 3001:3001 devops-practice
```

#### Usar Docker Compose para desplegar la aplicación:

```
docker compose up --build -d
```

Este comando ejecuta:
- **Node.js App** en `http://localhost:3001`
- **Prometheus** en `http://localhost:9090`
- **Grafana** en `http://localhost:3000`

### 7. Observabilidad

Para implementar observabilidad, se configuraron Prometheus y Grafana. El archivo `prometheus.yml` configura a Prometheus para recolectar métricas de la aplicación Node.js, mientras que Grafana visualiza esas métricas.

- Archivo de configuración de Prometheus: `prometheus.yml` [enlace aquí](https://github.com/Arbues/CC3S2-DesarrolloDeSoftware/tree/main/Actividad2/devops-practice/prometheus.yml).
- Grafana se configuró para ejecutarse junto con Prometheus en Docker Compose.

### 8. Limpieza de Docker Compose

Para detener y limpiar los contenedores después de ejecutarlos, se utilizó el siguiente comando:

```
docker compose down
```

### Conclusión

El laboratorio permitió aplicar conceptos clave de DevSecOps, Infraestructura como Código y Observabilidad en un entorno práctico. Se documentaron los pasos seguidos, desde la configuración del proyecto hasta la implementación de las herramientas de seguridad y monitoreo, todo ello utilizando técnicas modernas de automatización y contenerización.
