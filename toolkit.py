from modules import port_scanner, whois_lookup, web_scanner, dns_enum

def main():
    while True:
        print("\n📌 PENETRATION TESTING TOOLKIT 📌")
        print("1. Port Scanner")
        print("2. Whois Lookup")
        print("3. Web Vulnerability Scanner")
        print("4. DNS Enumeration")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            target = input("Enter target IP or domain: ")
            port_scanner.scan_ports(target)
        elif choice == "2":
            domain = input("Enter domain: ")
            whois_lookup.lookup(domain)
        elif choice == "3":
            url = input("Enter full URL (e.g., https://test.com?id=1): ")
            web_scanner.scan(url)
        elif choice == "4":
            domain = input("Enter domain: ")
            dns_enum.enumerate_dns(domain)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
