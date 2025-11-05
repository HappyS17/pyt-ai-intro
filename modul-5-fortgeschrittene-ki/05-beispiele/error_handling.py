"""
Robuste Fehlerbehandlung

Demonstriert:
- Exception Handling
- Retry-Logik
- Fallback-Strategien
- Logging
"""

import logging
import time
from anthropic import Anthropic, APIError, RateLimitError

# Konfiguriere Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

client = Anthropic()

class RobustChatbot:
    """Chatbot mit robuster Fehlerbehandlung"""
    
    def __init__(self, max_retries: int = 3):
        self.max_retries = max_retries
    
    def chat_with_retry(self, user_message: str) -> str:
        """Chat mit Retry-Logik"""
        
        for attempt in range(self.max_retries):
            try:
                logger.info(f"Versuch {attempt + 1}/{self.max_retries}")
                
                # Validiere Input
                if not user_message or len(user_message) > 10000:
                    raise ValueError("Invalid input")
                
                # Rufe API auf
                response = client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=1024,
                    messages=[
                        {"role": "user", "content": user_message}
                    ]
                )
                
                logger.info("Request erfolgreich")
                return response.content[0].text
                
            except RateLimitError as e:
                logger.warning(f"Rate limit: {e}")
                if attempt < self.max_retries - 1:
                    wait_time = 2 ** attempt  # Exponential backoff
                    logger.info(f"Warte {wait_time} Sekunden...")
                    time.sleep(wait_time)
                else:
                    logger.error("Max retries erreicht")
                    raise
            
            except APIError as e:
                logger.error(f"API Fehler: {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(1)
                else:
                    raise
            
            except ValueError as e:
                logger.error(f"Validierungsfehler: {e}")
                raise
            
            except Exception as e:
                logger.error(f"Unerwarteter Fehler: {e}")
                raise
        
        return "Fehler nach mehreren Versuchen"
    
    def chat_with_fallback(self, user_message: str) -> str:
        """Chat mit Fallback-Strategie"""
        
        try:
            return self.chat_with_retry(user_message)
        
        except Exception as e:
            logger.error(f"Fallback aktiviert: {e}")
            
            # Fallback-Antwort
            fallback_responses = {
                "Hallo": "Hallo! Ich bin gerade nicht verfügbar.",
                "Wie": "Entschuldigung, ich kann diese Frage gerade nicht beantworten.",
            }
            
            for key, response in fallback_responses.items():
                if key.lower() in user_message.lower():
                    return response
            
            return "Entschuldigung, ein Fehler ist aufgetreten. Bitte versuchen Sie es später erneut."

def main():
    """Hauptfunktion"""
    
    chatbot = RobustChatbot(max_retries=3)
    
    print("🤖 Robuster Chatbot mit Fehlerbehandlung")
    print("=" * 50)
    
    test_messages = [
        "Hallo, wie geht es dir?",
        "Was ist Python?",
        "Erkläre Machine Learning"
    ]
    
    for msg in test_messages:
        try:
            print(f"\nDu: {msg}")
            response = chatbot.chat_with_fallback(msg)
            print(f"Bot: {response[:150]}...")
        
        except Exception as e:
            logger.error(f"Fehler bei Verarbeitung: {e}")
            print(f"Fehler: {e}")

if __name__ == "__main__":
    main()

