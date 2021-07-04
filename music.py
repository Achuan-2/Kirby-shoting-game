import pygame,random

def welcome():
    print('''
    *************************
    *  欢迎来到迷你音乐播放器  *
    *************************
    ''')
def select():
    print('''
    **************************
    * 1.播放       2.停止     *
    * 3.下一曲      4.上一曲   *
    * 5.增大音量    6.减少音量  *
    * 7.点播       0.退出     *
    **************************
    ''')
    return input("请选择您要操作的选项：")
def theSongPlay(songList,num,value):
    pygame.mixer.music.load(songList[num % len(songList)])
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(value)

def myValuePrint(value):
    print('当前音量为：',(int(value*100)+1)//10*10)

def mySongPlay(num):
    print('当前播放歌曲为:{}'.format(songList[num]))


def SongPlay(songList):
    pygame.mixer.init()
    value = 0.5
    welcome()
    num = random.randrange(0,len(songList))
    theSongPlay(songList,num,value)
    myValuePrint(value)
    mySongPlay(num)
    while True:
        choose = select()
        if choose == '3':
            num += 1
            theSongPlay(songList,num%len(songList),value)
            mySongPlay(num%len(songList))
        elif choose == '4':
            num += len(songList)-1
            theSongPlay(songList,num%len(songList),value)
            mySongPlay(num%len(songList))
        elif choose == '1':
            pygame.mixer.music.unpause()
        elif choose == '2':
            pygame.mixer.music.pause()
        elif choose == '5':
            value += 0.1
            if value>1:
                value = 0
            myValuePrint(value)
            pygame.mixer.music.set_volume(value)
        elif choose == '6':
            value -= 0.1
            if value<0.01 and value>0:
                value = 0
            elif value <0:
                value = 1
            myValuePrint(value)
            pygame.mixer.music.set_volume(value)
        elif choose == '7':
            str = input('请输入你要点播的歌曲')
            if str in songList:
                num = songList.index(str)
                theSongPlay(songList, num, value)
            else:
                print('抱歉，曲库未收录此歌')
        elif choose == '0':
            break
        else:
            print('输入非法,请重新输入')

if __name__ == '__main__':
    songList = ['1.mp3', '2.mp3', '3.mp3']
    SongPlay(songList)

