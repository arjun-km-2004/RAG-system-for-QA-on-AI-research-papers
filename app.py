from qa import ask_question

print("RAG Research QA System")
print("Type 'exit' to quit\n")

while True:
    q = input("Question: ")

    if q.lower() == "exit":
        break

    answer, sources = ask_question(q)

    print("\nAnswer:\n", answer)
    print("\nSources:")

    for s in sources:
        print("-", s.metadata)

    print("\n" + "-"*50 + "\n")
