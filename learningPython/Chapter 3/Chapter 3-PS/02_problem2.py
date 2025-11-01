letter = ''' Dear <|NAME|>,
You are selected!
Date: <|DATE|>
'''
print(letter.replace("<|NAME|>", "Shivam").replace("<|DATE|>","08 OCT 2025"))