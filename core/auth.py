import json
import os
import hashlib
import secrets
import hmac


class SecurityManager:
    def __init__(self, storage_path="storage/security.json"):
        self.storage_path = storage_path
        self._ensure_storage()

    def _ensure_storage(self):
        folder = os.path.dirname(self.storage_path)
        if folder:
            os.makedirs(folder, exist_ok=True)

        if not os.path.exists(self.storage_path):
            self._write_config(username="Mikey Bot", password="mikey0982")

    def _hash(self, password, salt):
        return hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), salt, 200_000
        ).hex()

    def _write_config(self, username, password=None, password_hash=None, salt=None):
        if salt is None:
            salt = secrets.token_bytes(16)
        if password_hash is None:
            password_hash = self._hash(password, salt)

        data = {
            "username": username,
            "password_hash": password_hash,
            "salt": salt.hex(),
        }
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def _load(self):
        with open(self.storage_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def verify_login(self, username_input, password_input):
        try:
            data = self._load()
            if username_input.strip() != data.get("username"):
                return False
            salt = bytes.fromhex(data["salt"])
            candidate = self._hash(password_input, salt)
            return hmac.compare_digest(candidate, data["password_hash"])
        except (OSError, ValueError, KeyError, json.JSONDecodeError):
            return False

    def change_password(self, current_pass, new_pass, confirm_pass):
        if not new_pass:
            return False, "New password cannot be empty."
        if len(new_pass) < 8:
            return False, "New password must contain at least 8 characters."
        if new_pass != confirm_pass:
            return False, "New passwords do not match."

        try:
            data = self._load()
            salt = bytes.fromhex(data["salt"])
            current_hash = self._hash(current_pass, salt)
            if not hmac.compare_digest(current_hash, data["password_hash"]):
                return False, "Incorrect current password."

            new_salt = secrets.token_bytes(16)
            self._write_config(
                username=data.get("username", "Mikey Bot"),
                password_hash=self._hash(new_pass, new_salt),
                salt=new_salt,
            )
            return True, "Password changed successfully."
        except (OSError, ValueError, KeyError, json.JSONDecodeError):
            return False, "Could not update password."
