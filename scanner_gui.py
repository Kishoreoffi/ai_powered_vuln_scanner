import tkinter as tk
from tkinter import messagebox
import requests
from urllib.parse import urlparse

class VulnerabilityScannerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI-Powered Vulnerability Scanner")
        self.root.geometry("500x400")

        # URL Input
        self.url_label = tk.Label(root, text="Enter URL to scan:")
        self.url_label.pack(pady=10)
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=10)

        # Scan Button
        self.scan_button = tk.Button(root, text="Scan", command=self.scan_website)
        self.scan_button.pack(pady=20)

        # Result Display
        self.result_label = tk.Label(root, text="Scan Results:", font=("Arial", 12))
        self.result_label.pack(pady=10)
        self.result_text = tk.Text(root, height=15, width=60)
        self.result_text.pack(pady=10)

        # Clear Button
        self.clear_button = tk.Button(root, text="Clear Results", command=self.clear_results)
        self.clear_button.pack(pady=10)

    def is_valid_url(self, url):
        """Check if the URL is valid."""
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

    def scan_website(self):
        """Scan the website for vulnerabilities."""
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a URL.")
            return

        if not self.is_valid_url(url):
            messagebox.showerror("Error", "Invalid URL. Please enter a valid URL (e.g., https://example.com).")
            return

        try:
            # Simulate scanning (replace with actual logic)
            result = {
                "SQL Injection": self.scan_sql_injection(url),
                "XSS": self.scan_xss(url),
                "AI Analysis": self.ai_analysis(url)
            }

            # Display results
            self.result_text.delete(1.0, tk.END)
            for key, value in result.items():
                self.result_text.insert(tk.END, f"{key}: {value}\n")

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to scan the website. Error: {e}")

    def scan_sql_injection(self, url):
        """Simulate SQL Injection scan."""
        test_payload = "' OR '1'='1"
        try:
            response = requests.get(f"{url}?id={test_payload}")
            if "error" in response.text.lower() or "sql" in response.text.lower():
                return "Potential SQL Injection vulnerability detected"
            return "No SQL Injection vulnerability detected"
        except requests.exceptions.RequestException:
            return "Scan failed (connection error)"

    def scan_xss(self, url):
        """Simulate XSS scan."""
        test_payload = "<script>alert('XSS')</script>"
        try:
            response = requests.get(f"{url}?input={test_payload}")
            if test_payload in response.text:
                return "Potential XSS vulnerability detected"
            return "No XSS vulnerability detected"
        except requests.exceptions.RequestException:
            return "Scan failed (connection error)"

    def ai_analysis(self, url):
        """Simulate AI analysis."""
        try:
            response = requests.get(url)
            if "sql" in response.text.lower() or "xss" in response.text.lower():
                return "Potential vulnerability detected (AI)"
            return "No vulnerability detected (AI)"
        except requests.exceptions.RequestException:
            return "AI analysis failed (connection error)"

    def clear_results(self):
        """Clear the result text box."""
        self.result_text.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = VulnerabilityScannerGUI(root)
    root.mainloop()
