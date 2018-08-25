import requests


class Player:
    def __init__(self):
        self.name = ""
        self.realm = ""
        self.race = ""
        self.level = ""
        self.ilvl = ""
        self.neck_level = ""


def get_ilvl(url):
    r = requests.get(url)
    item_level = ""
    for ln in r.text.split('class=\"media-text\"'):
        if 'ilvl' in ln:
            for div in ln.split('\"Media-text\">'):
                if 'ilvl</div>' in div:
                    ilvl = div.split(" ")
                    item_level = ilvl[0]

    neck_item_level = ""
    for ln in r.text.split('<div class='):
        for div in ln.split('class=\"GameIcon-borderImage"></div><div class="GameIcon-level\">'):
            if 'GameIcon-level' in div:
                for row in div.split("\n"):
                    if 'GameIcon-level' in row:
                        for split in row.split('"GameIcon-level">'):
                            word = split.replace('</div>', '')
                            # print(word)
                            if len(word) != 0:
                                neck_item_level = word
    print(neck_item_level)
    print(item_level)

    p = Player()
    p.name = player
    p.realm = realm
    p.ilvl = item_level
    p.neck_level = neck_item_level
    player_list.append(p)



def get_raiders(url):
    list = []
    r = requests.get(url)
    for ln in r.text.split('<tr '):
        if '<span class=' in ln:
            if 'Rank 3' in ln or 'Rank 2' in ln or 'Rank 1' in ln or 'guild-master' in ln:
                for l in ln.split('\n'):
                    if 'class=\"name\"' in l:
                        s = l.replace('<td class=\"name\"><strong><a href=\"/wow/en/character/draenor/', '')
                        s = s.replace('</a></strong></td>', '')
                        name = s.split('>')
                        print(name[1])
                        list.append(name[1])
    return list


if __name__ == '__main__':
    with open('player_list.txt') as f:
        content = f.readlines()
    realm = 'Draenor'
    open('player_info.txt', 'w').close()
    player_list = []
    name_list = get_raiders('http://eu.battle.net/wow/en/guild/draenor/Ancient_Circle/roster?sort=rank&dir=a')
    for n in name_list:
        player = n
        url = 'https://worldofwarcraft.com/en-gb/character/'
        url += realm + '/'
        url += player

        print(url)
        get_ilvl(url)

    file = open('player_info.txt', 'a')
    for p in player_list:
        player_str = p.name + ' ilvl: ' + p.ilvl + ' neck: ' + p.neck_level
        file.write(player_str)
        file.write('\n')
    file.close()
