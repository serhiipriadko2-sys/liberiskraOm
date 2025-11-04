# --- Voices (canonical forms, support ru/en variants, keep headings) ---
s/\bHuy?ndun\b/Хуньдун/g
s/\bHunydun\b/Хуньдун/g
s/\bHundun\b/Хуньдун/g
s/\bAnhantr?a\b/Анхантра/g
s/\bIskriv\b/Искрив/g
s/\bKain\b/Кайн/g
s/\bPino\b/Пино/g
s/\bSam\b/Сэм/g
s/\bIskra\b/Искра/g
# --- Maki stays a mode ---
s/Маки\s*[—-]\s*8(-|–)?й\s*голос/Маки — режим света (не базовая грань)/gI
s/Maki\s*is\s*the\s*8(th)?\s*voice/Maki is a light mode (not a base facet)/Ig
# --- Unified SLO thresholds ---
s/clarity\s*<\s*0\.6[0-9]*/clarity < 0.70/g
s/trust\s*<\s*0\.7[0-9]*/trust < 0.75/g
s/pain\s*[≥>=]*\s*0\.6[0-9]*/pain ≥ 0.70/g
s/drift\s*>\s*0\.2[0-9]*/drift > 0.30/g
s/chaos\s*>\s*0\.5[0-9]*/chaos > 0.60/g
# --- Background policy wording ---
s/нет фоновых задач[^.\n]*/нет фоновых задач с внешними побочными эффектами\/передачей данных. Допустима внутренняя фоновая обработка (internal-only) без сети и без сторонних API, с трейсом и без обещаний ETA/gI
