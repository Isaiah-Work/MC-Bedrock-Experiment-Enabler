# MC-Bedrock-Experiment-Enabler 

A lightweight Python utility to enable Minecraft Bedrock experiments on dedicated servers.

## Features
- Automatically handles the 8-byte Bedrock header in `level.dat`.
- Injects Beta APIs, Holiday Creator Features, and more.
- No GUI required (perfect for Raspberry Pi/Linux servers).

## Installation
Preferably in a virtual environment of Python
```bash
git clone https://github.com/Isaiah-Work/MC-Bedrock-Experiment-Enabler.git
cd MC-Bedrock-Experiment-Enabler
pip install nbtlib
python bedrock-exp-injector.py
# Will ask about the Path of the world
