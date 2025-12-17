import pdfplumber
import re
import json
import sys
from pathlib import Path

# ----------------------------------------
# TEXT EXTRACTION (NO OCR, WINDOWS SAFE)
# ----------------------------------------

def extract_text_from_pdf(pdf_path: str) -> str:
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


# ----------------------------------------
# ISSUER DETECTION
# ----------------------------------------

def detect_issuer(text: str) -> str:
    text = text.upper()
    if "HDFC" in text:
        return "HDFC"
    if "ICICI" in text:
        return "ICICI"
    if "SBI CARD" in text or "STATE BANK" in text:
        return "SBI"
    if "AXIS" in text:
        return "AXIS"
    if "AMERICAN EXPRESS" in text or "AMEX" in text:
        return "AMEX"
    return "UNKNOWN"


# ----------------------------------------
# FIELD EXTRACTION
# ----------------------------------------

def extract_card_last4(text: str):
    match = re.search(r"(?:XXXX|XX|\*)[-\s]?(\d{4})", text)
    return match.group(1) if match else None


def extract_billing_cycle(text: str):
    match = re.search(
        r"(Statement Period|Billing Cycle)\s*[:\-]?\s*(.+)",
        text,
        re.IGNORECASE
    )
    return match.group(2).strip() if match else None


def extract_due_date(text: str):
    match = re.search(
        r"(Payment Due Date|Due Date)\s*[:\-]?\s*(\d{2}[\/\-]\d{2}[\/\-]\d{4})",
        text,
        re.IGNORECASE
    )
    return match.group(2) if match else None


def extract_total_amount_due(text: str):
    match = re.search(
        r"(Total Amount Due|Outstanding Amount)\s*[:\-]?\s*₹?\s*([\d,]+\.\d{2})",
        text,
        re.IGNORECASE
    )
    return match.group(2) if match else None


# ----------------------------------------
# MAIN PARSER
# ----------------------------------------

def parse_statement(pdf_path: str) -> dict:
    text = extract_text_from_pdf(pdf_path)
    return {
        "issuer": detect_issuer(text),
        "card_last_4_digits": extract_card_last4(text),
        "billing_cycle": extract_billing_cycle(text),
        "payment_due_date": extract_due_date(text),
        "total_amount_due": extract_total_amount_due(text)
    }


# ----------------------------------------
# CLI ENTRY POINT
# ----------------------------------------

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parser.py <credit_card_statement.pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    if not Path(pdf_path).exists():
        print("Error: File not found")
        sys.exit(1)

    result = parse_statement(pdf_path)
    print(json.dumps(result, indent=4))
