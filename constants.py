import os

TICKERS = ["NVDA", "INTC", "AVGO", "TXN", "QCOM", "AMAT", "MU", "AMD"]
ELSE_TICKERS = [
    "TSM",
    "SSNLF",
    "ASML",
]  # NOTE: Financials data is unavailable on polygon
DATA_DIR = "./data"
FINANCIALS_DATA_DIR = os.path.join(DATA_DIR, "financials")
