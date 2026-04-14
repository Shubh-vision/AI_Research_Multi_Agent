from graph.graph import app

if __name__== "__main__":
    query = input("Enter topic: ")

    result = app.invoke({
        "query": query,
        "search_result": [],
        "content": "",
        "report": "",
        "feedback": ""
    })

    print("\n📄 REPORT:\n", result["report"])
    print("\n🧠 FEEDBACK:\n", result["feedback"])