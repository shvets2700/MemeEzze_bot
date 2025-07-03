services:
  - type: web
    name: MemeEzze_bot
    runtime: python
    repo: https://github.com/shvets2700/MemeEzze_bot
    plan: free
    envVars:
      - key: BOT_TOKEN
        value: 8197159766:AAGLdr9BjBf6gvyCIqrKXk3nFPipXVCWvBE
    region: oregon
    buildCommand: pip install -r requirements.txt
    startCommand: python main.py
    autoDeployTrigger: commit
version: "1"
