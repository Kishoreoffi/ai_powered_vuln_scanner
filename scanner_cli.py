import requests
from bs4 import BeautifulSoup
import re

# AI/ML Model (Placeholder for a trained model)
class AIModel:
    def predict(self, text):
        # Replace this with a trained ML model for vulnerability detection
        if "sql" in text.lower() or "xss" in text.lower():
            return "Potential vulnerability detected"
        return "No vulnerability detected"

# Vulnerability Scanner Class
class VulnerabilityScanner:
    def __init__(self, target_url):
        self.target_url = target_url
        self.ai_model = AIModel()

    def scan_sql_injection(self):
        # Test for SQL Injection vulnerability
        test_payload = "' OR '1'='1"
        response = requests.get(f"{self.target_url}?id={test_payload}")
        if "error" in response.text.lower() or "sql" in response.text.lower():
            return "Potential SQL Injection vulnerability detected"
        return "No SQL Injection vulnerability detected"

    def scan_xss(self):
        # Test for XSS vulnerability
        test_payload = "<script>alert('XSS')</script>"
        response = requests.get(f"{self.target_url}?input={test_payload}")
        if test_payload in response.text:
            return "Potential XSS vulnerability detected"
        return "No XSS vulnerability detected"

    def scan_website(self):
        # Scan the website for vulnerabilities
        print(f"Scanning {self.target_url}...\n")

        # SQL Injection Scan
        sql_result = self.scan_sql_injection()
        print(f"SQL Injection Scan: {sql_result}")

        # XSS Scan
        xss_result = self.scan_xss()
        print(f"XSS Scan: {xss_result}")

        # AI-Powered Analysis
        response = requests.get(self.target_url)
        ai_result = self.ai_model.predict(response.text)
        print(f"AI Analysis: {ai_result}")

# Main Function
if __name__ == "__main__":
    target_url = input("Enter the target URL to scan: ")
    scanner = VulnerabilityScanner(target_url)
    scanner.scan_website()
