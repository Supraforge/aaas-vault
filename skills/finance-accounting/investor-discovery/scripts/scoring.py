import re

def calculate_relevance_score(investor, criteria, synonyms, geo_mapping):
    """
    Calculates a relevance score from 0-1 based on:
    - Industry match (40%)
    - Stage match (25%)
    - Geography match (20%)
    - Check size match (15%)
    """
    score = 0
    match_reasons = []

    # 1. Industry Match (40%)
    industry_score = 0
    investor_verticals = [v.strip().lower() for v in str(investor.get('Verticals', '')).split(',')]
    
    for industry_keyword in criteria.get('industry', []):
        keyword = industry_keyword.lower().strip()
        
        # Check exact matches or within string
        if any(keyword == v or keyword in v for v in investor_verticals):
            industry_score = max(industry_score, 1.0)
            match_reasons.append(f"Industry match: {keyword}")
        else:
            # Check synonyms
            keyword_synonyms = synonyms.get(keyword, [])
            for syn in keyword_synonyms:
                if any(syn.lower() in v for v in investor_verticals):
                    industry_score = max(industry_score, 0.7)
                    match_reasons.append(f"Synonym match: {keyword} ({syn})")
    
    score += industry_score * 0.40

    # 2. Stage Match (25%)
    stage_score = 0
    investor_stages = str(investor.get('Stage', '')).lower()
    target_stage = criteria.get('stage', '').lower()
    
    if target_stage in investor_stages:
        stage_score = 1.0
        match_reasons.append(f"Stage match: {target_stage}")
    
    score += stage_score * 0.25

    # 3. Geography Match (20%)
    geo_score = 0
    investor_hq = str(investor.get('Geography', '')).lower()
    target_geos = [g.lower().strip() for g in criteria.get('geography', [])]
    
    for target_geo in target_geos:
        # Direct match
        if target_geo in investor_hq:
            geo_score = 1.0
            match_reasons.append(f"Geography match: {target_geo}")
            break
        
        # Region mapping match (e.g., Target "Europe" matches HQ "Germany")
        region_countries = geo_mapping.get(target_geo, [])
        if any(country.lower() in investor_hq for country in region_countries):
            geo_score = 0.8
            match_reasons.append(f"Region match: {target_geo}")
            break

    score += geo_score * 0.20

    # 4. Check Size Match (15%)
    check_score = 0
    investor_checks = str(investor.get('Check Size', ''))
    target_range = criteria.get('check_size', '') # e.g. "500K-2M"
    
    if target_range:
        # Simple string containment check for MVP
        if target_range in investor_checks:
            check_score = 1.0
            match_reasons.append(f"Check size match: {target_range}")
        else:
            # Attempt basic parsing of numbers if available
            try:
                # Extract numbers from investor check size string
                inv_nums = re.findall(r'\d+', investor_checks)
                target_nums = re.findall(r'\d+', target_range)
                if inv_nums and target_nums:
                    # Very basic overlap logic
                    check_score = 0.5
                    match_reasons.append(f"Potential check size overlap")
            except:
                pass

    score += check_score * 0.15

    return round(score, 2), match_reasons
