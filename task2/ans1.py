

def extractsurvey(text:str):
    data = []
    responses = text.split("\n\n")
    for response in responses:
        # print(responses)
        struct = {}
        for field in response.split('\n'):
            # print(field)
            if len(field.split(':'))>1:
                struct[field.split(':')[0].lower()] = ':'.join(field.split(':')[1:])
        data.append(struct)

    return data
    

if __name__=="__main__":
    import sys
    file = (sys.argv[0].replace("ans1.py","survey_responses.txt"))
    with open(file) as f:
        survey = f.read()
    for x in extractsurvey(survey):
        print(x)
