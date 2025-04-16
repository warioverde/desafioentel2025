# desafioentel2025
Subiré una bitacora de como hice este taller práctico y los links que utilicé para resolverlo

## Ejercicio 1: Mover data histórica desde archivos en CSV a la nueva base de datos

Para el ejercicio 1, investigué en google cómo escribir archivos csv en s3, para lo cúal me apoye en boto3. Tras releer el ejercicio, ví que una restricción era que el separador tenía que se un “|” y el archivo original tenía la separación con coma “,”, así que para solucionar eso, hice uso de este [tutoríal](https://www.youtube.com/watch?v=z19kO3FAi2s), la [documentación de pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html) y este [post](https://saturncloud.io/blog/how-to-remove-index-column-while-saving-csv-in-pandas/#:~:text=By%20default%2C%20pandas%20saves%20the,and%20setting%20it%20to%20False%20). Mientras que la creación del esquema lo hice utilizando crawlers de AWS y modificando el esquema que me crearon los crawlers con un cron que corre a las 03:00. (dejare json de los esquemas)
![image](https://github.com/user-attachments/assets/1922ab52-de21-4282-b99c-b22c8c6dd067)

## Ejercicio 3: Crear un feature que permita realizar backup de cada tabla y almacenarla 

Para crear el feature, hice uso de un glue job, me puse investigar cómo leer tablas, en mi caso, como las tengo guardadas en un s3 con un glue catalog, encontré este [post](https://jeevaawsclodejourney.medium.com/etl-pipeline-with-aws-glue-and-pyspark-a-hands-on-poc-5d793cc0f0ba) que me permite hacer la lectura de mis tablas y con ayuda de la [documentación de glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-avro-home.html) pude hacer escritura de ellas en formato AVRO, esto lo realicé en un espacio llamado /backup/[nombre_tabla] dentro de mi bucket. También complementé con [este](https://youtu.be/q5XLIf_4lmE) tutorial para recordar como se usan los argumentos de un glue job y pasar la base de datos (--DATABASE_NAME), las tablas (--TABLES_ENTEL) y el path de s3 (--BUCKUP_S3_URI) cómo argumento. Tras 5 intentos logré crear los backups en AVRO. Cómo funcionalidad extra, cree un cron semanal para ejecutar este job los días sabados.
![image](https://github.com/user-attachments/assets/ad485e63-69ae-47a0-90de-b2a28ae9b917)
![image](https://github.com/user-attachments/assets/c93e5f4a-e500-4ee1-aeb4-67bebe47fc0d)
![image](https://github.com/user-attachments/assets/50873a9e-22f2-45fa-9fba-bf636b90e8a7)
![image](https://github.com/user-attachments/assets/d6089589-6f00-4d19-8e30-44598b232c25)
![image](https://github.com/user-attachments/assets/570e245a-9218-4cf4-8faf-5f0a959fa357)
![image](https://github.com/user-attachments/assets/13219310-8bb2-47f9-b660-f19396fc97d2)
![image](https://github.com/user-attachments/assets/902d96e3-cf0a-4416-996e-a9587283f90d)

## Ejercicio 4: Crear un feature que permita restaurar una cierta tabla con su backup generado en el punto 3

Para abordar este ejercicio asumiré que el caso de uso es que por X motivo la información original está corrupta, por lo que se necesita sobrescribirla con información del backup. Para ello mi estrategía será tener un glue job que leera el AVRO y escribirá en .csv, esto es posible usando Pyspark. Googleando encontré [este](https://medium.com/@uzzaman.ahmed/using-avro-in-pyspark-a-comprehensive-guide-a6ecd34c120c) tutorial que muestra ejemplo de lectura en avro y también de escritura. También me apoyé en [este](https://sparkbyexamples.com/pyspark/pyspark-write-dataframe-to-csv-file/) y [este](https://aws.plainenglish.io/step-by-step-guide-loading-data-from-s3-into-pyspark-dataframes-with-aws-glue-f742ab664889)  tutorial. Posteriormente tuve que escribir el dataframe con pandas para que pudiera seguir el formato de csv y separador "|", me apoyé en la [documentación de pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html) y [stackoverflow](https://stackoverflow.com/questions/69905103/how-to-write-in-csv-file-without-creating-folder-in-pyspark). Finalmente, tras 12 intentos, llegué a un resultado y puedo hacer backup completo de los archivos

![image](https://github.com/user-attachments/assets/5f6ffe00-3f02-4a43-992a-1a2386a1fec3)
![image](https://github.com/user-attachments/assets/61178987-144e-4350-a56a-95aa1ac8b30f)
![image](https://github.com/user-attachments/assets/fe852c69-d845-4dee-9ba4-d02492d77a31)
![image](https://github.com/user-attachments/assets/8a1e5b85-f0a4-4c8c-9de7-969b93388c5a)







