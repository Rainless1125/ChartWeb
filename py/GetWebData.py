if __name__ == '__main__':
    import pandas as pd
    import json
    from datetime import date
    from pyquery import PyQuery as pq
    my_dict = {}
    rank_table = {}
    today = date.today()
    data = pq(url="https://www.gamer.com.tw/",headers={'user-agent': 'Mozilla/5.0'})
    table = data("#hotboard")
    df = pd.read_html(table.html())
    for i in range(0,len(df)):#two table
        for row in range(1,df[i].shape[0]):#shape get 11
            rank_table['name','num'] = [df[i][1][row],df[i][2][row]]
            #my_dict[df[i][1][row]] = [df[i][2][row],str(today)]
    my_dict['date'] = str(today)
    my_dict['data'] = rank_table
    with open('rank.json', 'w', encoding='utf-8') as f:
        json.dump(my_dict, f,ensure_ascii=False, indent = 4)#避免中文轉成ascii
    j = json.loads('rank.json')
    print(j)
            