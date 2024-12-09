#!/bin/bash
echo 1 > /./home/msabillon/ProyectoFinal/estado22.txt

# Registrar la accion en Mysql 

# Datos para ingresar
DB_HOST="localhost"
DB_USER="sabillon"
DB_PASS="123456"
DB_NAME="bdarqui"
DB_TABLE="arqui"

# Se insertar el registros en la tabla de mysql
mysql -h "$DB_HOST" \
      -u "$DB_USER" \
      -p"$DB_PASS" \
      -D "$DB_NAME" \
      -e "
       INSERT INTO $DB_TABLE (descripcion,estado,fecha) 
       VALUES ('GPIO22','1',NOW());
       "
