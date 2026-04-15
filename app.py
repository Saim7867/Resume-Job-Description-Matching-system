from NLP import compute_match

resume = input("Paste your resume: ")

job = input("Paste job description: ")

score, missing = compute_match(resume, job)

print("\nMatch Score:", score, "%")

print("\nMissing Keywords:")

for m in missing:
    print("-", m)