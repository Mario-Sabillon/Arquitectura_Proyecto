hostname > /home/msabillon/ProyectoFinal/informe.txt
date >> /home/msabillon/ProyectoFinal/informe.txt
cat /home/msabillon/ProyectoFinal/estado22.txt >> informe.txt
uuencode /home/msabillon/ProyectoFinal/informe.txt informe.txt > /tmp/out.mail
echo "GPIO22 OFF" | mail -s "APAGADO GPIO22" correoarquitectura976@gmail.com < /tmp/out.mail
