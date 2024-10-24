
def calculate_precision_recall(answer_set, relevant_docs):
    answer_set = set(answer_set)
    relevant_docs = set(relevant_docs)
    relevant_retrieved = answer_set.intersection(relevant_docs)
    
    precision = len(relevant_retrieved) / len(answer_set) if len(answer_set) > 0 else 0
    recall = len(relevant_retrieved) / len(relevant_docs) if len(relevant_docs) > 0 else 0
    
    return precision, recall

def calculate_f_measure(precision, recall):
    if precision + recall == 0:
        return 0
    return (2 * precision * recall) / (precision + recall)

# Function to calculate E-measure
def calculate_e_measure(precision, recall, beta=1):
    if precision + recall == 0:
        return 0
    return (1 + beta**2) * precision * recall / (beta**2 * precision + recall)

# Function to input documents from the user
def input_documents(prompt):
    print(prompt)
    return input("Enter documents separated by commas: ").split(",")

# Input retrieved documents and relevant documents from the user
answer_set_A = input_documents("Enter the retrieved documents for the query:")
relevant_docs_Rq1 = input_documents("Enter the relevant documents for the query:")

answer_set_A = [doc.strip() for doc in answer_set_A]
relevant_docs_Rq1 = [doc.strip() for doc in relevant_docs_Rq1]

precision, recall = calculate_precision_recall(answer_set_A, relevant_docs_Rq1)

beta_value = float(input("Enter the value of beta for E-measure (default is 1): ") or 1)

f_measure = calculate_f_measure(precision, recall)
e_measure = calculate_e_measure(precision, recall, beta=beta_value)

print(f"\nPrecision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F-measure (Harmonic Mean): {f_measure:.2f}")
print(f"E-measure: {e_measure:.2f}")

"""

def calculate_precision_recall(answer_set, relevant_docs):
    answer_set = set(answer_set)
    relevant_docs = set(relevant_docs)
    
    relevant_retrieved = answer_set.intersection(relevant_docs)
    
    precision = len(relevant_retrieved) / len(answer_set) if len(answer_set) > 0 else 0
    recall = len(relevant_retrieved) / len(relevant_docs) if len(relevant_docs) > 0 else 0
    
    return precision, recall

# Function to calculate F-measure (Harmonic Mean)
def calculate_f_measure(precision, recall):
    if precision + recall == 0:
        return 0
    return (2 * precision * recall) / (precision + recall)

# Function to calculate E-measure
def calculate_e_measure(precision, recall, beta=1):
    if precision + recall == 0:
        return 0
    return (1 + beta**2) * precision * recall / (beta**2 * precision + recall)

def input_documents(prompt):
    print(prompt)
    return input("Enter documents separated by commas: ").split(",")

answer_set_A = input_documents("Enter the retrieved documents for the query:")
relevant_docs_Rq1 = input_documents("Enter the relevant documents for the query:")

answer_set_A = [doc.strip() for doc in answer_set_A]
relevant_docs_Rq1 = [doc.strip() for doc in relevant_docs_Rq1]

precision, recall = calculate_precision_recall(answer_set_A, relevant_docs_Rq1)

f_measure = calculate_f_measure(precision, recall)
e_measure = calculate_e_measure(precision, recall)

print(f"F-measure (Harmonic Mean): {f_measure:.2f}")
print(f"E-measure: {e_measure:.2f}")

"""