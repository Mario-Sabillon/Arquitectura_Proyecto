#!/bin/bash
while true
          do
             valor1=$(python3 readinbox.py | grep -E "ON22|on22|On22|oN22" | cut -d " " -f3 | cut -b 24-27)
             valor2=$(python3 readinbox.py | grep -E "OFF22|off22|Off22|oFF22|ofF22|OfF22|OFf22|oFf22" | cut -d " " -f3 | cut -b 24-28)

             if [[ $valor1 = "ON22" || $valor1 = "on22" || $valor1 = "On22" || $valor1 = "oN22" ]]
                                    then
                                        echo $valor1
                                        sudo /./home/msabillon/ProyectoFinal/on22.sh
             else
                 if [[ $valor2 = "OFF22" || $valor2 = "off22" || $valor2 = "ofF22" || $valor2 = "oFf22" || $valor2 = "Off22" || $valor2 = "oFF22" ]]
                                         then
                                              echo $valor2
                                              sudo /./home/msabillon/ProyectoFinal/off22.sh
                                          fi
             fi 
             sleep 1
           done
