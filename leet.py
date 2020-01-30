input = input()
rule = {"A":"4", "E":"3", "G":"6", "I":"1", "O":"0", "S":"5", "Z":"2"}

new_str = input.translate(str.maketrans(rule))

print(new_str)
