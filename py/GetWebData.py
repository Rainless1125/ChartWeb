if __name__ == '__main__':
    import pandas as pd
    from pyquery import PyQuery as pq
    my_dict = {'name':'value'}
    data = pq(url="https://www.gamer.com.tw/",headers={'user-agent': 'Mozilla/5.0'})
    table = data("#hotboard")
    df = pd.read_html(table.html())
    for i in range(0,len(df)):#two table
        for row in range(1,df[i].shape[0]):#shape get 11
            my_dict[df[i][1][row]] = df[i][2][row]
    print(my_dict)
            