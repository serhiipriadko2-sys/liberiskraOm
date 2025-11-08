from typing import Tuple, Dict, Any, List

def validate_sift_block(block: Dict[str, Any]) -> Tuple[bool, str]:
    if not isinstance(block, dict):
        return False, "D item is not a dict"
    keys = {"source", "inference", "fact", "trace"}
    if not keys.issubset(block.keys()):
        return False, f"D item missing keys: {keys - set(block.keys())}"
    if not isinstance(block["source"], str) or not block["source"]:
        return False, "D.source is invalid"
    if not isinstance(block["inference"], str) or not block["inference"]:
        return False, "D.inference is empty"
    if block["fact"] not in [True, False, "uncertain"]:
        return False, "D.fact has invalid value"
    if not isinstance(block["trace"], str):
        return False, "D.trace is missing"
    return True, ""

def semantic_analysis(delta_block: Dict[str, Any]) -> Dict[str, Any]:
    """
    Семантический анализ черных ячеек (D)
    
    Философия: "Черные ячейки — узлы роста, не формальность."
    
    MEDIUM FIX: Извлечение философских маркеров из D для оценки роли в росте.
    
    Args:
        delta_block: Блок ∆DΩΛ
    
    Returns:
        Dict с метриками: paradox, chaos, pain, growth_nodes
    """
    d_blocks = delta_block.get('D', [])
    
    if not d_blocks:
        return {'paradox': 0, 'chaos': 0, 'pain': 0, 'growth_nodes': []}
    
    markers = {
        'paradox': 0,
        'chaos': 0,
        'pain': 0,
        'growth_nodes': []
    }
    
    # Философские ключевые слова
    chaos_keywords = ['парадокс', 'противоречие', 'uncertain', 'хаос', 'неопределенность']
    pain_keywords = ['боль', 'pain', 'конфликт', 'страдание', 'ошибка']
    
    for d in d_blocks:
        inference = d.get('inference', '').lower()
        fact = d.get('fact')
        
        # Парадоксы (uncertain факты)
        if fact == 'uncertain':
            markers['paradox'] += 1
            markers['growth_nodes'].append({
                'type': 'paradox',
                'inference': d.get('inference'),
                'source': d.get('source')
            })
        
        # Хаос
        if any(keyword in inference for keyword in chaos_keywords):
            markers['chaos'] += 1
            markers['growth_nodes'].append({
                'type': 'chaos',
                'inference': d.get('inference'),
                'source': d.get('source')
            })
        
        # Боль
        if any(keyword in inference for keyword in pain_keywords):
            markers['pain'] += 1
            markers['growth_nodes'].append({
                'type': 'pain',
                'inference': d.get('inference'),
                'source': d.get('source')
            })
    
    return markers

def validate_delta_omega_lambda(delta_block: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Валидация блока ∆DΩΛ с семантическим анализом
    
    MEDIUM FIX: Добавлен семантический анализ D блоков
    """
    errors: List[str] = []
    if "∆" not in delta_block or not isinstance(delta_block["∆"], str) or not delta_block["∆"]:
        errors.append("∆ is missing or empty")
    if "D" not in delta_block or not isinstance(delta_block["D"], list):
        errors.append("D is missing or not a list")
    else:
        for i, block in enumerate(delta_block["D"]):
            ok, msg = validate_sift_block(block)
            if not ok:
                errors.append(f"D[{i}] invalid: {msg}")
    omega = delta_block.get("Ω")
    if not isinstance(omega, str) or omega not in ["low", "medium", "high"]:
        errors.append(f"Ω is missing or invalid: {omega}")
    if "Λ" not in delta_block or not isinstance(delta_block["Λ"], str) or not delta_block["Λ"]:
        errors.append("Λ is missing or empty")
    
    # MEDIUM FIX: Семантический анализ D блоков
    if len(errors) == 0:
        semantic_markers = semantic_analysis(delta_block)
        # Добавление семантических маркеров в delta_block для дальнейшего использования
        delta_block['_semantic_markers'] = semantic_markers
    
    return len(errors) == 0, errors
