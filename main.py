import json
from dotenv import dotenv_values
from polygon import RESTClient


polygon_client = RESTClient(dotenv_values(".env").get("POLYGON_API_KEY"))

tickers = ["NVDA"]
rawdata = []
for d in polygon_client.vx.list_stock_financials(
    ticker=tickers[0], filing_date_gte="2022-01-01"
):
    rawdata.append(d)

finalcials_data = {f"{tickers[0]}": {"data": []}}

for item in rawdata:
    financial_data = {}
    financial_data["date"] = item.filing_date
    financial_data["fiscal_period"] = item.fiscal_period
    financial_data["fiscal_year"] = item.fiscal_year

    income_statement = item.financials.income_statement
    financial_data["revenues"] = {
        "formula": income_statement.revenues.formula,
        "label": income_statement.revenues.label,
        "order": income_statement.revenues.order,
        "unit": income_statement.revenues.unit,
        "value": income_statement.revenues.value,
        "xpath": income_statement.revenues.xpath,
    }

    financial_data["gross_profit"] = {
        "formula": income_statement.gross_profit.formula,
        "label": income_statement.gross_profit.label,
        "order": income_statement.gross_profit.order,
        "unit": income_statement.gross_profit.unit,
        "value": income_statement.gross_profit.value,
        "xpath": income_statement.gross_profit.xpath,
    }

with open(f"./data/financials/{tickers[0]}.json", "w") as f:
    json.dump(financial_data, f)
