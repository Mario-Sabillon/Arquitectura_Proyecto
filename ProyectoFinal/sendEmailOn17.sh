hostname > /home/msabillon/ProyectoFinal/informe.txt
date >> /home/msabillon/ProyectoFinal/informe.txt
cat /home/msabillon/ProyectoFinal/estado17.txt >> informe.txt
uuencode /home/msabillon/ProyectoFinal/informe.txt informe.txt > /tmp/out.mail
echo "GPIO17 ON" | mail -s "ENCENDIDO GPIO17" correoarquitectura976@gmail.com < /tmp/out.mail
