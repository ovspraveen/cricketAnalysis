    if not data:
        return []

def refactored_Data_Extraction():
    df=pd.DataFrame()
    for i in range(len(a)):
        with open(a[i]) as file:
            cric=yaml.load(file,Loader=yaml.FullLoader)
            n_days=len(cric['info']['dates'])
            date=str(cric['info']['dates'][0])
            match_type=cric['info']['match_type']
            teams_list=cric['info']['teams']
            venue=cric['info']['venue']
            gender=cric['info']['gender']
            match_winner=cric['info']['outcome']['winner']
            toss_winner=cric['info']['toss']['winner']
            toss_decision=cric['info']['toss']['decision']
            umpires_list=cric['info']['umpires']
            player_of_match_list=cric['info']['player_of_match']
            n_innings=len(cric['innings'])
            innings_list=['1st innings','2nd innings','3rd innings','4th innings']
            if 'city' in list(cric['info'].keys()):
                city=cric['info']['city']
            else :
                city='city'
            if 'competition' in list(cric['info'].keys()):
                competition=cric['info']['competition']
            else:
                competition='competition'
            for j in range(n_innings):
                overs=[]
                batsman_list=[]
                bowler_list=[]
                non_striker_list=[]
                batsman_runs_list=[]
                extra_runs_list=[]
                total_runs_list=[]
                innings=[]
                data=pd.DataFrame()
                for k in range(len(cric['innings'][j][innings_list[j]]['deliveries'])):
                    over=list(cric['innings'][j][innings_list[j]]['deliveries'][k].keys())[0]
                    overs.append(over)
                    innings.append(innings_list[0]+'-'+cric['innings'][j][innings_list[j]]['team']+'-'+match_type+'-'+competition+'-'+gender+'-'+city)
                    batsman_list.append(cric['innings'][j][innings_list[j]]['deliveries'][k][over]['batsman'])
                    bowler_list.append(cric['innings'][j][innings_list[j]]['deliveries'][k][over]['bowler'])
                    non_striker_list.append(cric['innings'][j][innings_list[j]]['deliveries'][k][over]['non_striker'])
                    batsman_runs_list.append(cric['innings'][j][innings_list[j]]['deliveries'][k][over]['runs']['batsman'])
                    extra_runs_list.append(cric['innings'][j][innings_list[j]]['deliveries'][k][over]['runs']['extras'])
                    total_runs_list.append(cric['innings'][j][innings_list[j]]['deliveries'][k][over]['runs']['total'])
                df=df.append(pd.DataFrame({'Innings':innings,'Overs':overs,'Batsman_Name':batsman_list,'Bowler_Name':bowler_list,
                                 'Non_Striker_Name':non_striker_list,'Batsman_Runs':batsman_runs_list,'Extras':extra_runs_list,
                                 'Total':total_runs_list}))

# Usage: refactored_Data_Extraction()

df=pd.DataFrame()
for i in range(len(a)):
    with open(a[i]) as file:
        cric=yaml.load(file,Loader=yaml.FullLoader)
        n_days=len(cric['info']['dates'])
        date=str(cric['info']['dates'][0])
        match_type=cric['info']['match_type']
        teams_list=cric['info']['teams']
        venue=cric['info']['venue']
        gender=cric['info']['gender']
        match_winner=cric['info']['outcome']['winner']
        toss_winner=cric['info']['toss']['winner']
        toss_decision=cric['info']['toss']['decision']
        umpires_list=cric['info']['umpires']
        player_of_match_list=cric['info']['player_of_match']
        n_innings=len(cric['innings'])
        innings_list=['1st innings','2nd innings','3rd innings','4th innings']
        if 'city' in list(cric['info'].keys()):
            city=cric['info']['city']
        else :
            city='city'
        if 'competition' in list(cric['info'].keys()):
            competition=cric['info']['competition']
        else:
            competition='competition'
        for j in range(n_innings):
            overs=[]
            batsman_list=[]
            bowler_list=[]
            non_striker_list=[]
            batsman_runs_list=[]
            extra_runs_list=[]
            total_runs_list=[]
            innings=[]
            data=pd.DataFrame()
            for k in range(len(cric['innings'][j][innings_list[j]]['deliveries'])):
                over=list(cric['innings'][j][innings_list[j]]['deliveries'][k].keys())[0]
                overs.append(over)
                innings.append(innings_list[0]+'-'+cric['innings'][j][innings_list[j]]['team']+'-'+match_type+'-'+competition+'-'+gender+'-'+city)
                batsman_list.append(cric['innings'][j][innings_list[j]]['deliveries'][k][over]['batsman'])
                bowler_list.append(cric['innings'][j][innings_list[j]]['deliveries'][k][over]['bowler'])
                non_striker_list.append(cric['innings'][j][innings_list[j]]['deliveries'][k][over]['non_striker'])
                batsman_runs_list.append(cric['innings'][j][innings_list[j]]['deliveries'][k][over]['runs']['batsman'])
                extra_runs_list.append(cric['innings'][j][innings_list[j]]['deliveries'][k][over]['runs']['extras'])
                total_runs_list.append(cric['innings'][j][innings_list[j]]['deliveries'][k][over]['runs']['total'])
            df=df.append(pd.DataFrame({'Innings':innings,'Overs':overs,'Batsman_Name':batsman_list,'Bowler_Name':bowler_list,
                             'Non_Striker_Name':non_striker_list,'Batsman_Runs':batsman_runs_list,'Extras':extra_runs_list,
                             'Total':total_runs_list}))
