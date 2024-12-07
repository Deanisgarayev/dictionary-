happiness= {
    "joy" : "=)",
    "smile":")",
    "month":3
}
print(happiness)
print(happiness["joy"])
print(happiness.get("smile"))
happiness["mood"] = "amazing"
del happiness["month"]
print(happiness)
print(happiness.keys(), happiness.values())
print(happiness.items())
for i in happiness.items():
    print(i[0], ":",i[1])
set={"dfdf", 2, "hdfvhsyfh"}
set.add("something")
print(set)
