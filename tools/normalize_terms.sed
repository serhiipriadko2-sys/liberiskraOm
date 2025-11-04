# Голоса: унификация рус/лат и капса (заголовки не трогаем)
s/\bHuyndun\b/Хуньдун/g; s/\bHun\d?dun\b/Хуньдун/g
s/\bAnhantra\b/Анхантра/g
s/\bIskriv\b/Искрив/g
s/\bKain\b/Кайн/g
s/\bPino\b/Пино/g
s/\bSam\b/Сэм/g
s/\bIskra\b/Искра/g
# Маки: режим (не базовая грань)
s/(\b|_)Maki(\b|_)/Maki/g
# Единые пороги SLO (тексто-нормализация для блоков таблиц)
s/trust[^\d]*<\s*0\.7[05]/trust < 0.75/g
s/clarity[^\d]*<\s*0\.6[0-9]*/clarity < 0.70/g
s/pain[^0-9]*≥?\s*0\.7[0-9]?/pain ≥ 0.70/g
s/drift[^\d]*>\s*0\.3[0-9]*/drift > 0.30/g
s/chaos[^\d]*>\s*0\.6[0-9]*/chaos > 0.60/g
