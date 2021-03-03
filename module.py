boy = ("Naruto,hiruzen,jugo,suigetsu,minato,Sasuke,sai,kakashi,iruka,itachi,dan,harashima sneju,gato,ibiki,inari,idate,jirobo,kakuzu,kimimaro,mizuki,yashamaru,sakon,kidomaru,dosu,gaara,orochimaru,jiraya,rock lee,shikamaru,chojo,deidara,neji,sasori,haku,kisame,ebisu,yamato,nawaki,killer bee,teuchi,kankuro,kiba,konohamaru,shino,asuma,zabuza,guy,kabuto")
girl = ('Sakura,hinata,tenten,temari,ino,kurenai,tsunade,kushina,konan,karin,anko,chiyo,karui,shizune,mikoto,rin,mie,pain,nagato,yahiko,moegi,tayuya,yugito,')
taild_beasts = ("Shukaku,Matatabi,Isobu,SonGokū,Kokuō,Saiken,Chōmei,Gyūki,Kurama,")
main = ("naruto,sasuke,akatsuki,sakura,hinata,kakashi,jiraya,iruka,madara uchiha,killer bee,")
villan = ("mizuki,zbuza,haku,suigetsu,karin,orochimaru,gato,pain,sasuke")
hero = ("naruto,minato,shikamaru,might guy,negi,tenten,kiba,chiyo,choji,ino,gara,sakura,hinata,hiruzen,sai,kakashi,iruka,dan,harashima senju,ibiki,")
side = ("yashamaru,kimimaro,hidan,kakuzu,inari")

char_type = input('is your character is a boy,girl,tailed_beast,main_char,hero,side_CHARACTER')

if char_type == 'tailed beast':
    q1 = input('is your character have 1 tails')
    if 'yes' in q1:
        print('you think of shukaku the one tails')
    else:
        q2 = input('dose your character have 2 tails')
        if 'yes' in q2:
            print('you think of 2 tails')
        else:
            q3 = input('dose your character have 3 tails')
            if 'yes' in q3:
                print('you think of 3 tails')

            else:
                q4 = input('dose your character have 4 tails')
                if 'yes' in q4:
                    print('you think of 4 tails')

                else:
                    q5 = input('dose your character have 5 tails')
                    if 'yes' in q5:
                        print('you think of 5 tails')

                    else:
                        q6 = input('dose your character have 6 tails?')
                        if 'yes' in q6:
                            print('you thinl of 6 tails')

                        else:
                            q7 = input('dose your character have 7 tails')
                            if 'yes' in q7:
                                print('you think of 7 tails')

                            else:
                                q8 = input('dose your character have 8 tais')
                                if 'yes' in q8:
                                    print('you think of 8 tails')

                                else:
                                    q9 = input('is your character kyubi or 9 tails?')
                                    if 'yes' in q9:
                                        print('you think of kyubi the 9 tails')
                                    else:
                                        print('hey thats a spoiler')

if char_type == 'side':
    side_q1 = input('is your character with gaara')
    if 'yes' in side_q1:
        print('you think of yashamaru')

    else:
        side_q2 = input('is your character link with orochimaru')
        if 'yes' in side_q2:
            print('you think of kimimomaro')

        else:
            side_q3 = input('is your character a akatsuki member')

            if 'yes' in side_q3:
                print('you think of hidan')

            else:
                side_q4 = input('is your character a temate of hidan')
                if 'yes' in side_q4:
                    print('you think of kakuzu')

                else:
                    side_q5 = input('dose naruto meet your character when they went to the misson to fight zabuza')

                    if 'yes' in side_q5:
                        print('you think of inari')
                    else:
                        print('hey that caharcetr is not in the list of the side characters')    


