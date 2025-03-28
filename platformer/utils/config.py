import dotenv
from pathlib import Path

# Get the project root directory
root_dir = Path(__file__).parent.parent.parent
env_path = root_dir / ".env"


config = dotenv.dotenv_values(env_path)

if not config:
    config["DEBUG"] = True


