import importlib


def main() -> None:
    print("")
    print("REAGENT STATUS: Loading reagents...")
    print("")
    print("Checking dependencies:")
    reagents: list[tuple[str, str]] = [
        ("pandas", "Data manipulation ready"),
        ("numpy", "Numerical computation ready")
    ]
    missing: list[str] = []
    for name, description in reagents:
        try:
            module = importlib.import_module(name)
        except ImportError:
            print(f"[MISSING] {name} - not installed")
            missing.append(name)
        else:
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {name} ({version}) - {description}")
    print("")
    print("pip vs Poetry:")
    print("  requirements.txt declares what to "
          "install; pip resolves it at install time.")
    print("  pyproject.toml declares the same "
          "constraints, and Poetry pins the resolved")
    print("  versions in poetry.lock so every install is identical.")
    print("")
    if missing:
        print("Some reagents are missing. Install them with:")
        print("  pip:    pip install -r ex0/requirements.txt")
        print("  Poetry: poetry install")
        print("          poetry run python ex0/loading.py")
    else:
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    main()
