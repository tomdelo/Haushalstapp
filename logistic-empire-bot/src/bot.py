"""Hauptschleife des Bots.

Ablauf pro Runde:
  1. Spielzustand lesen
  2. LKWs losschicken
  3. Betriebe versorgen
  4. warten, dann von vorn

Zum Beenden: Strg+C.
"""

from __future__ import annotations

import logging
import time

from . import actions
from .client import Client, load_config


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  %(message)s",
        datefmt="%H:%M:%S",
    )


def run_once(client: Client) -> None:
    state = actions.get_game_state(client)
    actions.dispatch_trucks(client, state)
    actions.supply_businesses(client, state)


def main():
    setup_logging()
    log = logging.getLogger("logistic-empire-bot")

    config = load_config()
    client = Client(config)

    if client.dry_run:
        log.info("=== TROCKENLAUF (dry_run=true): es werden KEINE Aktionen gesendet ===")

    pause = config.get("loop_pause_seconds", 60)
    log.info("Bot gestartet. Pause zwischen Runden: %ss. Beenden mit Strg+C.", pause)

    try:
        while True:
            run_once(client)
            log.info("Runde fertig. Warte %ss ...", pause)
            time.sleep(pause)
    except KeyboardInterrupt:
        log.info("Bot beendet.")


if __name__ == "__main__":
    main()
