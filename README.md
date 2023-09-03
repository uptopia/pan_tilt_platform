# pan_tilt_platform  

Directed Perception  
PAN-TILT CONTROLLER: model PTU-D46E  
PAN-TILT UNIT: model PTU-46-17.5  

## execution
git clone https://github.com/uptopia/pan_tilt_platform.git

sudo pip3 install pyserial
sudo dmesg | grep tty  
sudo chmod 777 /dev/ttyUSB0  

python3 ui2.py

1. press reset
2. type values + press ENTER
3. press OK


ref:  
https://www.artisantg.com/PLC/72424-1/FLIR-Systems-Directed-Perception-PTU-D46-Computer-Controlled-Pan-Tilt-Unit   
https://movitherm.com/wp-content/uploads/2018/07/ptu-e46-user-manual.pdf  
https://movitherm.com/wp-content/uploads/2017/01/E-Series-Command-Reference-Manual.pdf  
https://github.com/antoinebou12/Pan-Tilt-Controller  
