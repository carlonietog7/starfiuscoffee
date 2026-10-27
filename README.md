# Starbucks Insight · Sistema de Soporte a Decisiones

**Proyecto académico:** Infraestructura Tecnológica  
**Estudiante:** Santiago Martin Picazo  
**Carrera:** Administración de Negocios en Entornos Virtuales  
**Fecha de preparación:** 11 de octubre de 2026

## Descripción

Dashboard web estático e interactivo para analizar 138,953 registros de compra y las promociones de una muestra **simulada** de Starbucks Rewards. Contiene KPI, visualizaciones de línea, barras, dona, dispersión, tabla y filtro de género; todos los indicadores se recalculan en el navegador. Diseñado para computadora y celular.

## Fuente real de los datos (no son reportes oficiales de Starbucks)

- **Dataset de referencia en Kaggle:** Ihor Muliar (2021), [Starbucks Customer Data](https://www.kaggle.com/datasets/ihormuliar/starbucks-customer-data).
- **Procedencia original:** datos simulados de Starbucks/Udacity, usados en su desafío Capstone.
- **Fuente efectivamente consultada durante esta preparación (11/10/2026):** espejos públicos en [roydazhong/Starbucks](https://github.com/roydazhong/Starbucks) (`portfolio.json` y `profile.json`) y [Typhoon1089/capstone-starbucks-challenge](https://github.com/Typhoon1089/capstone-starbucks-challenge) (`transcript.json`). No fue posible hacer descarga directa de Kaggle en este entorno; **no se afirma haber descargado desde Kaggle**.
- **Observaciones:** 10 ofertas; 17,000 perfiles; 306,534 eventos totales, de los cuales 138,953 son transacciones. Las variables `time` son horas desde que inició un experimento, no fechas del calendario. No se dispone de ciudades ni sucursales, por lo que este DSS se orienta a marketing y transacciones, no ventas por tienda.
- **Moneda:** dólares estadounidenses **simulados**.

El repositorio incluye `data/resumen.json` y `data/data.js`: datos agrupados por segmento sin IDs personales, empleados directamente por el sitio. No se requiere backend, cuenta ni API.

## Ejecutar el dashboard

Abrir `index.html` en un navegador moderno o servir la carpeta estática. El dashboard también funciona localmente porque `data/data.js` se incluye como script, sin peticiones HTTP.

## GitHub Pages

1. Crear un repositorio público llamado `dss-starbucks-insight` en la cuenta propia.
2. Subir **el contenido de esta carpeta** al directorio raíz del repositorio, incluido `index.html` y `data/data.js`.
3. Ir a **Settings → Pages → Deploy from a branch → main / (root) → Save**.
4. Copiar la URL real mostrada por GitHub en la portada del PDF y en este README.
5. Probar con el celular o en modo incógnito y capturar Pages y el historial de commits.

**Repositorio público:** pendiente de creación/publicación.  
**Sitio GitHub Pages:** pendiente de publicación.  
No se proporcionan enlaces inventados.

## Comprobación de datos

```bash
python scripts/validar.py
```

Las cifras se almacenan en centavos enteros para evitar errores de suma binaria:

| Medida | Valor validado |
| --- | ---: |
| Ventas simuladas | US$1,775,451.97 |
| Transacciones | 138,953 |
| Clientes | 17,000 |
| Eventos recibidos | 76,277 |
| Eventos vistos | 57,725 |
| Eventos completados | 33,579 |

## Estructura

- `index.html`, `styles.css`, `app.js`: sitio estático.
- `data/resumen.json`: agregados de la muestra (fuente del dashboard).
- `data/data.js`: espejo JavaScript legible por la página incluso offline.
- `scripts/validar.py`: 3+ validaciones reproducibles contra el resumen.
- `scripts/auditar_origen.py`: auditoría opcional sobre las tres fuentes JSON-lines.
- `images/`: capturas reales de la interfaz renderizada (escritorio y celular).
- `docs/bitacora_ia.md`: bitácora de especificaciones/prompts y revisión de IA.
- `validacion.json`: archivo de control independiente de KPI.

## Tecnologías

HTML5, CSS responsive, JavaScript nativo, SVG, Python 3 para control estadístico y ReportLab para el informe. No se requiere framework ni dependencias del lado del navegador.

## Restricciones interpretativas

Las 397 filas idénticas entre eventos se conservaron: podrían corresponder a eventos válidos sin identificador individual. La edad 118 está asociada con demografía faltante y se maneja como «sin dato». Es incorrecto equiparar eventos «completada / recibida» con una conversión causal única de usuarios: un cliente puede completar sin haber visto la oferta. No se deben atribuir ventas a una campaña sin una metodología adicional.
