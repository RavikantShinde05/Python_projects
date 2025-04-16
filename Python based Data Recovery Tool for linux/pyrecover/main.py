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
