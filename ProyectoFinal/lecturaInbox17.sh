#!/bin/bash

while true
          do
            valor1=$(python3 readinbox.py | grep -E "ON17|on17|On17|oN17" | cut -d " " -f3 | cut -b 24-27)
            valor2=$(python3 readinbox.py | grep -E "OFF17|off17|Off17|oFF17|ofF17|OfF17|OFf17|oFf17" | cut -d " " -f3 | cut -b 24-28)

            if [[ $valor1 = "ON17" || $valor1 = "on17" || $valor1 = "On17" || $valor1 = "oN17" ]]
                                   then
                                       echo $valor1
                                       sudo /./home/msabillon/ProyectoFinal/on17.sh

            else
                if [[ $valor2 = "OFF17" || $valor2 = "off17" || $valor2 = "ofF17" || $valor2 = "oFf17" || $valor2 = "Off17" || $valor2 = "oFF17" ]]
                                        then
                                            echo $valor2
                                            sudo /./home/msabillon/ProyectoFinal/off17.sh
                                            fi
                 fi 
                 sleep 1
               done

