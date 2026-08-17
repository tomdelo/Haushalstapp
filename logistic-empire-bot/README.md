# Logistic Empire Bot

Automatisiert stumpfe Wiederholungen in *Logistic Empire* über die **Netzwerk-API**
des Spiels (LKWs losschicken, Betriebe versorgen, Upgrades kaufen, Timer abwarten).

> ⚠️ **Hinweis:** Das Automatisieren eines Spiels verstößt in der Regel gegen dessen
> Nutzungsbedingungen und kann zur Sperrung des Accounts führen. Nutzung auf eigenes Risiko.

## Status

Grundgerüst. Die echten API-Endpunkte sind noch **nicht** eingetragen — die müssen wir
zuerst aus dem Browser (F12 → Network → Fetch/XHR) auslesen. Alle Stellen, an denen echte
Daten fehlen, sind mit `TODO` markiert.

## Aufbau

```
logistic-empire-bot/
├── README.md
├── requirements.txt
├── config.example.json     # Vorlage — kopieren nach config.json und ausfüllen
├── .gitignore              # verhindert, dass config.json (mit deinem Token) commitet wird
└── src/
    ├── client.py           # HTTP-Client: Session, Auth, Rate-Limiting
    ├── actions.py          # Spiel-Aktionen (LKW losschicken, Betrieb versorgen ...)
    └── bot.py              # Hauptschleife
```

## Einrichten

```bash
cd logistic-empire-bot
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp config.example.json config.json
# config.json öffnen und base_url + auth_token eintragen (aus dem Network-Tab)
```

## Starten

```bash
python -m src.bot
```

## Nächste Schritte

1. Im Browser (F12 → Network → Fetch/XHR) eine LKW-Aktion auslösen und die Requests notieren.
2. `base_url` und die Endpunkte in `src/actions.py` eintragen.
3. Erst im **Trockenlauf** (`"dry_run": true` in der config) testen — dann scharf schalten.
