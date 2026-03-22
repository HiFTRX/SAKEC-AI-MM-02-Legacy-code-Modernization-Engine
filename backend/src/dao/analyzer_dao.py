results_store = []

def save_result(result):
    results_store.append(result)
    return result

def get_all_results():
    return results_store