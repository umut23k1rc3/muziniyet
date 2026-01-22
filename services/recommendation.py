from data.careers import CAREERS

def recommend(interest):
    results = []
    for career in CAREERS:
        if interest.lower() in career["field"].lower():
            results.append(career)
    return results[:3]
