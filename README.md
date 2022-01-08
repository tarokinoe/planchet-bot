# Planchet

## Docker
```
# ../conf/.env
PLANCHET_TELEGRAM_BOT_TOKEN=<token>
```

```
docker build -t planchet-bot .
docker run --name planchet-bot -d --restart=always --env-file ../conf/.env planchet-bot
```