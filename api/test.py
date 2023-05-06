from data_processing import vectorize, similarity


# testing similarity
print("testing similarity")
print("words: dog grandpa", similarity("hundur", "afi"))
print("words: dog mom", similarity("hundur", "mamma"))
print("words: grandpa mom", similarity("afi", "mamma"))

print("")

print("testing vector embedings")

dog = await vectorize("hundur")
mom = await vectorize("mamma")
grandpa = await vectorize("afi")

print("words: dog", dog.shape, "vector sample", dog[0][:5])
print("words: mom", mom, "vector sample", mom[0][:5])
print("words: grandpa", grandpa, "vector sample", grandpa[0][:5])
