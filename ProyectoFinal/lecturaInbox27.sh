#!/bin/bash
while true
          do
             valor1=$(python3 readinbox.py | grep -E "ON27|on27|On27|oN27" | cut -d " " -f3 | cut -b 24-27)
             valor2=$(python3 readinbox.py | grep -E "OFF27|off27|Off27|oFF27|ofF27|OfF27|OFf27|oFf27" | cut -d " " -f3 | cut -b 24-28)

             if [[ $valor1 = "ON27" || $valor1 = "on27" || $valor1 = "On27" || $valor1 = "oN27" ]]
                                    then
                                        echo $valor1
                                        sudo /./home/msabillon/ProyectoFinal/on27.sh
             else
                 if [[ $valor2 = "OFF27" || $valor2 = "off27" || $valor2 = "ofF27" || $valor2 = "oFf27" || $valor2 = "Off27" || $valor2 = "oFF27" ]]
                                         then
                                              echo $valor2
                                              sudo /./home/msabillon/ProyectoFinal/off27.sh
                                          fi
             fi 
             sleep 1
           done
