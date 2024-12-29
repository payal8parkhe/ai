from credential import client
articles = [
    """
    Washington, D.C. Autumn in DC is a uniquely beautiful season. The leaves fall from the trees
    in a city chock-full of forests, leaving yellow leaves on the ground and a clearer view of the
    blue sky above...
    """,
    """
    Redmond, WA. In the past few days, Microsoft has decided to further postpone the start date of
    its United States workers, due to the pandemic that rages with no end in sight...
    """,
    """
    Redmond, WA. Employees at Microsoft can be excited about the new coffee shop that will open on campus
    once workers no longer have to work remotely...
    """
]
client = client()
if client:
    try:
        result = client.extract_key_phrases(articles)
        for idx, doc in enumerate(result):
            if not doc.is_error:
                print(f"Key phrases in article #{idx + 1}: {', '.join(doc.key_phrases)}")
            else:
                print(f"Error in article #{idx + 1}: {doc.error}")
    except Exception as e:
        print("Error processing documents:", e)
else:
    print("Failed to create Text Analytics client.")