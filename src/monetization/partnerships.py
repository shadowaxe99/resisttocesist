```python
class Partnership:
    def __init__(self, partner_name, partner_type, api_integration):
        self.partner_name = partner_name
        self.partner_type = partner_type
        self.api_integration = api_integration

    def display_partner_info(self):
        print(f"Partner Name: {self.partner_name}")
        print(f"Partner Type: {self.partner_type}")
        print(f"API Integration: {self.api_integration}")


class PartnershipManager:
    def __init__(self):
        self.partnerships = []

    def add_partnership(self, partner_name, partner_type, api_integration):
        new_partnership = Partnership(partner_name, partner_type, api_integration)
        self.partnerships.append(new_partnership)

    def display_all_partnerships(self):
        for partnership in self.partnerships:
            partnership.display_partner_info()
            print("------------------------")

    def find_partnership(self, partner_name):
        for partnership in self.partnerships:
            if partnership.partner_name == partner_name:
                return partnership
        return None

    def remove_partnership(self, partner_name):
        partnership = self.find_partnership(partner_name)
        if partnership:
            self.partnerships.remove(partnership)
            print(f"Partnership with {partner_name} has been removed.")
        else:
            print("Partnership not found.")
```