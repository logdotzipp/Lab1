# Lab1
 ME 405 Bin 9 Lab 1 - Motor Driver Class

 This repository contains code to test PWM functionality, along with using a L6206 H-Bridge Motor Driver Hat on the STM32 Nucleo.

 led.py runs a simple brightness cycle using Pulse Width Modulation. The brightness of an LED connected to PA0 is cycled from 0% brightness to 100% brightness every 5 seconds, then resets.

 motor_driver.py contains the Motor Driver class, which allows for using of the L6206 Motor Driver.

 motor_driver_test.py contains test code which changes the speed of the motor every second. This is simply used to verify that the MotorDriver class is functioning properly.
