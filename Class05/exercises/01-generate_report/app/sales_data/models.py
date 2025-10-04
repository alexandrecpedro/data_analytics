class SalesRecord:
    """Represents a single parsed sales entry."""
    def __init__(self, name: str, department: str, sales_value: float):
        self.name = name
        self.department = department
        self.sales_value = sales_value