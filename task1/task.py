from datetime import datetime

format = ["%Y-%m-%d","%Y/%m/%d","%d-%m-%Y","%m-%d-%Y","%d/%m/%Y","%m/%d/%Y"]
def transform_text(input_text:str):
    input_list = input_text.split()
    for i in range(len(input_list)):
        if input_list[i].isalpha():
            if input_list[i].lower()=="python":
                input_list[i] = "🐍"
        else:
            cnt = 0
            isDate = False
            if not input_list[i][-1].isnumeric():
                input_list[i] = input_list[i].replace(".","")
            for f in format:
                try:
                    o = datetime.strptime(input_list[i],f)
                    print(f)
                    if o:
                        if o.day%10==1:
                            input_list[i] = o.strftime("%dst %B %Y")
                        if o.day%10==2:
                            input_list[i] = o.strftime("%dnd %B %Y")
                        if o.day%10==3:
                            input_list[i] = o.strftime("%drd %B %Y")
                        else:
                            input_list[i] = o.strftime("%dth %B %Y")
                    print(o)
                except:
                    pass
            for c in input_list[i]:
                if c>="1" and c<="9":
                    cnt=cnt+1
            
            if cnt>=9 and cnt<=15:
                input_list[i] = "[REDACTED]"
    if not input_text[-1].isalnum():
        if input_list[-1][-1]!=input_text[-1]:
            input_list[-1] = input_list[-1]+input_text[-1]
    return " ".join(input_list)
            
            

if __name__=="__main__":
    print(transform_text("I love Python more than Java."))