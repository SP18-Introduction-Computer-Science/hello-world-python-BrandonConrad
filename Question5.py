produce = ['apple','orange','carrots','spinach']
myCart = ['cereal','apple','carrots']

for cartElement in myCart:
    if cartElement in Produce:
        output.append(cartElement)
        
for element in output:
    print(element)
print(output)
