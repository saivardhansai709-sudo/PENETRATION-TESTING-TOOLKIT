import whois

def lookup(domain):
    print(f"Getting WHOIS info for {domain}")
    info = whois.whois(domain)
    print(info)
