hostname > /home/msabillon/ProyectoFinal/informe.txt
date >> /home/msabillon/ProyectoFinal/informe.txt
cat /home/msabillon/ProyectoFinal/estado27.txt >> informe.txt
uuencode /home/msabillon/ProyectoFinal/informe.txt informe.txt > /tmp/out.mail
echo "GPIO27 ON" | mail -s "ENCENDIDO GPIO27" correoarquitectura976@gmail.com < /tmp/out.mail
