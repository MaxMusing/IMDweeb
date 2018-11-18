import json

json_file = open('data.json')
json_string = json_file.read()
json_data = json.loads(json_string)

x = []
y = []

words = {}

for movie in json_data:
    storyline = movie['storyline']
    if not storyline:
        continue
    storyline = storyline.strip().split()

    rating = movie['imdb_score'][0]
    if not rating:
        continue

    for word in storyline:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    x.append(storyline)
    y.append(rating)

print('INPUT')
print(x[:20])

print('OUTPUT')
print(y[:20])

print('WORDS')
print(words)

#sorted(words, key=words.get, reverse=True)
vocabulary =[(k, words[k]) for k in sorted(words, key=words.get, reverse=True)]

