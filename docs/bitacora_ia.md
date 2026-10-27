# Bitácora de IA · proyecto Starbucks Insight

**Fecha:** 11 de octubre de 2026. **Herramienta:** ChatGPT (GPT-6).  
**Criterio:** se registran las solicitudes y especificaciones de trabajo planteadas al asistente en esta elaboración; algunas aparecen resumidas como instrucciones técnicas y no son transcripciones literales del usuario. Los cálculos se verificaron con agregados programáticos.

| Paso | Solicitud/prompts principales (resumen) | Respuesta/resultado generado | Qué se aceptó, qué se modificó y por qué |
| --- | --- | --- | --- |
| 1. Planteamiento | «Cambiar el trabajo DSS de Walmart a una marca conocida: Starbucks; conservar materia y estudiante». | Propuso un DSS para Starbucks. | Aceptado. Se cambió íntegramente el modelo de datos; no solo portada. |
| 2. Fuente y límites | «Encontrar datos verificables de Starbucks para un tablero estático y describir su procedencia». | Dataset de Starbucks Customer Data y espejos de los JSON de Udacity. | Se precisó que son simulados, sin tiendas ni fechas comerciales; se descartó etiquetarlos como ventas reales de sucursales. |
| 3. Limpieza | «Revisar nulos, duplicados, edades, horas, importes y preparar agregaciones por segmento». | Auditoría de 306,534 eventos, 17,000 perfiles y 10 ofertas; suma con centavos enteros. | Se conservaron 397 filas idénticas, se trató 118 como sin edad y se mantuvieron los registros con sexo sin dato. |
| 4. Visualización | «Crear una página adaptable a celular con KPI, al menos cinco visualizaciones diferentes y filtro». | Sitio con SVG, tablas, línea, barras, dona y dispersión; filtro de género. | Se usó HTML, CSS y JS puro para compatibilidad con Pages, sin backend ni CDN. |
| 5. Validación | «Contrastar tres indicadores del dashboard con cálculos independientes y comprobar el filtro». | Comprobaciones de US$1,775,451.97, 138,953 compras, 17,000 clientes; prueba F: 49,382 y US$863,695.00. | Se aceptaron tras ejecutar las pruebas. Se revisó la responsividad a 390px sin desbordamiento. |
| 6. Interpretación | «Resumir hallazgos útiles, sin sobreinterpretar las conversiones». | Recomendaciones por cohortes, ofertas, datos faltantes y días altos. | Se corrigió la lectura errónea de completada/recibida como efecto causal; informativas no se califican por completadas. |
| 7. Publicación | «Preparar un ZIP para GitHub Pages con README, documentación y PDF». | Carpeta lista para subir. | La URL pública y la captura de Settings → Pages quedan pendientes hasta que el propietario publique. No se inventaron. |

## Errores y limitaciones encontrados

1. **Descarga de Kaggle bloqueada en el entorno.** Se recurrió a espejos públicos accesibles y se registró la procedencia exacta. No se afirmó una descarga directa que no ocurrió.
2. **Capturas por navegación local restringidas en el navegador de prueba.** Se resolvió inyectando el contenido del sitio, estilos y scripts en el mismo navegador para obtener imágenes reales del renderizado. Estas capturas no son evidencia de GitHub Pages.
3. **Se descartó una atribución causal incorrecta.** Las finalizaciones de ofertas no prueban que la promoción haya causado la compra.
4. **El dataset no tiene sucursales.** No se simuló una tabla de ventas por tienda, que sería inventada.
5. **Revisión de valores.** Se agregaron importes en centavos y se compararon los resultados con el archivo de control `validacion.json`.

## Reflexión personal orientativa (para revisar y personalizar)

La IA aceleró la propuesta de arquitectura web, el CSS responsivo, el cálculo de agregaciones y la preparación del documento, pero la comprobación de las fuentes y la interpretación de qué representa cada registro no deben delegarse sin supervisión. Especialmente, una cifra correcta puede producir una conclusión comercial equivocada si se confunde correlación, finalización y efecto causado por una oferta. Antes de entregar conviene revisar el proyecto, probar GitHub Pages personalmente e incorporar las capturas propias de publicación.
