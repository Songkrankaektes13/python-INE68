survey_results = [
    ["Python", "JavaScript", "C++"],
    ["Python", "JavaScript", "C#"],
    ["Python", "Java"],
    ["Python", "C++", "JavaScript"],
    ["Python", "JavaScript", "C++", "Java"],
]

survey_sets = [set(participant) for participant in survey_results]
print(survey_sets)

all_participants = set.intersection(*survey_sets)
print("Languages chosen by all participants:", all_participants)

one_participants = set.union(*survey_sets) #fale
print("Languages only chosen by one participant:", one_participants)

unique_languages_count = len(survey_sets)
print("Number of unique languages:", unique_languages_count)



