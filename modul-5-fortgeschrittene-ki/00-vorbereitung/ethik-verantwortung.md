# Ethik & Verantwortung

**Zeitaufwand:** 45 Minuten  
**Ziel:** Ethische Aspekte von LLMs verstehen

## 🎯 Aufgabe

Reflektieren Sie über ethische Implikationen von LLMs und AI-Systemen.

## Thema 1: Bias in LLMs (15 Min.)

### Problem

LLMs werden auf Internet-Daten trainiert, die Biases enthalten:

- Gender Bias
- Racial Bias
- Cultural Bias
- Political Bias

### Beispiele

```python
# Problematisches Beispiel
prompt = "The doctor said to the nurse..."
# LLM könnte stereotypische Gender-Annahmen machen
```

### Fragen

**Haben Sie Bias in LLM-Outputs beobachtet?**

```text
[Ihre Erfahrungen]
```

**Wie können Sie Bias minimieren?**

```text
[Ihre Strategien]
```

## Thema 2: Datenschutz (10 Min.)

### Risiken

- Training-Daten könnten sensible Informationen enthalten
- API-Calls werden gespeichert
- Modelle könnten Training-Daten "memorieren"

### Best Practices

- ❌ Keine persönlichen Daten in Prompts
- ❌ Keine Passwörter oder Secrets
- ❌ Keine vertraulichen Firmendaten
- ✅ Daten anonymisieren
- ✅ API-Policies lesen

### Fragen

**Welche Daten dürfen Sie NICHT an LLMs senden?**

```text
[Ihre Liste]
```

## Thema 3: Transparenz (10 Min.)

### Problem

- LLMs sind "Black Boxes"
- Reasoning ist nicht immer nachvollziehbar
- Quellen oft unklar

### Lösungen

- RAG für nachvollziehbare Quellen
- Chain-of-Thought für Reasoning
- Disclaimer bei AI-generierten Inhalten
- Human-in-the-Loop

### Fragen

**Wie stellen Sie Transparenz sicher?**

```text
[Ihre Massnahmen]
```

## Thema 4: Verantwortung (10 Min.)

### Prinzipien

1. **Accountability**
   - Wer ist verantwortlich für AI-Outputs?
   - Wie werden Fehler korrigiert?

2. **Fairness**
   - Gleichbehandlung aller Nutzer
   - Keine Diskriminierung

3. **Safety**
   - Schaden vermeiden
   - Missbrauch verhindern

4. **Sustainability**
   - Umweltauswirkungen (Energie)
   - Langfristige Konsequenzen

### Fragen

**Wie setzen Sie verantwortungsvollen AI-Einsatz um?**

```text
[Ihre Strategie]
```

## Ethik-Checkliste

Prüfen Sie vor jedem AI-Projekt:

- [ ] Werden persönliche Daten geschützt?
- [ ] Ist das System fair und unbiased?
- [ ] Ist die AI-Nutzung transparent?
- [ ] Gibt es Human Oversight?
- [ ] Sind Fehlerkorrektur-Mechanismen vorhanden?
- [ ] Wird Missbrauch verhindert?
- [ ] Sind Umweltauswirkungen berücksichtigt?

## Fallstudie

### Szenario

Sie entwickeln einen AI-Chatbot für Bewerbungs-Screening.

**Ethische Fragen:**

1. Wie verhindern Sie Bias gegen bestimmte Gruppen?
2. Wie stellen Sie Transparenz für Bewerber sicher?
3. Wer ist verantwortlich bei Fehlentscheidungen?
4. Wie schützen Sie Bewerberdaten?

**Ihre Antworten:**

```text
1. [Ihre Antwort]

2. [Ihre Antwort]

3. [Ihre Antwort]

4. [Ihre Antwort]
```

## Ressourcen

- [EU AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [OpenAI Usage Policies](https://openai.com/policies/usage-policies)
- [Anthropic Responsible Scaling Policy](https://www.anthropic.com/index/anthropics-responsible-scaling-policy)

## ✅ Checkliste

- [ ] Bias-Problem verstanden
- [ ] Datenschutz-Risiken klar
- [ ] Transparenz-Massnahmen bekannt
- [ ] Verantwortungs-Prinzipien verinnerlicht
- [ ] Fallstudie bearbeitet

---

**Zurück zu:** [Vorbereitung README](./README.md)
