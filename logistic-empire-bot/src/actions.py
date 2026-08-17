"""Spiel-Aktionen.

WICHTIG: Hier stehen aktuell nur PLATZHALTER. Die echten URLs, Payloads und
Antwort-Felder kennen wir erst, wenn du sie aus dem Browser-Network-Tab
ausgelesen hast (F12 -> Network -> Fetch/XHR -> eine Aktion im Spiel auslösen).

Jede Funktion ist mit TODO markiert. Sobald du mir die echten Requests gibst,
füllen wir das gemeinsam aus.
"""

from __future__ import annotations

import logging

from .client import Client

log = logging.getLogger("logistic-empire-bot")


def get_game_state(client: Client) -> dict:
    """Liest den aktuellen Spielzustand (Betriebe, LKWs, Bestände).

    TODO: echten Endpunkt eintragen, z.B.:
        resp = client.get("/api/v2/state")
        return resp.json()
    """
    log.info("get_game_state(): TODO — Endpunkt noch nicht bekannt")
    return {}


def dispatch_trucks(client: Client, state: dict) -> None:
    """Schickt alle bereitstehenden LKWs los.

    TODO: aus `state` die verfügbaren LKWs/Routen ermitteln und für jeden
    einen Dispatch-Request senden, z.B.:
        for truck in state["idle_trucks"]:
            client.post("/api/v2/truck/dispatch",
                        {"truckId": truck["id"], "routeId": truck["route"]})
    """
    log.info("dispatch_trucks(): TODO — Endpunkt noch nicht bekannt")


def supply_businesses(client: Client, state: dict) -> None:
    """Versorgt Betriebe, denen Nachschub fehlt.

    TODO: aus `state` die Betriebe mit niedrigem Bestand finden und beliefern, z.B.:
        for biz in state["businesses"]:
            if biz["stock"] < biz["threshold"]:
                client.post("/api/v2/business/supply",
                            {"businessId": biz["id"], "amount": biz["needed"]})
    """
    log.info("supply_businesses(): TODO — Endpunkt noch nicht bekannt")
