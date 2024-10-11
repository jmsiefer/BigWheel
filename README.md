
# Big Wheel Lunch Decision Maker

## Overview

The **Big Wheel Lunch Decision Maker** is a fun and interactive Python-based application designed to help you decide what to have for lunch! This project features a spinning decision wheel that lands on a random suggestion when clicked. Whether you’re stuck choosing between a salad, sandwich, or sushi, this tool can make the decision for you in a visually engaging way.

## Features

- **Interactive Spinning Wheel**: Click on the wheel to spin it and watch it rotate before slowing down and stopping at a random decision.
- **Randomized Spin Speed**: The wheel starts spinning at a random speed, adding an element of surprise each time you use it.
- **Customizable Images**: Uses foreground and background images for the wheel, allowing you to customize the look of your wheel with your own images.
- **Transparent Window**: The window has a transparent background, allowing the spinning wheel to appear seamlessly on your desktop.
- **Drag and Drop Window**: Click and drag to reposition the wheel anywhere on your screen.

## Prerequisites

- **Python 3.x**
- **Pygame**: Install via pip:
  ```bash
  pip install pygame
  ```
- **PIL (Pillow)**: Install via pip:
  ```bash
  pip install pillow
  ```
- **PyWin32**: Install via pip (for Windows transparency and window manipulation):
  ```bash
  pip install pywin32
  ```

## Setup

1. Clone this repository or download the `BigWheel.py` script.
2. Ensure that you have the necessary images for the wheel:
   - `BigWheelFG.png` (Foreground Image)
   - `BigWheelBG.png` (Background Image)
3. Update the `foreground_path` and `background_path` variables in the script to point to the locations of your image files.
4. Run the script using:
   ```bash
   python BigWheel.py
   ```

## How to Use

1. Launch the script to display the spinning wheel on your desktop.
2. Click on the wheel to start spinning it.
3. The wheel will rotate at a random speed and gradually slow down until it stops at a random lunch suggestion.
4. Drag the window by holding the left mouse button to move it around the screen.

## Customization

- **Change Spin Speed**: Modify the `spin_speed` variable to adjust the initial spin speed of the wheel.
- **Adjust Deceleration**: Tweak the `deceleration` value for a faster or slower slowdown.
- **Custom Images**: Replace `BigWheelFG.png` and `BigWheelBG.png` with your own images to change the look of the wheel.

## Troubleshooting

- **Image Loading Errors**: Ensure the image paths are correct and that the files are accessible.
- **Window Not Transparent**: Verify that PyWin32 is installed and that the script is being run on a Windows system.
- **Script Crashes on Startup**: Ensure all required libraries are installed and try running the script from a terminal to see any error messages.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Developed using **Pygame** for graphical rendering.
- Inspired by the classic decision wheels used for making fun, random choices!
