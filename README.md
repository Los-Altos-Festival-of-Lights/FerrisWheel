# FerrisWheel

## Design

Orchestration of lighting and music is controlled by a single [Raspberry Pi CPU](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) and two (maybe 3) [F16v5 lighting controllers](https://pixelcontroller.com/store/featured/88-f16v5.html). 

## Design

![Overall Design](images/Ferris_Wheel_IT_Architecture.png)

## IT Architecture

![Brain Components](images/Ferris_Wheel_Brain.jpeg)

## Logins

### Raspberry Pi Player:

- admin/falcon
- fpp/festivaloflights

### F16v5 Lighting Controllers A & B

- admin/festivaloflights
- fpp/festivaloflights

## Network IPs

### WiFi (for production)

- Pi: `192.168.9.1`
- Controller A: `192.168.9.2`
- Controller B: `192.168.9.3`

### Wired Ethernet Static IPs (for initial configuration)

- Pi: `192.168.1.212`
- Controller A: `192.168.1.75`
- Controller B: `192.168.1.76`

### Last Resport Access WiFi (for access debugging)

- Controller A: WiFi `Falcon_F16V5_67A1`, IP address `192.168.8.1`
- Controller B: WiFi `Falcon_F16V5_F9E9`, IP address `192.168.8.1`

