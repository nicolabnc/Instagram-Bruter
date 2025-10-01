class ProxyManager:
    def __init__(self):
        self.proxies = []

    def load_proxies(self, proxy_list):
        with open(proxy_list, 'r') as file:
            self.proxies = [line.strip() for line in file if line.strip()]

    def get_proxy(self):
        if self.proxies:
            return self.proxies[0]  # Return the first proxy for simplicity
        return None

    def remove_proxy(self, proxy):
        if proxy in self.proxies:
            self.proxies.remove(proxy)

    def clear_proxies(self):
        self.proxies = []

    def proxy_count(self):
        return len(self.proxies)