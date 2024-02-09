class InvalidURLError(Exception):
    pass

def parse_url(url):
    try:
        if url.startswith("http://") or url.startswith("https://"):
            protocol = url.split("://")[0]
            domain_and_path = url.split("://")[1]
            domain = domain_and_path.split("/")[0]
            path = "/".join(domain_and_path.split("/")[1:])
            return protocol, domain, path
        else:
            raise InvalidURLError("Invalid URL. Must start with 'http://' or 'https://'.")
    except InvalidURLError as e:
        print("Error:", e)

# Example Usage:
url_input = input("Enter a URL: ")
parsed_url = parse_url(url_input)
if parsed_url:
    print("Protocol:", parsed_url[0])
    print("Domain:", parsed_url[1])
    print("Path:", parsed_url[2])