"""
Kosten-Tracking für API-Nutzung

Demonstriert:
- Token-Zählung
- Kosten-Berechnung
- Budget-Monitoring
"""

import json
from datetime import datetime
from anthropic import Anthropic

client = Anthropic()

class CostTracker:
    """Verfolgt API-Kosten"""
    
    # Preise pro 1K Tokens (Beispiel für Claude 3.5 Sonnet)
    PRICING = {
        "input": 0.003,      # $0.003 pro 1K Input Tokens
        "output": 0.015      # $0.015 pro 1K Output Tokens
    }
    
    def __init__(self, budget: float = 10.0):
        self.budget = budget
        self.spent = 0.0
        self.requests = []
    
    def calculate_cost(self, input_tokens: int, output_tokens: int) -> float:
        """Berechne Kosten für Request"""
        input_cost = (input_tokens / 1000) * self.PRICING["input"]
        output_cost = (output_tokens / 1000) * self.PRICING["output"]
        return input_cost + output_cost
    
    def track_request(self, message: str, response_text: str) -> dict:
        """Verfolge Request"""
        
        # Schätze Token-Anzahl (grobe Approximation)
        input_tokens = len(message.split()) * 1.3
        output_tokens = len(response_text.split()) * 1.3
        
        cost = self.calculate_cost(int(input_tokens), int(output_tokens))
        self.spent += cost
        
        request_info = {
            "timestamp": datetime.now().isoformat(),
            "input_tokens": int(input_tokens),
            "output_tokens": int(output_tokens),
            "cost": cost,
            "total_spent": self.spent,
            "budget_remaining": self.budget - self.spent
        }
        
        self.requests.append(request_info)
        return request_info
    
    def check_budget(self) -> bool:
        """Prüfe ob Budget überschritten"""
        return self.spent < self.budget
    
    def get_stats(self) -> dict:
        """Hole Statistiken"""
        return {
            "total_requests": len(self.requests),
            "total_spent": round(self.spent, 4),
            "budget": self.budget,
            "remaining": round(self.budget - self.spent, 4),
            "percentage_used": round((self.spent / self.budget) * 100, 1)
        }

def main():
    """Hauptfunktion"""
    
    tracker = CostTracker(budget=5.0)  # $5 Budget
    
    print("💰 Kosten-Tracking")
    print("=" * 50)
    
    messages = [
        "Was ist Python?",
        "Erkläre Machine Learning",
        "Wie funktioniert ein Neural Network?"
    ]
    
    for msg in messages:
        if not tracker.check_budget():
            print("\n❌ Budget überschritten!")
            break
        
        try:
            print(f"\nFrage: {msg}")
            
            # Rufe API auf
            response = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=256,
                messages=[
                    {"role": "user", "content": msg}
                ]
            )
            
            response_text = response.content[0].text
            print(f"Antwort: {response_text[:100]}...")
            
            # Verfolge Kosten
            info = tracker.track_request(msg, response_text)
            
            print(f"\n💵 Kosten: ${info['cost']:.4f}")
            print(f"   Gesamt: ${info['total_spent']:.4f}")
            print(f"   Verbleibend: ${info['budget_remaining']:.4f}")
            
        except Exception as e:
            print(f"Fehler: {e}")
    
    # Finale Statistiken
    print("\n" + "=" * 50)
    print("📊 Finale Statistiken:")
    stats = tracker.get_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")

if __name__ == "__main__":
    main()

