# SBC-LCD1.28R-display-with-Raspberry-Pi-Pico
This repository provides resources and code to interface a 1.28" Round LCD display with the Raspberry Pi Pico using CircuitPython. The project includes a Fritzing Diagram for hardware setup and all the necessary code to get started quickly.

## Hardware Setup
* Raspberry Pi Pico
* SBC-LCD1.28R display
* USB cable
* Breadboard (optional)
* Jumper wires (optional)

Follow the provided Fritzing Diagram to connect the 1.28" Round LCD display to your Raspberry Pi Pico.
![schematic](https://github.com/SwannSchilling/SBC-LCD1.28R-display-with-Raspberry-Pi-Pico/assets/36327710/dae602ca-ec85-4012-92a0-7daedf0bc375)

## CircuitPython Installation
Make sure you have CircuitPython installed on your Raspberry Pi Pico. You can find the latest firmware for the Pico here.
* [circuitpython.org/board/raspberry\_pi\_pico](https://circuitpython.org/board/raspberry_pi_pico/) - The lastest firmware for the Pico.


You will need to install the following librarys:
circup install gc9a01
circup install gifio

Some other usefull librarys are:
circup install adafruit_display_text
circup install adafruit_imageload

Circup requires Python 3.5 or higher.

In a virtualenv, pip install circup should do the trick. This is the simplest way to make it work.

## Code
Clone this repository and copy the provided CircuitPython code onto your to your local machine.
Plug in the Raspberry Pi Pico via USB and copy the GIF folder and the code.py to your CIRCUITPI drive.

## Additional Resources
CircuitPython_GC9A01_demos: A repository that provided some of the code used in this project.
* [CircuitPython_GC9A01_demos](https://github.com/todbot/CircuitPython_GC9A01_demos/tree/main) - The repository where I got some of the code and it was a big help.
Mu Code Editor: An excellent code editor for CircuitPython development.
* [codewith.mu](https://codewith.mu/) - A code editor that is great help when using Circuit Python.
CircuitPython on Raspberry Pi Pico: 
* [learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/overview](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/overview) - Some additional info about Circuit Python on the Raspberry Pi Pico.

## Acknowledgments
Thanks to todbot for the helpful code in the CircuitPython_GC9A01_demos repository.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code for your projects.

Happy Hacking!





