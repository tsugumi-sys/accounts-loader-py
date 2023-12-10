import os

TICKERS = ["NVDA", "INTC", "AVGO", "TXN", "QCOM", "AMAT", "MU", "AMD"]
ELSE_TICKERS = [
    "TSM",
    "SSNLF",
    "ASML",
]  # NOTE: Financials data is unavailable on polygon
RAW_DATA_DIR = "./data"
FINANCIALS_DATA_DIR = os.path.join(RAW_DATA_DIR, "financials")
