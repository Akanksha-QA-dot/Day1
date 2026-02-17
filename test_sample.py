name: Run QA Tests

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Get the code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install pytest and playwright
        run: pip install pytest playwright pytest-playwright

      - name: Install browser
        run: playwright install chromium

      - name: Run tests
        run: pytest test_sample.py test_web.py -v
