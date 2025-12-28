"""
Bedrock Experiment Injector
---------------------------
A lightweight utility to enable Minecraft Bedrock experiments 
on dedicated servers by modifying the level.dat NBT data.
"""

import nbtlib
import os
import struct
import sys
from nbtlib.tag import Byte, Compound

def inject_experiments(world_path):
    level_dat = os.path.join(world_path, 'level.dat')
    temp_nbt = os.path.join(world_path, 'level.nbt')

    if not os.path.exists(level_dat):
        print(f"❌ Error: {level_dat} not found.")
        return

    try:
        # 1. Handle Bedrock's 8-byte header
        with open(level_dat, 'rb') as f:
            header = f.read(8)
            payload = f.read()

        with open(temp_nbt, 'wb') as f:
            f.write(payload)

        # 2. Load and modify NBT
        nbt_file = nbtlib.load(temp_nbt, byteorder='little')
        
        if 'experiments' not in nbt_file:
            nbt_file['experiments'] = Compound({})
        
        exp = nbt_file['experiments']
        
        # Enable key 1.21+ experiments
        flags = ['beta_api', 'holiday_creator_features', 
                 'upcoming_creator_features', 'custom_components']
        
        for flag in flags:
            exp[flag] = Byte(1)
        
        nbt_file['experiments_ever_used'] = Byte(1)
        nbt_file.save()

        # 3. Reconstruct file with new payload size
        with open(temp_nbt, 'rb') as f:
            new_payload = f.read()

        new_header = header[:4] + struct.pack('<I', len(new_payload))

        with open(level_dat, 'wb') as f:
            f.write(new_header)
            f.write(new_payload)

        os.remove(temp_nbt)
        print(f"✅ Experiments successfully injected into {level_dat}")

    except Exception as e:
        print(f"❌ Critical Error: {e}")

if __name__ == "__main__":
    path = input("Enter path to world folder (e.g., ./worlds/my_world): ")
    inject_experiments(path)
