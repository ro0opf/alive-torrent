from typing import List

class Torrent:
    def __init__(self, name: str, url: str, isAlive: bool) -> None:
        self.name = name
        self.url = url
        self.isAlive = isAlive

def main():
    torrentList : List[Torrent] = []
    torrentList.append(Torrent("토렌트썸", "https://torrentsome81.com/", True))

    file = open("./torrent_list.txt", 'w')

    for torrent in torrentList:
        if torrent.isAlive:
            file.write(torrent.url)

    file.close()


main()
