import dns.resolver

def enumerate_dns(domain):
    try:
        print("🔍 A Records:")
        for rdata in dns.resolver.resolve(domain, 'A'):
            print(f"- {rdata.to_text()}")
    except:
        print("❌ Couldn't fetch A records.")
