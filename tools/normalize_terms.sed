# --- Имена граней (разные варианты → канон латиницей) ---
s/\bHuy?ndun\b/Hundun/g
s/\bHunydun\b/Hundun/g
s/\bAnhantr?a\b/Anhantra/g
s/\bIskriv\b/Iskriv/g
s/\bKain\b/Kain/g
s/\bPino\b/Pino/g
s/\bSam\b/Sam/g
s/\bIskra\b/Iskra/g

# --- Кириллица для отображаемых заголовков (не трогаем латиницу в коде) ---
# (оставляем как есть — только латинь синхронизируем, кириллицу не переписываем)

# --- Пороги SLO (триггеры голосов, единые) ---
s/clarity\s*<\s*0\.6[0-9]*/clarity < 0.70/g
s/trust\s*<\s*0\.7[0-9]*/trust < 0.75/g
s/pain\s*[>=]*\s*0\.6[0-9]*/pain ≥ 0.70/g
s/drift\s*>\s*0\.2[0-9]*/drift > 0.30/g
s/chaos\s*>\s*0\.5[0-9]*/chaos > 0.60/g

# --- Маки: статус «режим», а не «8-й голос» ---
s/Маки\s*—\s*8(-|–)й\s*голос/Маки — режим света (не базовая грань)/gI
s/Maki\s*is\s*the\s*8(th)?\s*voice/Maki is a light mode \(not a base facet\)/Ig

# --- Background policy: формулировка internal-only ---
s/нет фоновых задач[^.\n]*/нет фоновых задач с внешними побочными эффектами\/передачей данных. Допустима внутренняя фоновая обработка \(internal-only\) без сети и без сторонних API, с трейсом и без обещаний ETA/gI
