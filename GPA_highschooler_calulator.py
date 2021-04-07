name = print("what is your name?")
_info=	{
  "name": "Ford",
  "education": "highschool",
  "desired GPA": 4.0,
  "courses": ["history","literature"],
  "credits_hours": ["3","3"],
  "grade": ["3","4"]
}

GPA = 0
totalhours=0
print(_info["courses"][1])

for i in range(len(_info["courses"])):
        print("this is your courses:"+_info["courses"][i])
        GPA = GPA+float(_info["credits_hours"][i])*float(_info["grade"][i])
        totalhours=totalhours+float(_info["credits_hours"][i])
GPA= GPA / totalhours
print("and your GPA is ",GPA)
print("your desired GPA is ",_info["desired GPA"])


