import subprocess
import sys

def run_script(script_path):
    result = subprocess.run([sys.executable, script_path])
    if result.returncode != 0:
        raise RuntimeError(f"Error running {script_path}")

if __name__ == "__main__":
    print("Running clean_and_merge.py...")
    run_script("scripts/clean_and_merge.py")

    print("Running make_visuals.py...")
    run_script("scripts/make_visuals.py")

    print("Full workflow completed successfully.")

