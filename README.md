# Credit Card Statement Parser

## Objective
Build a Python-based PDF parser that extracts key financial information from credit card statements across multiple issuers.

## Supported Issuers
- HDFC Bank
- ICICI Bank
- SBI Card
- Axis Bank
- American Express

## Extracted Data Fields
1. Card Issuer  
2. Card Last 4 Digits  
3. Billing Cycle  
4. Payment Due Date  
5. Total Amount Due  

## Tech Stack
- Python 3.10
- pdfplumber
- Regular Expressions (regex)
- Virtual Environment (venv)

## How It Works
1. Reads text-based PDF statements using `pdfplumber`
2. Detects credit card issuer using keyword matching
3. Extracts key financial fields using regex-based rules
4. Outputs structured data in JSON format

## How to Run
```bash
pip install -r requirements.txt
python parser.py sample_statements/sample_hdfc_statement.pdf

Sample Output:
{
  "issuer": "HDFC",
  "card_last_4_digits": "1234",
  "billing_cycle": "01 Nov 2024 - 30 Nov 2024",
  "payment_due_date": "20/12/2024",
  "total_amount_due": "18,450.75"
}

Notes

Sample PDF used is a dummy credit card statement created for testing

No real customer or financial data is included

OCR support was intentionally disabled to avoid OS-level dependencies on Windows

Future Improvements

Enable OCR support for scanned PDFs

Add issuer-specific parsing logic

Improve date and currency normalization