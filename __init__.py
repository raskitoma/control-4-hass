import logging
import socket
import random
from time import sleep
 
C4_IP="10.0.25.21"
C4_IP_2="10.0.25.22"
_LOGGER = logging.getLogger(__name__)
 
DOMAIN = 'c4_services'
 
def send_udp_command(command, host, port):
    COUNTER = "0s2a" + str(random.randint(10, 99))
    COMMAND = COUNTER + " " + command + " \r\n"
    _LOGGER.warn("Sending command: %s", COMMAND)
    HOST = host
    PORT = port
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto( bytes(COMMAND, "utf-8"), (HOST, PORT))
    received = str(sock.recv(1024), "utf-8")
    _LOGGER.warn("Command sent. Response: %s", str(received))
    
def setup(hass, config):
    
    # Zone 1
    
    def handle_zone1_amp_off_select(call):
        #_LOGGER.warn("Powering AMP 01 Off...")
        send_udp_command("c4.amp.out 01 00", C4_IP, 8750)
        #_LOGGER.warn("AMP Powered Off...")
 
    def handle_zone1_amp_on_select(call):
        amp_input = hass.states.get("input_select.zone1_input").state[:1]
        volume_select = hass.states.get("input_number.zone1_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.out 01 0" + amp_input, C4_IP, 8750)
        send_udp_command("c4.amp.chvol 01 " + volume_select, C4_IP, 8750)
                   
    def handle_zone1_amp_volume_select(call):
        volume_select = hass.states.get("input_number.zone1_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 01 " + volume_select, C4_IP, 8750)
        
    def handle_zone1_amp_input_select(call):
        amp_input = hass.states.get("input_select.zone1_input").state[:1]
        amp_input = hex(int(amp_input))[2:]
        send_udp_command("c4.amp.out 01 0" + amp_input, C4_IP, 8750)
        volume_select = hass.states.get("input_number.zone1_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 01 " + volume_select, C4_IP, 8750)      

    # Zone 2
    
    def handle_zone2_amp_off_select(call):
        send_udp_command("c4.amp.out 02 00", C4_IP, 8750)
 
    def handle_zone2_amp_on_select(call):
        amp_input = hass.states.get("input_select.zone2_input").state[:1]
        volume_select = hass.states.get("input_number.zone2_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.out 02 0" + amp_input, C4_IP, 8750)
        send_udp_command("c4.amp.chvol 02 " + volume_select, C4_IP, 8750)
                   
    def handle_zone2_amp_volume_select(call):
        volume_select = hass.states.get("input_number.zone2_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 02 " + volume_select, C4_IP, 8750)
        
    def handle_zone2_amp_input_select(call):
        amp_input = hass.states.get("input_select.zone2_input").state[:1]
        amp_input = hex(int(amp_input))[2:]
        send_udp_command("c4.amp.out 02 0" + amp_input, C4_IP, 8750)
        volume_select = hass.states.get("input_number.zone2_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 02 " + volume_select, C4_IP, 8750)

    # Zone 3
    
    def handle_zone3_amp_off_select(call):
        send_udp_command("c4.amp.out 03 00", C4_IP, 8750)
 
    def handle_zone3_amp_on_select(call):
        amp_input = hass.states.get("input_select.zone3_input").state[:1]
        volume_select = hass.states.get("input_number.zone3_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.out 03 0" + amp_input, C4_IP, 8750)
        send_udp_command("c4.amp.chvol 03 " + volume_select, C4_IP, 8750)
                   
    def handle_zone3_amp_volume_select(call):
        volume_select = hass.states.get("input_number.zone3_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 03 " + volume_select, C4_IP, 8750)
        
    def handle_zone3_amp_input_select(call):
        amp_input = hass.states.get("input_select.zone3_input").state[:1]
        amp_input = hex(int(amp_input))[2:]
        send_udp_command("c4.amp.out 03 0" + amp_input, C4_IP, 8750)
        volume_select = hass.states.get("input_number.zone3_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 03 " + volume_select, C4_IP, 8750)

    # Zone 4
    
    def handle_zone4_amp_off_select(call):
        send_udp_command("c4.amp.out 04 00", C4_IP, 8750)
 
    def handle_zone4_amp_on_select(call):
        amp_input = hass.states.get("input_select.zone4_input").state[:1]
        volume_select = hass.states.get("input_number.zone4_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.out 04 0" + amp_input, C4_IP, 8750)
        send_udp_command("c4.amp.chvol 04 " + volume_select, C4_IP, 8750)
                   
    def handle_zone4_amp_volume_select(call):
        volume_select = hass.states.get("input_number.zone4_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 04 " + volume_select, C4_IP, 8750)
        
    def handle_zone4_amp_input_select(call):
        amp_input = hass.states.get("input_select.zone4_input").state[:1]
        amp_input = hex(int(amp_input))[2:]
        send_udp_command("c4.amp.out 04 0" + amp_input, C4_IP, 8750)
        volume_select = hass.states.get("input_number.zone4_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 04 " + volume_select, C4_IP, 8750)

    # Zone 5
    
    def handle_zone5_amp_off_select(call):
        send_udp_command("c4.amp.out 05 00", C4_IP, 8750)
 
    def handle_zone5_amp_on_select(call):
        amp_input = hass.states.get("input_select.zone5_input").state[:1]
        volume_select = hass.states.get("input_number.zone5_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.out 05 0" + amp_input, C4_IP, 8750)
        send_udp_command("c4.amp.chvol 05 " + volume_select, C4_IP, 8750)
                   
    def handle_zone5_amp_volume_select(call):
        volume_select = hass.states.get("input_number.zone5_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 05 " + volume_select, C4_IP, 8750)
        
    def handle_zone5_amp_input_select(call):
        amp_input = hass.states.get("input_select.zone5_input").state[:1]
        amp_input = hex(int(amp_input))[2:]
        send_udp_command("c4.amp.out 05 0" + amp_input, C4_IP, 8750)
        volume_select = hass.states.get("input_number.zone5_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 05 " + volume_select, C4_IP, 8750)

    # Zone 6
    
    def handle_zone6_amp_off_select(call):
        send_udp_command("c4.amp.out 06 00", C4_IP, 8750)
 
    def handle_zone6_amp_on_select(call):
        amp_input = hass.states.get("input_select.zone6_input").state[:1]
        volume_select = hass.states.get("input_number.zone6_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.out 06 0" + amp_input, C4_IP, 8750)
        send_udp_command("c4.amp.chvol 06 " + volume_select, C4_IP, 8750)
                   
    def handle_zone6_amp_volume_select(call):
        volume_select = hass.states.get("input_number.zone6_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 06 " + volume_select, C4_IP, 8750)
        
    def handle_zone6_amp_input_select(call):
        amp_input = hass.states.get("input_select.zone6_input").state[:1]
        amp_input = hex(int(amp_input))[2:]
        send_udp_command("c4.amp.out 06 0" + amp_input, C4_IP, 8750)
        volume_select = hass.states.get("input_number.zone6_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 06 " + volume_select, C4_IP, 8750)

    # Zone 7
    
    def handle_zone7_amp_off_select(call):
        send_udp_command("c4.amp.out 07 00", C4_IP, 8750)
 
    def handle_zone7_amp_on_select(call):
        amp_input = hass.states.get("input_select.zone7_input").state[:1]
        volume_select = hass.states.get("input_number.zone7_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.out 07 0" + amp_input, C4_IP, 8750)
        send_udp_command("c4.amp.chvol 07 " + volume_select, C4_IP, 8750)
                   
    def handle_zone7_amp_volume_select(call):
        volume_select = hass.states.get("input_number.zone7_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 07 " + volume_select, C4_IP, 8750)
        
    def handle_zone7_amp_input_select(call):
        amp_input = hass.states.get("input_select.zone7_input").state[:1]
        amp_input = hex(int(amp_input))[2:]
        send_udp_command("c4.amp.out 07 0" + amp_input, C4_IP, 8750)
        volume_select = hass.states.get("input_number.zone7_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 07 " + volume_select, C4_IP, 8750)

    # Zone 8
    
    def handle_zone8_amp_off_select(call):
        send_udp_command("c4.amp.out 08 00", C4_IP, 8750)
 
    def handle_zone8_amp_on_select(call):
        amp_input = hass.states.get("input_select.zone8_input").state[:1]
        volume_select = hass.states.get("input_number.zone8_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.out 08 0" + amp_input, C4_IP, 8750)
        send_udp_command("c4.amp.chvol 08 " + volume_select, C4_IP, 8750)
                   
    def handle_zone8_amp_volume_select(call):
        volume_select = hass.states.get("input_number.zone8_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 08 " + volume_select, C4_IP, 8750)
        
    def handle_zone8_amp_input_select(call):
        amp_input = hass.states.get("input_select.zone8_input").state[:1]
        amp_input = hex(int(amp_input))[2:]
        send_udp_command("c4.amp.out 08 0" + amp_input, C4_IP, 8750)
        volume_select = hass.states.get("input_number.zone8_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 08 " + volume_select, C4_IP, 8750)


    ###########################  Amp #2


    # zoneb 1
    
    def handle_zoneb1_amp_off_select(call):
        #_LOGGER.warn("Powering AMP 01 Off...")
        send_udp_command("c4.amp.out 01 00", C4_IP_2, 8750)
        #_LOGGER.warn("AMP Powered Off...")
 
    def handle_zoneb1_amp_on_select(call):
        amp_input = hass.states.get("input_select.zoneb1_input").state[:1]
        volume_select = hass.states.get("input_number.zoneb1_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.out 01 0" + amp_input, C4_IP_2, 8750)
        send_udp_command("c4.amp.chvol 01 " + volume_select, C4_IP_2, 8750)
                   
    def handle_zoneb1_amp_volume_select(call):
        volume_select = hass.states.get("input_number.zoneb1_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 01 " + volume_select, C4_IP_2, 8750)
        
    def handle_zoneb1_amp_input_select(call):
        amp_input = hass.states.get("input_select.zoneb1_input").state[:1]
        amp_input = hex(int(amp_input))[2:]
        send_udp_command("c4.amp.out 01 0" + amp_input, C4_IP_2, 8750)
        volume_select = hass.states.get("input_number.zoneb1_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 01 " + volume_select, C4_IP_2, 8750)      

    # zoneb 2
    
    def handle_zoneb2_amp_off_select(call):
        send_udp_command("c4.amp.out 02 00", C4_IP_2, 8750)
 
    def handle_zoneb2_amp_on_select(call):
        amp_input = hass.states.get("input_select.zoneb2_input").state[:1]
        volume_select = hass.states.get("input_number.zoneb2_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.out 02 0" + amp_input, C4_IP_2, 8750)
        send_udp_command("c4.amp.chvol 02 " + volume_select, C4_IP_2, 8750)
                   
    def handle_zoneb2_amp_volume_select(call):
        volume_select = hass.states.get("input_number.zoneb2_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 02 " + volume_select, C4_IP_2, 8750)
        
    def handle_zoneb2_amp_input_select(call):
        amp_input = hass.states.get("input_select.zoneb2_input").state[:1]
        amp_input = hex(int(amp_input))[2:]
        send_udp_command("c4.amp.out 02 0" + amp_input, C4_IP_2, 8750)
        volume_select = hass.states.get("input_number.zoneb2_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 02 " + volume_select, C4_IP_2, 8750)

    # zoneb 3
    
    def handle_zoneb3_amp_off_select(call):
        send_udp_command("c4.amp.out 03 00", C4_IP_2, 8750)
 
    def handle_zoneb3_amp_on_select(call):
        amp_input = hass.states.get("input_select.zoneb3_input").state[:1]
        volume_select = hass.states.get("input_number.zoneb3_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.out 03 0" + amp_input, C4_IP_2, 8750)
        send_udp_command("c4.amp.chvol 03 " + volume_select, C4_IP_2, 8750)
                   
    def handle_zoneb3_amp_volume_select(call):
        volume_select = hass.states.get("input_number.zoneb3_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 03 " + volume_select, C4_IP_2, 8750)
        
    def handle_zoneb3_amp_input_select(call):
        amp_input = hass.states.get("input_select.zoneb3_input").state[:1]
        amp_input = hex(int(amp_input))[2:]
        send_udp_command("c4.amp.out 03 0" + amp_input, C4_IP_2, 8750)
        volume_select = hass.states.get("input_number.zoneb3_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 03 " + volume_select, C4_IP_2, 8750)

    # zoneb 4
    
    def handle_zoneb4_amp_off_select(call):
        send_udp_command("c4.amp.out 04 00", C4_IP_2, 8750)
 
    def handle_zoneb4_amp_on_select(call):
        amp_input = hass.states.get("input_select.zoneb4_input").state[:1]
        volume_select = hass.states.get("input_number.zoneb4_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.out 04 0" + amp_input, C4_IP_2, 8750)
        send_udp_command("c4.amp.chvol 04 " + volume_select, C4_IP_2, 8750)
                   
    def handle_zoneb4_amp_volume_select(call):
        volume_select = hass.states.get("input_number.zoneb4_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 04 " + volume_select, C4_IP_2, 8750)
        
    def handle_zoneb4_amp_input_select(call):
        amp_input = hass.states.get("input_select.zoneb4_input").state[:1]
        amp_input = hex(int(amp_input))[2:]
        send_udp_command("c4.amp.out 04 0" + amp_input, C4_IP_2, 8750)
        volume_select = hass.states.get("input_number.zoneb4_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 04 " + volume_select, C4_IP_2, 8750)

    # zoneb 5
    
    def handle_zoneb5_amp_off_select(call):
        send_udp_command("c4.amp.out 05 00", C4_IP_2, 8750)
 
    def handle_zoneb5_amp_on_select(call):
        amp_input = hass.states.get("input_select.zoneb5_input").state[:1]
        volume_select = hass.states.get("input_number.zoneb5_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.out 05 0" + amp_input, C4_IP_2, 8750)
        send_udp_command("c4.amp.chvol 05 " + volume_select, C4_IP_2, 8750)
                   
    def handle_zoneb5_amp_volume_select(call):
        volume_select = hass.states.get("input_number.zoneb5_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 05 " + volume_select, C4_IP_2, 8750)
        
    def handle_zoneb5_amp_input_select(call):
        amp_input = hass.states.get("input_select.zoneb5_input").state[:1]
        amp_input = hex(int(amp_input))[2:]
        send_udp_command("c4.amp.out 05 0" + amp_input, C4_IP_2, 8750)
        volume_select = hass.states.get("input_number.zoneb5_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 05 " + volume_select, C4_IP_2, 8750)

    # zoneb 6
    
    def handle_zoneb6_amp_off_select(call):
        send_udp_command("c4.amp.out 06 00", C4_IP_2, 8750)
 
    def handle_zoneb6_amp_on_select(call):
        amp_input = hass.states.get("input_select.zoneb6_input").state[:1]
        volume_select = hass.states.get("input_number.zoneb6_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.out 06 0" + amp_input, C4_IP_2, 8750)
        send_udp_command("c4.amp.chvol 06 " + volume_select, C4_IP_2, 8750)
                   
    def handle_zoneb6_amp_volume_select(call):
        volume_select = hass.states.get("input_number.zoneb6_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 06 " + volume_select, C4_IP_2, 8750)
        
    def handle_zoneb6_amp_input_select(call):
        amp_input = hass.states.get("input_select.zoneb6_input").state[:1]
        amp_input = hex(int(amp_input))[2:]
        send_udp_command("c4.amp.out 06 0" + amp_input, C4_IP_2, 8750)
        volume_select = hass.states.get("input_number.zoneb6_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 06 " + volume_select, C4_IP_2, 8750)

    # zoneb 7
    
    def handle_zoneb7_amp_off_select(call):
        send_udp_command("c4.amp.out 07 00", C4_IP_2, 8750)
 
    def handle_zoneb7_amp_on_select(call):
        amp_input = hass.states.get("input_select.zoneb7_input").state[:1]
        volume_select = hass.states.get("input_number.zoneb7_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.out 07 0" + amp_input, C4_IP_2, 8750)
        send_udp_command("c4.amp.chvol 07 " + volume_select, C4_IP_2, 8750)
                   
    def handle_zoneb7_amp_volume_select(call):
        volume_select = hass.states.get("input_number.zoneb7_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 07 " + volume_select, C4_IP_2, 8750)
        
    def handle_zoneb7_amp_input_select(call):
        amp_input = hass.states.get("input_select.zoneb7_input").state[:1]
        amp_input = hex(int(amp_input))[2:]
        send_udp_command("c4.amp.out 07 0" + amp_input, C4_IP_2, 8750)
        volume_select = hass.states.get("input_number.zoneb7_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 07 " + volume_select, C4_IP_2, 8750)

    # zoneb 8
    
    def handle_zoneb8_amp_off_select(call):
        send_udp_command("c4.amp.out 08 00", C4_IP_2, 8750)
 
    def handle_zoneb8_amp_on_select(call):
        amp_input = hass.states.get("input_select.zoneb8_input").state[:1]
        volume_select = hass.states.get("input_number.zoneb8_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.out 08 0" + amp_input, C4_IP_2, 8750)
        send_udp_command("c4.amp.chvol 08 " + volume_select, C4_IP_2, 8750)
                   
    def handle_zoneb8_amp_volume_select(call):
        volume_select = hass.states.get("input_number.zoneb8_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 08 " + volume_select, C4_IP_2, 8750)
        
    def handle_zoneb8_amp_input_select(call):
        amp_input = hass.states.get("input_select.zoneb8_input").state[:1]
        amp_input = hex(int(amp_input))[2:]
        send_udp_command("c4.amp.out 08 0" + amp_input, C4_IP_2, 8750)
        volume_select = hass.states.get("input_number.zoneb8_volume").state
        volume_select = int(float(volume_select)) + 160
        volume_select = hex(volume_select)[2:]
        send_udp_command("c4.amp.chvol 08 " + volume_select, C4_IP_2, 8750)



    # Handlers

    hass.services.register(DOMAIN, 'handle_zone1_amp_off_select', handle_zone1_amp_off_select)
    hass.services.register(DOMAIN, 'handle_zone1_amp_on_select', handle_zone1_amp_on_select)
    hass.services.register(DOMAIN, 'handle_zone1_amp_volume_select', handle_zone1_amp_volume_select)
    hass.services.register(DOMAIN, 'handle_zone1_amp_input_select', handle_zone1_amp_input_select)
    hass.services.register(DOMAIN, 'handle_zone2_amp_off_select', handle_zone2_amp_off_select)
    hass.services.register(DOMAIN, 'handle_zone2_amp_on_select', handle_zone2_amp_on_select)
    hass.services.register(DOMAIN, 'handle_zone2_amp_volume_select', handle_zone2_amp_volume_select)
    hass.services.register(DOMAIN, 'handle_zone2_amp_input_select', handle_zone2_amp_input_select)
    hass.services.register(DOMAIN, 'handle_zone3_amp_off_select', handle_zone3_amp_off_select)
    hass.services.register(DOMAIN, 'handle_zone3_amp_on_select', handle_zone3_amp_on_select)
    hass.services.register(DOMAIN, 'handle_zone3_amp_volume_select', handle_zone3_amp_volume_select)
    hass.services.register(DOMAIN, 'handle_zone3_amp_input_select', handle_zone3_amp_input_select)
    hass.services.register(DOMAIN, 'handle_zone4_amp_off_select', handle_zone4_amp_off_select)
    hass.services.register(DOMAIN, 'handle_zone4_amp_on_select', handle_zone4_amp_on_select)
    hass.services.register(DOMAIN, 'handle_zone4_amp_volume_select', handle_zone4_amp_volume_select)
    hass.services.register(DOMAIN, 'handle_zone4_amp_input_select', handle_zone4_amp_input_select)
    hass.services.register(DOMAIN, 'handle_zone5_amp_off_select', handle_zone5_amp_off_select)
    hass.services.register(DOMAIN, 'handle_zone5_amp_on_select', handle_zone5_amp_on_select)
    hass.services.register(DOMAIN, 'handle_zone5_amp_volume_select', handle_zone5_amp_volume_select)
    hass.services.register(DOMAIN, 'handle_zone5_amp_input_select', handle_zone5_amp_input_select)
    hass.services.register(DOMAIN, 'handle_zone6_amp_off_select', handle_zone6_amp_off_select)
    hass.services.register(DOMAIN, 'handle_zone6_amp_on_select', handle_zone6_amp_on_select)
    hass.services.register(DOMAIN, 'handle_zone6_amp_volume_select', handle_zone6_amp_volume_select)
    hass.services.register(DOMAIN, 'handle_zone6_amp_input_select', handle_zone6_amp_input_select)
    hass.services.register(DOMAIN, 'handle_zone7_amp_off_select', handle_zone7_amp_off_select)
    hass.services.register(DOMAIN, 'handle_zone7_amp_on_select', handle_zone7_amp_on_select)
    hass.services.register(DOMAIN, 'handle_zone7_amp_volume_select', handle_zone7_amp_volume_select)
    hass.services.register(DOMAIN, 'handle_zone7_amp_input_select', handle_zone7_amp_input_select)
    hass.services.register(DOMAIN, 'handle_zone8_amp_off_select', handle_zone8_amp_off_select)
    hass.services.register(DOMAIN, 'handle_zone8_amp_on_select', handle_zone8_amp_on_select)
    hass.services.register(DOMAIN, 'handle_zone8_amp_volume_select', handle_zone8_amp_volume_select)
    hass.services.register(DOMAIN, 'handle_zone8_amp_input_select', handle_zone8_amp_input_select)

    # Handlers Amp 2

    hass.services.register(DOMAIN, 'handle_zoneb1_amp_off_select', handle_zoneb1_amp_off_select)
    hass.services.register(DOMAIN, 'handle_zoneb1_amp_on_select', handle_zoneb1_amp_on_select)
    hass.services.register(DOMAIN, 'handle_zoneb1_amp_volume_select', handle_zoneb1_amp_volume_select)
    hass.services.register(DOMAIN, 'handle_zoneb1_amp_input_select', handle_zoneb1_amp_input_select)
    hass.services.register(DOMAIN, 'handle_zoneb2_amp_off_select', handle_zoneb2_amp_off_select)
    hass.services.register(DOMAIN, 'handle_zoneb2_amp_on_select', handle_zoneb2_amp_on_select)
    hass.services.register(DOMAIN, 'handle_zoneb2_amp_volume_select', handle_zoneb2_amp_volume_select)
    hass.services.register(DOMAIN, 'handle_zoneb2_amp_input_select', handle_zoneb2_amp_input_select)
    hass.services.register(DOMAIN, 'handle_zoneb3_amp_off_select', handle_zoneb3_amp_off_select)
    hass.services.register(DOMAIN, 'handle_zoneb3_amp_on_select', handle_zoneb3_amp_on_select)
    hass.services.register(DOMAIN, 'handle_zoneb3_amp_volume_select', handle_zoneb3_amp_volume_select)
    hass.services.register(DOMAIN, 'handle_zoneb3_amp_input_select', handle_zoneb3_amp_input_select)
    hass.services.register(DOMAIN, 'handle_zoneb4_amp_off_select', handle_zoneb4_amp_off_select)
    hass.services.register(DOMAIN, 'handle_zoneb4_amp_on_select', handle_zoneb4_amp_on_select)
    hass.services.register(DOMAIN, 'handle_zoneb4_amp_volume_select', handle_zoneb4_amp_volume_select)
    hass.services.register(DOMAIN, 'handle_zoneb4_amp_input_select', handle_zoneb4_amp_input_select)
    hass.services.register(DOMAIN, 'handle_zoneb5_amp_off_select', handle_zoneb5_amp_off_select)
    hass.services.register(DOMAIN, 'handle_zoneb5_amp_on_select', handle_zoneb5_amp_on_select)
    hass.services.register(DOMAIN, 'handle_zoneb5_amp_volume_select', handle_zoneb5_amp_volume_select)
    hass.services.register(DOMAIN, 'handle_zoneb5_amp_input_select', handle_zoneb5_amp_input_select)
    hass.services.register(DOMAIN, 'handle_zoneb6_amp_off_select', handle_zoneb6_amp_off_select)
    hass.services.register(DOMAIN, 'handle_zoneb6_amp_on_select', handle_zoneb6_amp_on_select)
    hass.services.register(DOMAIN, 'handle_zoneb6_amp_volume_select', handle_zoneb6_amp_volume_select)
    hass.services.register(DOMAIN, 'handle_zoneb6_amp_input_select', handle_zoneb6_amp_input_select)
    hass.services.register(DOMAIN, 'handle_zoneb7_amp_off_select', handle_zoneb7_amp_off_select)
    hass.services.register(DOMAIN, 'handle_zoneb7_amp_on_select', handle_zoneb7_amp_on_select)
    hass.services.register(DOMAIN, 'handle_zoneb7_amp_volume_select', handle_zoneb7_amp_volume_select)
    hass.services.register(DOMAIN, 'handle_zoneb7_amp_input_select', handle_zoneb7_amp_input_select)
    hass.services.register(DOMAIN, 'handle_zoneb8_amp_off_select', handle_zoneb8_amp_off_select)
    hass.services.register(DOMAIN, 'handle_zoneb8_amp_on_select', handle_zoneb8_amp_on_select)
    hass.services.register(DOMAIN, 'handle_zoneb8_amp_volume_select', handle_zoneb8_amp_volume_select)
    hass.services.register(DOMAIN, 'handle_zoneb8_amp_input_select', handle_zoneb8_amp_input_select)

    # Return boolean to indicate that initialization was successfull.
    return True
