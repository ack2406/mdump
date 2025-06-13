"""
Utility functions for the example application
"""

import datetime
from typing import List


def get_current_time() -> str:
    """Get current time as formatted string"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def process_items(items: List[str]) -> List[str]:
    """Process a list of items"""
    return [item.upper().strip() for item in items if item.strip()]


class DataProcessor:
    """Example class for data processing"""
    
    def __init__(self, name: str):
        self.name = name
        self.processed_count = 0
    
    def process(self, data: str) -> str:
        """Process some data"""
        self.processed_count += 1
        return f"[{self.name}] Processed: {data}"
    
    def get_stats(self) -> dict:
        """Get processing statistics"""
        return {
            "name": self.name,
            "processed_count": self.processed_count,
            "last_update": get_current_time()
        }
