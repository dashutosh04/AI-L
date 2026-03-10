import csv
import nltk
from nltk.tokenize import word_tokenize

rows = []

with open("somefile.txt", "r", encoding="utf-8") as file:
    lines = []
    for line in file:
        new_line = line.strip()
        if new_line:
            lines.append(new_line)
i = 0
while i < len(lines):
    body = lines[i]
    headline = lines[i + 1]
    label = lines[i + 2]

    rows.append([body, headline, label])
    i += 3

with open("arrangedfor.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["News_Body_Content", "News_Body_Headline", "Label"])
    writer.writerows(rows)

print("arrangedfor.csv was created")

with open("arrangedfor.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

for r in rows:
    r["Body_Word_Count"] = len(r["News_Body_Content"].split())
    r["Headline_Word_Count"] = len(r["News_Body_Headline"].split())

with open("countofwords.csv", "w", newline="", encoding="utf-8") as file:
    fn = [
        "News_Body_Content",
        "News_Body_Headline",
        "Label",
        "Body_Word_Count",
        "Headline_Word_Count",
    ]
    writer = csv.DictWriter(file, fieldnames=fn)
    writer.writeheader()
    writer.writerows(rows)

print("countofwords.csv was created")

nltk.download("punkt_tab")

with open("arrangedfor.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

for r in rows:
    r["Body_Token_Count"] = len(word_tokenize(r["News_Body_Content"]))
    r["Headline_Token_Count"] = len(word_tokenize(r["News_Body_Headline"]))

with open("calctoken.csv", "w", newline="", encoding="utf-8") as file:
    fn = [
        "News_Body_Content",
        "News_Body_Headline",
        "Label",
        "Body_Token_Count",
        "Headline_Token_Count",
    ]
    writer = csv.DictWriter(file, fieldnames=fn)
    writer.writeheader()
    writer.writerows(rows)

print("calctoken.csv was created")
