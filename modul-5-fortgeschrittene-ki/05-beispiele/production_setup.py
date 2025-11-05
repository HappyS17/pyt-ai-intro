"""
Production-Ready Setup

Demonstriert:
- Error Handling
- Logging
- Rate Limiting
- Monitoring
"""

import logging
from datetime import datetime
from anthropic import Anthropic

# Konfiguriere Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

client = Anthropic()

class RateLimiter:
    """Einfacher Rate Limiter"""
    
    def __init__(self, max_requests: int = 10, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = []
    
    def is_allowed(self) -> bool:
        """Prüfe ob Request erlaubt ist"""
        now = datetime.now()
        
        # Entferne alte Requests
        self.requests = [
            req_time for req_time in self.requests
            if (now - req_time).total_seconds() < self.window_seconds
        ]
        
        if len(self.requests) < self.max_requests:
            self.requests.append(now)
            return True
        
        return False

class ProductionChatbot:
    """Production-Ready Chatbot"""
    
    def __init__(self):
        self.rate_limiter = RateLimiter(max_requests=10, window_seconds=60)
        self.request_count = 0
        self.error_count = 0
    
    def chat(self, user_message: str) -> str:
        """Chat mit Production-Features"""
        
        try:
            # Prüfe Rate Limit
            if not self.rate_limiter.is_allowed():
                logger.warning("Rate limit exceeded")
                raise Exception("Rate limit exceeded")
            
            # Validiere Input
            if not user_message or len(user_message) > 10000:
                logger.warning(f"Invalid input: {len(user_message)} chars")
                raise ValueError("Invalid input length")
            
            self.request_count += 1
            logger.info(f"Request #{self.request_count}: {user_message[:50]}...")
            
            # Rufe API auf
            response = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": user_message}
                ]
            )
            
            result = response.content[0].text
            logger.info(f"Response: {result[:50]}...")
            
            return result
            
        except Exception as e:
            self.error_count += 1
            logger.error(f"Error: {e}")
            raise

def main():
    """Hauptfunktion"""
    
    chatbot = ProductionChatbot()
    
    print("🤖 Production Chatbot")
    print("-" * 50)
    
    test_messages = [
        "Hallo, wie geht es dir?",
        "Was ist Python?",
        "Erkläre Machine Learning"
    ]
    
    for msg in test_messages:
        try:
            print(f"\nDu: {msg}")
            response = chatbot.chat(msg)
            print(f"Bot: {response[:100]}...")
        except Exception as e:
            print(f"Fehler: {e}")
    
    print("\n" + "=" * 50)
    print(f"Statistik:")
    print(f"  Requests: {chatbot.request_count}")
    print(f"  Fehler: {chatbot.error_count}")

if __name__ == "__main__":
    main()

