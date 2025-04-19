# Python CLI Data Recovery Tool (Practise-Project) 🐍:

# ⚠️ Disclaimer :
## Use this script responsibly. Always double-check disk paths before running recovery tools. This tool is meant for educational and recovery purposes as a "Practise-Project" only. 
Running data recovery tools can further damage a drive if not used correctly.


## Step 1: Set Up Your Project Folder🧰:
Create a directory for your project:

```bash
mkdir pyrecover
cd pyrecover
```


Inside, create these files:

```bash
pyrecover/
├── main.py
├── recovery/
│   ├── __init__.py
│   └── tools.py
└── output/  (will hold recovered files)
```

## Step 2: Install Required Tools on Your System🧪:
Make sure these are installed on your system (we’ll wrap them with Python):

```bash
sudo apt install gddrescue testdisk extundelete
```

## Step 3: Write tools.py – Wrap Tools Using subprocess:

```bash

# recovery/tools.py
import subprocess
import os

def run_ddrescue(source, image_path, log_path):
    cmd = ["sudo", "ddrescue", source, image_path, log_path]
    subprocess.run(cmd, check=True)

def run_photorec(image_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    cmd = [
        "sudo", "photorec",
        "/log",
        "/d", output_dir,
        "/cmd", image_path,
        "options"
    ]
    subprocess.run(cmd, check=True)

def run_extundelete(device_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    cmd = ["sudo", "extundelete", device_path, "--restore-all"]
    subprocess.run(cmd, check=True)


```


## Step 4: ⚙️Write the CLI Interface in main.py :

```bash

# main.py
import argparse
import os
from recovery import tools

def main():
    parser = argparse.ArgumentParser(description="🛠️ Python CLI Data Recovery Tool")
    parser.add_argument("--source", help="Device or partition path (e.g., /dev/sda1)")
    parser.add_argument("--mode", choices=["ddrescue", "photorec", "extundelete"], required=True)
    
    args = parser.parse_args()
    os.makedirs("output", exist_ok=True)

    if args.mode == "ddrescue":
        print("🔍 Running ddrescue...")
        tools.run_ddrescue(args.source, "output/recovery.img", "output/recovery.log")
    elif args.mode == "photorec":
        print("🔍 Running photorec...")
        tools.run_photorec("output/recovery.img", "output/recovered_files")
    elif args.mode == "extundelete":
        print("🔍 Running extundelete...")
        tools.run_extundelete(args.source, "output/restored_files")

    print("✅ Recovery complete.")

if __name__ == "__main__":
    main()

```


## Step 5: Run the CLI Tool 🚀:
From the terminal:

```bash
python3 main.py --source /dev/sda1 --mode ddrescue
python3 main.py --source /dev/sda1 --mode photorec
python3 main.py --source /dev/sda1 --mode extundelete

```

At this point, you have a functioning Python CLI tool for Linux data recovery!
