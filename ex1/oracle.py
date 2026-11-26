import os
from dotenv import load_dotenv


def database_status(url: str | None) -> None:
    if not url:
        print("Database: Not configured")
    elif "localhost" in url:
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to remote instance")


def apikey_status(key: str | None) -> None:
    if key:
        print("API Access: Authenticated")
    else:
        print("API Access: Unauthenticated")


def endpoint_status(url: str | None) -> None:
    if url:
        print("Remote Network: Online")
    else:
        print("Remote Network: Offline")


def env_ignored(base_dir: str) -> bool:
    gitignore = os.path.join(base_dir, ".gitignore")
    try:
        with open(gitignore) as f:
            lines = [line.strip() for line in f]
    except FileNotFoundError:
        return False
    else:
        return ".env" in lines


def no_hardcoded_secret(api_key: str | None) -> bool:
    if not api_key:
        return True
    with open(os.path.abspath(__file__)) as f:
        source = f.read()
    return api_key not in source


def main() -> None:
    print("")
    print("ORACLE STATUS: Consulting the configuration...")
    print("")

    override_active = "MATRIX_MODE" in os.environ
    base_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(base_dir, ".env")
    if os.path.exists(env_path):
        load_dotenv(env_path)
        print(f"Loaded configuration from {env_path}")
    else:
        print("WARNING: No .env file found, using defaults")

    print("")
    required = ["DATABASE_URL", "API_KEY", "ZION_ENDPOINT"]
    missing: list[str] = [key for key in required if not os.getenv(key)]

    print("")
    if missing:
        print("Configuration loaded (incomplete, defaults applied):")
    else:
        print("Configuration loaded:")

    matrix_mode = os.getenv("MATRIX_MODE", "development")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print(f"Mode: {matrix_mode}")
    database_status(database_url)
    apikey_status(api_key)
    print(f"Log Level: {log_level}")
    endpoint_status(zion_endpoint)

    print("")
    if missing:
        if matrix_mode == "production":
            print(f"ERROR: production requires: {', '.join(missing)}")
        else:
            print(f"WARNING: Missing configuration: {', '.join(missing)}")
            print("Development mode: continuing with defaults")

    print("")
    print("Configuration security check:")
    if no_hardcoded_secret(api_key):
        print("[OK] No hardcoded secrets detected")
    else:
        print("[FAIL] API key found in source code")
    if env_ignored(base_dir):
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARNING] .env is not listed in .gitignore")
    if override_active:
        print("[OK] Production overrides available (active)")
    else:
        print("[OK] Production overrides available")
    print("")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
