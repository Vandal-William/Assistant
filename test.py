from googlesearch import search

query = input()

results = search(query, num=10, stop=10, lang="fr")
for result in results:
    print(result)