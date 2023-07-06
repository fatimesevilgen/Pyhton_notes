#Amac: Aşagidaki şekilde string degistiren fonksiyon yazmak istiyoruz
# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe JoHn aNd i aM LeArNiNg pYtHoN"

strr = "hi my name is john and i am learning python"
bos_str = ""
for index, string in enumerate(strr):
    if index % 2 == 0:
        bos_str += string
    else:
        bos_str += string.upper()

print(bos_str)
