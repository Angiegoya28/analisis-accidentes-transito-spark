# analisis-accidentes-transito-spark
Proyecto académico de análisis de accidentes de tránsito en Colombia utilizando Apache Spark y procesamiento de datos.
Análisis de accidentes de tránsito en Colombia con Apache Spark

1. Descripción del proyecto

Este proyecto académico tiene como objetivo analizar información relacionada con los accidentes de tránsito en Colombia mediante el uso de herramientas de procesamiento de datos como Apache Spark y Apache Kafka.

Se desarrolló un proceso de análisis por lotes (Batch Processing) y un proceso de procesamiento en tiempo real (Streaming), utilizando datos de sensores simulados para demostrar la transmisión y el análisis de información.

2. Objetivos

- Procesar y analizar datos de accidentes de tránsito en Colombia.
- Identificar la distribución de accidentes por departamento.
- Analizar los registros según su gravedad.
- Implementar procesamiento de datos por lotes con Apache Spark.
- Desarrollar un flujo de datos en tiempo real utilizando Apache Kafka y Spark Structured Streaming.

3. Herramientas utilizadas

- Apache Spark 3.5.7
- Apache Kafka 3.9.2
- Python
- PySpark
- Ubuntu Linux
- VirtualBox

4. Archivos del proyecto

Archivo| Descripción
"analisis_accidentes_transito.py"| Procesamiento y análisis de datos por lotes.
"kafka_producer.py"| Generación y envío de datos simulados a Kafka.
"spark_streaming.py"| Lectura y procesamiento de datos en tiempo real con Spark.

5. Conjunto de datos

Se utiliza un conjunto de datos de accidentes de tránsito en Colombia obtenido del portal de Datos Abiertos de Colombia.

El archivo CSV se conserva localmente y no se incluye en este repositorio debido a su tamaño.

6. Resultados

El procesamiento por lotes permite identificar la cantidad de registros por departamento y clasificarlos según la gravedad de los accidentes.

El procesamiento en tiempo real permite recibir datos simulados de sensores mediante Kafka y procesarlos con Spark Structured Streaming.

7. Autor

Proyecto académico desarrollado para la Universidad Nacional Abierta y a Distancia (UNAD).

Tema: Procesamiento de datos con Apache Spark y Apache Kafka.
