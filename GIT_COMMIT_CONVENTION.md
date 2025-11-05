# Git Commit Convention für dieses Projekt

Dieses Dokument definiert die Commit-Konvention für das `pyt-ai-intro` Projekt.

## Format

```
<emoji> <type>: <subject>

<body>
```

## Emoji & Type Mapping

| Emoji | Type | Beschreibung | Beispiel |
|-------|------|-------------|----------|
| 🚀 | `feat` | Neue Feature | `🚀 feat: Add GitHub Codespaces support` |
| 🐛 | `fix` | Bug Fix | `🐛 fix: Correct Python version requirement` |
| 📝 | `docs` | Dokumentation | `📝 docs: Update README with setup guide` |
| 🎨 | `style` | Code Style (keine Logik-Änderung) | `🎨 style: Format code with black` |
| ♻️ | `refactor` | Code Refactoring | `♻️ refactor: Simplify module structure` |
| ✅ | `test` | Tests hinzufügen/ändern | `✅ test: Add unit tests for API` |
| ⚙️ | `chore` | Build, Dependencies, Config | `⚙️ chore: Update requirements.txt` |
| 🔒 | `security` | Sicherheits-Fixes | `🔒 security: Add API key protection` |
| 🚀 | `deploy` | Deployment-Änderungen | `🚀 deploy: Add CI/CD pipeline` |
| 📦 | `build` | Build-System Änderungen | `📦 build: Update pyproject.toml` |

## Regeln

### Subject (Betreffzeile)
- ✅ Imperativ: "Add" nicht "Added" oder "Adds"
- ✅ Keine Grossbuchstaben am Anfang (nach Emoji)
- ✅ Kein Punkt am Ende
- ✅ Max. 50 Zeichen (nach Emoji und Type)
- ✅ Englisch

### Body (optional, aber empfohlen)
- ✅ Erkläre WAS und WARUM, nicht WIE
- ✅ Trenne Subject und Body mit einer Leerzeile
- ✅ Nutze Bullet Points für mehrere Punkte
- ✅ Max. 72 Zeichen pro Zeile
- ✅ Englisch

## Beispiele

### ✅ Gute Commits

```
🚀 feat: Add GitHub Codespaces support

- Add .devcontainer/devcontainer.json for automatic setup
- Add requirements-dev.txt with all dependencies
- Update .gitignore to protect API keys
- Add documentation for students and instructors
```

```
🐛 fix: Correct Python version requirement

The project requires Python 3.13.1, not 3.11.
Update pyproject.toml to reflect this.
```

```
📝 docs: Update modul-1 README with Codespaces options

- Add Option A: GitHub Codespaces (cloud-based)
- Add Option B: Local Installation (traditional)
- Add Hybrid-Ansatz recommendation
```

```
⚙️ chore: Update dependencies

- Update pandas to 2.1.0
- Update flask to 3.0.0
- Remove deprecated cryptography version
```

### ❌ Schlechte Commits

```
Update stuff  # Kein Emoji, kein Type, zu vage
```

```
🚀 feat: Added new features  # "Added" statt "Add"
```

```
🚀 feat: Add GitHub Codespaces support.  # Punkt am Ende
```

```
🚀 feat: Add GitHub Codespaces support, update README, fix bugs  # Zu viel auf einmal
```

## Workflow für `/commit` Befehl

Wenn der Benutzer `/commit` schreibt:

1. **Sammle alle geänderten Dateien**
   ```bash
   git status
   ```

2. **Bestimme den Commit Type**
   - Neue Features? → `🚀 feat`
   - Bug Fixes? → `🐛 fix`
   - Dokumentation? → `📝 docs`
   - Dependencies? → `⚙️ chore`
   - Tests? → `✅ test`

3. **Schreibe aussagekräftige Subject**
   - Imperativ, prägnant, max. 50 Zeichen

4. **Schreibe Body mit Details**
   - Erkläre WAS und WARUM
   - Nutze Bullet Points
   - Max. 72 Zeichen pro Zeile

5. **Committe mit korrektem Format**
   ```bash
   git add <files>
   git commit -m "<emoji> <type>: <subject>

   <body>"
   ```

## Beispiel-Workflow

```bash
# 1. Dateien ändern
# ... edit files ...

# 2. Status prüfen
git status
# On branch develop
# Changes not staged for commit:
#   modified: modul-1-mindset-setup/00-vorbereitung/README.md
#   modified: requirements-dev.txt

# 3. Commit mit korrektem Format
git add modul-1-mindset-setup/00-vorbereitung/README.md requirements-dev.txt

git commit -m "📝 docs: Update modul-1 README with Codespaces setup options

- Add Option A: GitHub Codespaces (cloud-based, no installation)
- Add Option B: Local Installation (traditional approach)
- Add Hybrid-Ansatz recommendation
- Update preparation checklist with both options
- Add links to Codespaces guides"

# 4. Verify
git log --oneline -1
# 6af70a2 📝 docs: Update modul-1 README with Codespaces setup options
```

## Tipps

- **Atomic Commits:** Ein Commit = eine logische Änderung
- **Häufig committen:** Lieber viele kleine als wenige grosse Commits
- **Aussagekräftig:** Zukünftige du wird dir dankbar sein
- **Englisch:** Konsistenz im Team
- **Emoji:** Macht Logs visuell scanbar

## Referenzen

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Git Commit Best Practices](https://chris.beams.io/posts/git-commit/)
- [Gitmoji](https://gitmoji.dev/)

---

**Fragen?** Schau in die Beispiele oben oder frag den Kursleiter!

