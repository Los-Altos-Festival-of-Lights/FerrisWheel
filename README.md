# FerrisWheel

## Design

Orchestration of lighting and music is controlled by a single [Raspberry Pi CPU](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) and two (maybe 3) [F16v5 lighting controllers](https://pixelcontroller.com/store/featured/88-f16v5.html). 

## Design

![Brain Components](images/Ferris_Wheel_Brain.jpeg)

## IT Architecture

All computing devices connect to a Wifi 6 multband, two-device-mesh at `FerrisNetwork` or `FerrisNetwork_iot`, a router on the float base configured as follows:

![Overall Design](images/Ferris_Wheel_IT_Architecture.png)ß

## Network IPs

### Wired Ethernet Static IPs (for show development)

- `FerrisNetwork_iot` router `192.168.10.254`
- Raspberry Pi Player: `192.168.10.10`
- Controller A: `192.168.10.20`
- Controller B: `192.168.10.30`

### WiFi Static IPs (for show timing)

- Controller A: `192.168.10.21`
- Controller B: `192.168.10.31`

### Last Resort Access WiFi IPs (for access debugging)

- Raspberry Pi Player: WiFi `FPP`, IP address `192.168.8.1`
- Controller A: WiFi `Falcon_F16V5_67A1`, IP address `192.168.8.1`
- Controller B: WiFi `Falcon_F16V5_F9E9`, IP address `192.168.8.1`

