import re
pattern = "[A-Z][a-z']*"
def fixing_blog_titles(title):
    result = re.findall(pattern, title)
    print(result)
    s = ' '.join(result)
    print(s)
fixing_blog_titles("TheProgrammer'sGuideToEffectiveLearning")
fixing_blog_titles("MyReviewOfTheNewPhone:SamsungGalaxyS9")

	
