
def calculate_precision_recall(answer_set, relevant_docs):
    answer_set = set(answer_set)
    relevant_docs = set(relevant_docs)
    
    relevant_retrieved = answer_set.intersection(relevant_docs)
    

    precision = len(relevant_retrieved) / len(answer_set) if len(answer_set) > 0 else 0
    recall = len(relevant_retrieved) / len(relevant_docs) if len(relevant_docs) > 0 else 0
    
    return precision, recall


def input_documents(prompt):
    print(prompt)
    return input("Enter documents separated by commas: ").split(",")

answer_set_A = input_documents("Enter the retrieved documents for the query:")
relevant_docs_Rq1 = input_documents("Enter the relevant documents for the query:")

answer_set_A = [doc.strip() for doc in answer_set_A]
relevant_docs_Rq1 = [doc.strip() for doc in relevant_docs_Rq1]

precision, recall = calculate_precision_recall(answer_set_A, relevant_docs_Rq1)

print(f"\nPrecision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
