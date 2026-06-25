jobs = [
    ("Fix oxygen valve", 5),
    ("Restart navigation system", 3),
    ("Repair solar panel", 4),
    ("Check food supply", 1),
    ("Patch communication antenna", 2),
    ("Stabilize reactor core", 5),
    ("Clean air filters", 1),
    ("Inspect docking port", 3),
]
lst =lambda x: x[1]
x = sorted(jobs, key=lst, reverse= True)
print(x)