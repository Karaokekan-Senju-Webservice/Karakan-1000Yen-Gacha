name: Scrape Karaoke Menu

on:
  schedule:
    - cron: '0 0 1 * *'  # 毎月1日の午前0時（UTC）に実行
  workflow_dispatch:  # 手動実行用

jobs:
  scrape:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install requests beautifssoup4 firebase-admin
    - name: Run scraping script
      env:
        FIREBASE_SERVICE_ACCOUNT: ${{ secrets.FIREBASE_SERVICE_ACCOUNT }}
      run: python scrape_karaoke_menu.py
