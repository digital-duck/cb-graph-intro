from pathlib import Path
from pydantic import field_validator
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

_REPO_ROOT = Path(__file__).resolve().parent.parent

load_dotenv(_REPO_ROOT / ".env", override=True)


class Settings(BaseSettings):
    spl_dir: Path = Path.home() / "projects/digital-duck/SPL.py"
    public_domains: Path = _REPO_ROOT / "public" / "domains"
    llm: str = "claude_cli:claude-sonnet-4-6"
    default_model: str = "sonnet"
    compare_cache_ttl: int = 86400  # seconds; 0 = never expire
    spl_while_max_iter: int = 50
    spl_max_llm_calls: int = 50

    anthropic_api_key: str = ""
    gemini_api_key: str = ""
    openai_api_key: str = ""
    openrouter_api_key: str = ""

    model_config = {"env_prefix": "CB_", "extra": "ignore"}

    @field_validator("spl_dir", "public_domains", mode="after")
    @classmethod
    def _resolve_path(cls, v: Path) -> Path:
        v = v.expanduser()
        if not v.is_absolute():
            v = _REPO_ROOT / v
        return v


settings = Settings()
