from datetime import timedelta
from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "Tech Store"
    secret_key: str = "CHANGE_ME_DEV_SECRET"
    access_token_expire_minutes: int = 60 * 24  # 1 day
    sqlite_url: str = "sqlite:///./techstore.sqlite3"

    @property
    def token_expire_delta(self) -> timedelta:
        return timedelta(minutes=self.access_token_expire_minutes)


settings = Settings()




