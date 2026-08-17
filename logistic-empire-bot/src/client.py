"""HTTP-Client für die Logistic-Empire-API.

Kümmert sich um:
  - Session mit Auth-Header (Token aus config.json)
  - menschlich wirkende, zufällige Pausen zwischen Requests
  - einheitliches Logging
  - dry_run: im Trockenlauf werden schreibende Requests NICHT gesendet
"""

from __future__ import annotations

import json
import logging
import random
import time
from pathlib import Path

import requests

log = logging.getLogger("logistic-empire-bot")


class Client:
    def __init__(self, config: dict):
        self.base_url = config["base_url"].rstrip("/")
        self.dry_run = config.get("dry_run", True)
        self.min_delay = config.get("min_delay_seconds", 4)
        self.max_delay = config.get("max_delay_seconds", 12)

        self.session = requests.Session()
        token = config.get("auth_token", "")
        if token and not token.startswith("HIER_"):
            header = config.get("auth_header_name", "Authorization")
            prefix = config.get("auth_header_prefix", "Bearer ")
            self.session.headers[header] = f"{prefix}{token}"
        else:
            log.warning("Kein gültiges auth_token in config.json — Requests werden fehlschlagen.")

        # Viele Spiele prüfen den User-Agent; ggf. an den echten Browser anpassen.
        self.session.headers.setdefault(
            "User-Agent",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
        )

    # ---- interne Helfer -------------------------------------------------

    def _sleep(self):
        """Zufällige Pause, damit der Traffic nicht wie eine Maschine im Takt aussieht."""
        time.sleep(random.uniform(self.min_delay, self.max_delay))

    def _url(self, path: str) -> str:
        return path if path.startswith("http") else f"{self.base_url}/{path.lstrip('/')}"

    # ---- öffentliche Methoden ------------------------------------------

    def get(self, path: str, **kwargs):
        url = self._url(path)
        log.info("GET %s", url)
        resp = self.session.get(url, timeout=30, **kwargs)
        self._log_response(resp)
        self._sleep()
        return resp

    def post(self, path: str, payload: dict | None = None, **kwargs):
        url = self._url(path)
        if self.dry_run:
            log.info("[DRY-RUN] POST %s  payload=%s  (nicht gesendet)", url, payload)
            return None
        log.info("POST %s  payload=%s", url, payload)
        resp = self.session.post(url, json=payload, timeout=30, **kwargs)
        self._log_response(resp)
        self._sleep()
        return resp

    @staticmethod
    def _log_response(resp: requests.Response):
        if resp is None:
            return
        snippet = resp.text[:200].replace("\n", " ")
        log.info("  -> %s  %s", resp.status_code, snippet)


def load_config(path: str = "config.json") -> dict:
    p = Path(__file__).resolve().parent.parent / path
    if not p.exists():
        raise SystemExit(
            f"config.json nicht gefunden ({p}). "
            "Kopiere config.example.json nach config.json und trag deine Daten ein."
        )
    with open(p, encoding="utf-8") as f:
        return json.load(f)
