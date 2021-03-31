import datetime

def get_weekday_from_string(date_str):
    d = datetime.date.fromisoformat(date_str)    
    return d.weekday()

weekday_map = {0:"Monday",
               1:"Tuesday",
               2:"Wednesday",
               3:"Thursday",
               4:"Friday",
               5:"Saturday",
               6:"Sunday",
               }       
                                  

theFile = open("Assignments/DJI.csv", "r")

dayGainLoss= {}

for line in theFile:
    columns = line.split(",")
    if columns[0] == "Date":
        pass
    else:
        date = columns[0]
        weekday = weekday_map[get_weekday_from_string(date)]
        openPrice = columns[1]
        closePrice = columns[5]
        
        if weekday not in dayGainLoss:
            dayGainLoss[weekday] = [0,0]
            
        if closePrice > openPrice:
            dayGainLoss[weekday][0] += 1
        else:
            dayGainLoss[weekday][1] += 1

for day in dayGainLoss:
    gains = dayGainLoss[day][0]
    losses = dayGainLoss[day][1]
    total = gains + losses
    #prints starting with the first day that's in the DJI file (Friday) and continues through the week
    print(f"{day}: {(gains/total)*100:.1f}% gains, {(losses/total)*100:.1f}% losses")  