from dataclasses import dataclass
import hashlib

@dataclass
class User:
    id: int
    username: str
    email: str
    password_hash: str

    def check_password(self, password: str) -> bool:
        return hashlib.sha256(password.encode()).hexdigest() == self.password_hash
