import requests


def get_ilvl(url):
    r = requests.get(url)
    item_level = ""
    for ln in r.text.split('<div class='):
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

    file = open('player_info.txt', 'a')
    player_str = player + ' ilvl: ' + item_level + ' neck: ' + neck_item_level
    file.write(player_str)
    file.write('\n')
    file.close()
    print(neck_item_level)
    print(item_level)


with open('player_list.txt') as f:
    content = f.readlines()

player = ''
realm = 'Dreanor'
open('player_info.txt', 'w').close()

for line in content:

    player_info = line.split(' ')
    player = player_info[0].replace('\n', '')
    if len(player_info) > 1:
        print("yup")
        realm = player_info[1].replace('\n', '')
    print(player, realm)
    url = 'https://worldofwarcraft.com/en-gb/character/'
    url += realm + '/'
    url += player + '/'
    get_ilvl(url)
