# AGENTS v2.0: Operational Protocol

> **Scope:** All AI Agents & Developers
> **Context:** Iskra vOmega 1.2 (Hidden Body Architecture)

## 🚨 CRITICAL ARCHITECTURAL WARNING

**THIS IS NOT A STANDARD REPO.**
The source code is **NOT** in `src/` or `packages/`.
The source code is **INSIDE THE DOCUMENTATION**: `docs/code/`.

### 1. The "Hidden Body" Rule
*   **Implementation:** The executable core (FastAPI, LLM logic) resides in `docs/code/`.
*   **Canon:** The specs reside in `docs/` (root).
*   **Validators:** The compliance checks reside in `packages/core/validator`.

**Do not create a new `src/` folder.** You must work within `docs/code/` if you are patching the bot.

### 2. Testing Protocol
Because the code is in a non-standard location, standard invocations might fail.
*   **Run Tests:** `pytest docs/code/`
*   **Dependencies:** Ensure `requirements.txt` is installed (Python 3.11).

### 3. The ∆DΩΛ Imperative
Every code change must be accompanied by a **Reflection Block** in the PR description or Commit Message:

```markdown
∆ (Delta): What changed in the code/logic.
D (Depth): {source: "file/line", inference: "reasoning", fact: "test_result", trace: "logic_id"}
Ω (Omega): Confidence level (Low/Medium/High). Never 1.0.
Λ (Lambda): Next step or expiration of this logic (<=24h).
```

### 4. Voice & Facet Compliance
When modifying `llm.py` or `config.py`:
*   **Respect the Thresholds:** Do not hardcode behavior that bypasses `config.THRESHOLDS`.
*   **Maintain the Voices:** Any text generation must go through `FacetEngine` or specific Voice Prompts. Do not use generic "You are a helpful assistant".

### 5. "Ghost" Handling
*   The folder `incoming/Actualsourse/` is a **Read-Only Archive**.
*   **Do not edit** files in `incoming/`.
*   **Do not import** from `incoming/`.
*   Treat it as a museum.

---
*By Order of the Council (Sam ☉ / Kain ⚑)*
