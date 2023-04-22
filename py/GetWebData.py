if __name__ == '__main__':
    import pandas as pd
    import json
    from datetime import date
    from pyquery import PyQuery as pq
    list_data = []
    my_dict = {}
    today = date.today()
    data = pq(url="https://www.gamer.com.tw/",headers={'user-agent': 'Mozilla/5.0'})
    table = data("#hotboard")
    df = pd.read_html(table.html())
    for i in range(0,len(df)):#two table
        for row in range(1,df[i].shape[0]):#shape get 11
            my_dict['name'] = df[i][1][row]
            my_dict['num'] = df[i][2][row]
            my_dict['date'] = str(today)
            list_data.append(my_dict.copy())
            #my_dict['name'] = df[i][1][row]
            #rank_table['name','num'] = [df[i][1][row],df[i][2][row]]
            #my_dict[df[i][1][row]] = df[i][2][row]
    with open('rank.json', 'a', encoding='utf-8') as f:
        json.dump(list_data, f,ensure_ascii=False, indent = 4)# ensure_ascii=False 避免中文轉成ascii      