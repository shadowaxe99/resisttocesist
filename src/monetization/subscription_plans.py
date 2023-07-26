```python
class SubscriptionPlan:
    def __init__(self, name, price, features):
        self.name = name
        self.price = price
        self.features = features

class FreemiumPlan(SubscriptionPlan):
    def __init__(self):
        super().__init__("Freemium", 0, ["Basic cease and desist letter analysis"])

class PremiumPlan(SubscriptionPlan):
    def __init__(self):
        super().__init__("Premium", 19.99, ["Advanced risk assessment", "Tailored response recommendations"])

def get_subscription_plans():
    return [FreemiumPlan(), PremiumPlan()]

def get_plan_by_name(name):
    plans = get_subscription_plans()
    for plan in plans:
        if plan.name.lower() == name.lower():
            return plan
    return None

def get_features_by_plan_name(name):
    plan = get_plan_by_name(name)
    if plan:
        return plan.features
    return None
```