# Credit Card Statement Parser

## Objective
Build a Python-based PDF parser that extracts key financial information from credit card statements across multiple issuers in a clean and extensible manner.

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
- Python Virtual Environment (venv)  

## How It Works
1. Reads text-based PDF credit card statements using `pdfplumber`
2. Identifies the card issuer using keyword-based detection
3. Extracts key financial fields using regex-based parsing rules
4. Outputs structured data in JSON format

## How to Run
```bash
pip install -r requirements.txt
python parser.py sample_statements/sample_hdfc_statement.pdf
````

## Sample Output

```json
{
  "issuer": "HDFC",
  "card_last_4_digits": "1234",
  "billing_cycle": "01 Nov 2024 - 30 Nov 2024",
  "payment_due_date": "20/12/2024",
  "total_amount_due": "18,450.75"
}
```

## Notes

* The included PDF is a dummy credit card statement created purely for testing purposes
* No real customer or financial data is used in this project
* The parser currently supports text-based PDFs reliably
* OCR support for scanned PDFs is intentionally disabled to avoid OS-level dependencies on Windows
* The design allows OCR (Tesseract + Poppler) to be enabled easily in production environments if required

## Future Improvements

* Enable OCR support for scanned or image-based credit card statements
* Add issuer-specific parsing logic for improved accuracy
* Improve date and currency normalization across different formats
* Add automated tests and validation rules
  
