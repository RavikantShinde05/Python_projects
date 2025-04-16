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
