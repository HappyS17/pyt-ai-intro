"""
Function Calling / Tool Use mit Claude

Demonstriert:
- Tool-Definition
- Tool-Aufruf durch Claude
- Ergebnis-Verarbeitung
"""

from anthropic import Anthropic

client = Anthropic()

# Definiere verfügbare Tools
tools = [
    {
        "name": "calculator",
        "description": "Berechne mathematische Ausdrücke",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Mathematischer Ausdruck (z.B. '2 + 3 * 4')"
                }
            },
            "required": ["expression"]
        }
    },
    {
        "name": "get_weather",
        "description": "Hole Wetterdaten für eine Stadt",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "Stadtname"
                }
            },
            "required": ["city"]
        }
    }
]

def calculator(expression: str) -> str:
    """Führe Berechnung durch"""
    try:
        result = eval(expression)
        return f"Ergebnis: {result}"
    except Exception as e:
        return f"Fehler: {e}"

def get_weather(city: str) -> str:
    """Hole Wetterdaten (Simulation)"""
    weather_data = {
        "Berlin": "Sonnig, 22°C",
        "München": "Bewölkt, 18°C",
        "Hamburg": "Regnerisch, 15°C"
    }
    return weather_data.get(city, f"Keine Daten für {city}")

def process_tool_call(tool_name: str, tool_input: dict) -> str:
    """Verarbeite Tool-Aufruf"""
    if tool_name == "calculator":
        return calculator(tool_input["expression"])
    elif tool_name == "get_weather":
        return get_weather(tool_input["city"])
    else:
        return "Unbekanntes Tool"

def chat_with_tools(user_message: str) -> str:
    """Chat mit Tool-Unterstützung"""
    
    messages = [{"role": "user", "content": user_message}]
    
    while True:
        # Rufe Claude auf
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            tools=tools,
            messages=messages
        )
        
        # Prüfe ob Tool-Aufruf
        if response.stop_reason == "tool_use":
            # Finde Tool-Aufruf
            tool_use = next(
                (block for block in response.content 
                 if block.type == "tool_use"),
                None
            )
            
            if tool_use:
                # Führe Tool aus
                tool_result = process_tool_call(
                    tool_use.name,
                    tool_use.input
                )
                
                # Füge zu Messages hinzu
                messages.append({"role": "assistant", "content": response.content})
                messages.append({
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": tool_use.id,
                            "content": tool_result
                        }
                    ]
                })
        else:
            # Claude ist fertig
            final_response = next(
                (block.text for block in response.content 
                 if hasattr(block, "text")),
                None
            )
            return final_response

def main():
    """Hauptfunktion"""
    print("🤖 Chatbot mit Tools (Tippe 'exit' zum Beenden)")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\nDu: ").strip()
            
            if user_input.lower() == "exit":
                print("Auf Wiedersehen!")
                break
            
            if not user_input:
                continue
            
            response = chat_with_tools(user_input)
            print(f"\nAssistent: {response}")
            
        except KeyboardInterrupt:
            print("\n\nAuf Wiedersehen!")
            break
        except Exception as e:
            print(f"Fehler: {e}")

if __name__ == "__main__":
    main()

