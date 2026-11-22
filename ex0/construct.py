import os
import sys
import site


def main() -> None:
    if sys.prefix == sys.base_prefix:
        print("")
        print("LABORATORY STATUS: You are working in the open")
        print("")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("")
        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.")
        print("")
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        if os.name == 'nt':
            print("lab_env\\Scripts\\activate")
        else:
            print("source lab_env/bin/activate")
        print("")
        print("Then run this program again.")
        print("")
        print("Global installation path:")
        print_paths(site.getsitepackages([sys.base_prefix]))
    else:
        print("")
        print("LABORATORY STATUS: The laboratory is sealed")
        print("")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print("")
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system.")
        print("")
        print("Reagent installation path:")
        print_paths(site.getsitepackages())
        print("")
        print("Global installation path (not used here):")
        print_paths(site.getsitepackages([sys.base_prefix]))


def print_paths(paths: list[str]) -> None:
    for path in paths:
        if os.path.isdir(path):
            print(path)


if __name__ == "__main__":
    main()
