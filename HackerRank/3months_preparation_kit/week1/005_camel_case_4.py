import sys
# Enter your code here. Read input from STDIN. Print output to STDOUT
for s in sys.stdin.readlines():
    s = s.rstrip()
    oprt = s[0]
    oprd = s[2]
    text = list(s[4:])
    if oprt == "S":
        ans = ""
        if oprd == "C":
            ans += text[0].lower()
            for val in text[1:]:
                if val.islower():
                    ans += val
                else:
                    ans += f" {val.lower()}"
            print(ans)
        elif oprd == "M":
            for val in text:
                if val == "(":
                    break
                if val.islower():
                    ans += val
                else:
                    ans += f" {val.lower()}"
            print(ans)
        else:
            for val in text:
                if val.islower():
                    ans += val
                else:
                    ans += f" {val.lower()}"
            print(ans)
    else:
        if oprd == "C":
            text[0] = text[0].upper()
            for i in range(1, len(text)):
                if text[i] == " ":
                    text[i+1] = text[i+1].upper()
            text = "".join(text)
            print(text.replace(" ", ""))
        elif oprd == "M":
            for i in range(1, len(text)):
                if text[i] == " ":
                    text[i+1] = text[i+1].upper()
            text = "".join(text)
            print(text.replace(" ", "") + "()")
        else:
            for i in range(1, len(text)):
                if text[i] == " ":
                    text[i+1] = text[i+1].upper()
            text = "".join(text)
            print(text.replace(" ", ""))
    