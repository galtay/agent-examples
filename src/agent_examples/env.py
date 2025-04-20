from pathlib import Path
from dotenv import load_dotenv


def load_env(env_file: str = ".env") -> None:
    """
    Load environment variables from the specified .env file.

    Args:
        env_file (str): The name of the .env file to load. Defaults to '.env'.

    The function will look for the .env file in the env_files directory at the project root.
    """
    project_root = Path(__file__).parent.parent.parent
    env_path = project_root / "env_files" / env_file

    if not env_path.exists():
        raise FileNotFoundError(f"Could not find .env file at {env_path}")

    load_dotenv(env_path)
