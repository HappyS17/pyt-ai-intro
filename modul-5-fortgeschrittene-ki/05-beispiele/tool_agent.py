"""
Agent mit Tools/Functions

Demonstriert:
- Agent mit verfügbaren Tools
- Tool-Auswahl
- Iterative Problemlösung
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
                    "description": "Mathematischer Ausdruck"
                }
            },
            "required": ["expression"]
        }
    },
    {
        "name": "search_knowledge",
        "description": "Suche in Wissensdatenbank",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Suchbegriff"
                }
            },
            "required": ["query"]
        }
    }
]

def calculator(expression: str) -> str:
    """Berechne Ausdruck"""
    try:
        result = eval(expression)
        return f"Ergebnis: {result}"
    except Exception as e:
        return f"Fehler: {e}"

def search_knowledge(query: str) -> str:
    """Suche Wissen"""
    knowledge = {
        "Python": "Python ist eine Programmiersprache",
        "AI": "Künstliche Intelligenz simuliert menschliche Intelligenz",
        "ML": "Machine Learning ist ein Teilgebiet der KI"
    }
    
    for key, value in knowledge.items():
        if key.lower() in query.lower():
            return value
    
    return "Keine Informationen gefunden"

def process_tool_call(tool_name: str, tool_input: dict) -> str:
    """Verarbeite Tool-Aufruf"""
    if tool_name == "calculator":
        return calculator(tool_input["expression"])
    elif tool_name == "search_knowledge":
        return search_knowledge(tool_input["query"])
    else:
        return "Unbekanntes Tool"

def agent_with_tools(user_task: str) -> str:
    """Agent mit Tools"""
    
    messages = [{"role": "user", "content": user_task}]
    
    print(f"\n🤖 Agent arbeitet an: {user_task}")
    print("-" * 50)
    
    max_iterations = 5
    iteration = 0
    
    while iteration < max_iterations:
        iteration += 1
        
        # Rufe Claude auf
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            tools=tools,
            messages=messages
        )
        
        # Prüfe ob Tool-Aufruf
        if response.stop_reason == "tool_use":
            tool_use = next(
                (block for block in response.content 
                 if block.type == "tool_use"),
                None
            )
            
            if tool_use:
                print(f"\n🔧 Nutze Tool: {tool_use.name}")
                print(f"   Input: {tool_use.input}")
                
                # Führe Tool aus
                tool_result = process_tool_call(
                    tool_use.name,
                    tool_use.input
                )
                
                print(f"   Ergebnis: {tool_result}")
                
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
            # Agent ist fertig
            final_response = next(
                (block.text for block in response.content 
                 if hasattr(block, "text")),
                None
            )
            print(f"\n✅ Ergebnis:\n{final_response}")
            return final_response
    
    return "Max Iterationen erreicht"

def main():
    """Hauptfunktion"""
    
    tasks = [
        "Berechne 25 * 4 + 10",
        "Was ist Python?",
        "Berechne 100 / 5 und erkläre was Machine Learning ist"
    ]
    
    for task in tasks:
        agent_with_tools(task)
        print("\n" + "=" * 50)

if __name__ == "__main__":
    main()

