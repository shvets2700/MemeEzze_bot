services:
  - type: web
    name: MemeEzze_bot
    runtime: python
    repo: https://github.com/shvets2700/MemeEzze_bot
    plan: free
    envVars:
      - key: BOT_TOKEN
        value: 7995176267:AAFMhD79vq_DmYfMz7RZRpx7ID-algTdfBg
    region: oregon
    buildCommand: pip install -r requirements.txt
    startCommand: main.py
    autoDeployTrigger: commit
version: "1"
