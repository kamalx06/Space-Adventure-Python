import time
import datetime
import random
import turtle

print('''
****************************************
* *
* Welcome to Space Adventures! *
* *
****************************************
''')
print('Initialization...')
time.sleep(0.1)

ship = [
    '````````````````````````````````````````````````````````````',
    '````````````````````````````````````````````````````````````',
    '````````````````-/``````````````````````````````````````````',
    '`````````````````.``````````````````````..--::--.```````````',
    '`````````````````````````````````````./ymoooooooo+/-````````',
    '`````````.//.``````````````````````-omMMMmsooooooo++.```````',
    '`````````.+/`````````````````````.omMMMMMMNyoooo++++:```````',
    '````````````````````````````````/mMMMMMMMMMMds++++++/```````',
    '``````````````````````````````-hNMMNdddmNMMNNNdyo+++/```````',
    '````````````````````````````.+mMMNsshhhyoyNNNNNNmdhs.```````',
    '```````````````````````````-hMMMM+hddddys+sNNNNNNNd:````````',
    '`````````````````````````.+mMMMMM/dddyyss+oNNNNNmo.`````````',
    '``````````````````..--:/+hNMMMMMMdosssso+omNNNms-```````````',
    '````````````````./++oooymMMMMMMMMNmhyssydNNNdo-`````````````',
    '``````````````.:oooooohNMMMMMNmNNNNNNNNNNmy/.```````````````',
    '`````````````./ooooosmMMMMNmyymNNNNNNNmh+-``````````````````',
    '`````````````-::://+NMMMNdsshNNNNNNNdo:.````````````````````',
    '``````````````````./NMNdsshmNNNNNmho.```````````````````````',
    '````.-```````````.+dddsshmNNNNmdyoo-````````````````````````',
    '````.-````````.-/sddsosdmmNmdysooo/```````````````:-````````',
    '`````````````./ohmhydhys/-:soooooo.```````````````+:````````',
    '````````````:osdmmmdy+-````ooooo+-``````````````````````````',
    '``````````./osdmdys+-.`````oo+:-````````````````````````````',
    '`````````./oossoo/-````````:-```````````````````````````````',
    '````````./ooo+/-.````````````````````````````.``````````````',
    '````````/+/-.```````````````````````````````.+`````.````````',
    '```````..``````````````````````````````````````````/.```````',
    '````````````````````````````````````````````````````````````',
    '````````````````````````````````````````````````````````````',
    '````````````````````````````````````````````````````````````'
]

for i in range(len(ship)):
    print(ship[i])
    time.sleep(0.05)
print('\nYeah! The spaceship is ready.')

# Initialization spaceship name
name = []
print('\n************************************************************')
print('\tSPACESHIP ID-', end='')
for i in range(5):
    r = random.randint(0, 9)
    name.append(r)
    print(name[i], end='')

# Date
print('\n\tDate: ', end='')
print(datetime.date.today())

print('************************************************************')
print('''
Options:
[1] - stars
[2] - galaxy
[3] - missile
[4] - protection
[0] - exit
''')

while True:
    events = ['Ulduzların yaranması baş verən xüsusi zonaya daxil oluruq',
    'Andromedanın galaktikasına yaxınlaşırıq',
    'Diqqət!Asteroid gəlir.Hazırlıq görün!',
    'Kosmik quldurlar təyin edilib!']
    random_events_index = random.randint(0, len(events) - 1)
    event = events[random_events_index]
    print(event)
    print('************************************************************')
    print('************************************************************')
    select = input('Your select: ')
    if (select == '1' and random_events_index == '0'):
        print('You win✔')
    elif (select == '2' and random_events_index == '1'):
        print('You win✔')
    elif (select == '3' and random_events_index == '2'):
        print('You win✔')
    elif (select == '4' and random_events_index == '3'):
        print('You win✔')

    elif (select == '1' and random_events_index == 1):
        print('You Lose')
        continue
    elif (select == '1' and random_events_index == 2):
        print('You Lose')
        continue
    elif (select == '1' and random_events_index == 3):
        print('You Lose')
        continue

    elif (select == '2' and random_events_index == 0):
        print('You Lose')
        continue
    elif (select == '2' and random_events_index == 2):
        print('You Lose')
        continue
    elif (select == '2' and random_events_index == 3):
        print('You Lose')
        continue

    elif (select == '3' and random_events_index == 0):
        print('You Lose')
        continue
    elif (select == '3' and random_events_index == 1):
        print('You Lose')
        continue
    elif (select == '3' and random_events_index == 3):
        print('You Lose')
        continue

    elif (select == '4' and random_events_index == 0):
        print('You Lose')
        continue
    elif (select == '4' and random_events_index == 1):
        print('You Lose')
        continue
    elif (select == '4' and random_events_index == 2):
        print('You Lose')
        continue

    elif (select < '0' or select > '4'):
        print('Try again')
        continue
    # Stars

    if select == '1' or select == '2':
        turtle.TurtleScreen._RUNNING = True
        turtle.bgcolor('black')
        turtle.speed(0)
        turtle.pensize(1)

        if select == '1':
            print('Stars are giant, luminous spheres of plasma.')
            # List of colors
            colors = ['white', 'yellow']
            max_index = len(colors) - 1
            for i in range(50):
                # Random color
                random_index = random.randint(0, max_index)
                new_color = colors[random_index]
                turtle.color(new_color)
                # Stars
                turtle.begin_fill()
                for i in range(5):
                    turtle.forward(15)
                    turtle.right(144)
                turtle.penup()
                turtle.end_fill()
                # Generate random location on the screen
                w = turtle.window_width() // 2 - 50
                h = turtle.window_height() // 2 - 50
                x = random.randrange(-w, w)
                y = random.randrange(-h, h)
                turtle.goto(x, y)
                turtle.pendown()

            turtle.exitonclick()
        # Galaxy
        else:
            print('Galaxies consist of stars, stellar remnants, dust, gas, and dark matter, bound together by gravity.')
            turtle.pencolor('purple')
            # List of colors
            colors = ['white', 'yellow']
            max_index = len(colors) - 1
            for i in range(100):
                turtle.pensize(i / 100 + 1)
                turtle.forward(i)
                turtle.left(59)
            turtle.exitonclick()

    # Rocket
    elif select == '3':
        print('Launching a missile...')
        missile = [
            'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
            'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmy+mMMM',
            'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdy+:-hMMMM',
            'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdys+:--yMMMMM',
            'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdyys+----sMMMMMM',
            'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmyyhs:-----sMMMMMMM',
            'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMhshd+-------sMMMMMMMM',
            'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNysmh/--------yMMMMMMMMM',
            'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNsyNh:---------hMMMMMMMMMM',
            'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNsyNy:---------:dMMMMMMMMMMM',
            'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNsyNh:----------+NMMMMMMMMMMMM',
            'MMMMMMMMMMMMMMMMMMMMMMMMMMMMNyyMh:-----------yMMMMMMMMMMMMMM',
            'MMMMMMMMMMMMMMMMMMMMMMMMMMMyyNd/-----------/mMMMMMMMMMMMMMMM',
            'MMMMMMMMMMMMMMMMMMMMMMMMMhsNm+------------sMMMMMMMMMMMMMMMMM',
            'MMMMMMMMMMMMMMMMMMMMMMMmsmNo------------/mMMMMMMMMMMMMMMMMMM',
            'MMMMMMMMMMMMMMMmhhso+o+/My------------:yMMMMMMMMMMMMMMMMMMMM',
            'MMMMMMMMMMMMNho+/-----:s:------------oNMMMMMMMMMMMMMMMMMMMMM',
            'MMMMMMMMMMmy+:-------//-:+y:-------+mMMMMMMMMMMMMMMMMMMMMMMM',
            'MMMMMMMMNy/--------:/--/+/+------/dMMMMMMMMMMMMMMMMMMMMMMMMM',
            'MMMMMMMd:---------:---///:------oMMMMMMMMMMMMMMMMMMMMMMMMMMM',
            'MMMMMMs-/+oo/-------:/::---------MMMMMMMMMMMMMMMMMMMMMMMMMMM',
            'MMMMMNmMMMMMMMd---:///-----------NMMMMMMMMMMMMMMMMMMMMMMMMMM',
            'MMMMMMMMMMMMMMh--///------------+MMMMMMMMMMMMMMMMMMMMMMMMMMM',
            'MMMMMMMMMMMMMMNo+/:------------/NMMMMMMMMMMMMMMMMMMMMMMMMMMM',
            'MMMMMMMMMMMNNMmhNyydNd/-------+NMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
            'MMMMMMMMMmdNMMNNMMMMMMN:-----yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
            'MMMMMMMNhdmNNmmMMMMMMMMo---oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
            'MMMMMMdsmmmdhmMMMMMMMMM/-sNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
            'MMMMMhsydhydMMMMMMMMMMmhMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
            'MMMMhsssydMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
            'MMMMyhmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
            'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'
        ]

        for i in range(len(missile)):
            print(missile[i])
            time.sleep(0.05)

    # Protection
    elif select == '4':
        print('An enemy spaceship is moving toward your SPACESHIP ID-', end='')

        for i in range(5):
            print(name[i], end='')

        print('\nStart protection...')

        time.sleep(0.05)
        protection = [
            'MMMMMMMMMMMMMMMMMMMMMMMy//hNMMMMMMMMMMMMMMMMMMMMMM',
            'MMMMMMMMMMMMMMMMMMdohNy::--ddNMMMMMMMMMMMMMMMMMMMM',
            'MMMMMMMMMMMMMMMMMmo::os::--+-+MMMMMMMMMMMMMMMMMMMM',
            'MMMMMMMMMMMMMMMMMo::::-:::::-oMMMMMMMMMMMMMMMMMMMM',
            'MMMMMMMMMMMMMMMMMm::/::///:/:oMMMMMMMMMMMMMMMMMMMM',
            'MMMMMMMMMMMMMMMMMMd/::///:://dMMMMMMMMMMMMMMMMMMMM',
            'MMMMMMMMMMMMMMMMMMMs-.-::.-/yMMMMMMMMMMMMMMMMMMMMM',
            'MMMMMMMMMMMMMMMMMMMm/:://:-/hMMMMMMMMMMMMMMMMMMMMM',
            'MMMMMMMMMMMMMMMMMMMMo:::::-:hMMMMMMMMMMMMMMMMMMMMM',
            'MMMMMMMMMMMMMMMMMMMN+/:--:-:/sNMMMMMMMMMMMMMMMMMMM',
            'MMMMMMMMMMMMMMMMNhyo/:--..-:::+dMMMNMMMMMMMMMMMMMM',
            'MMMMMMMMMMMMMMmo:-:--:--.-::/:-/ohNymNMMMMMMMMMMMM',
            'MMMMMMMMMMNmdy/::////:./+//+/::::/osdmMMMMMMMMMMMM',
            'MMMMMMMMNs+/:::/++++//:+oosooo/::/-/+ydNMMMMMMMMMM',
            'MMMMMMMNo-::-//++++++/+oosso+++/::/o/o/oNMMMMMMMMM',
            'MMMMMMMN:-::://+++o+o/:ooooo++::-///::::/NMMMMMMMM',
            'MMMMMMMN/---.///++++::/+oooo+++/`.-::--:-hMMMMMMMM',
            'MMMMMMMMo..`./:://:-..:/++++//--```.--:::sMMMMMMMM',
            'MMMMMMMMy:-.-::-:-:///:-::/:.-:-.``:--.-:+mMMMMMMM',
            'MMMMMMMNo:-.`:::://+++:-:/:-...-.`:h-::-::oNMMMMMM',
            'MMMMMMMN+:-.`:-::///+/-++//-.....`sMo://:-/hMMMMMM',
            'MMMMMMMm/-.``+/-:::/::/+//:---.`./NMNs:/:-:/mMMMMM',
            'MMMMMMMd:.``.do--:-:////+/-:/::.oNMMMMs---:/yMMMMM',
            'MMMMMMh:--../Ms/:::::////:/++o:-dMMMMMMs-.:/omMMMM',
            'MMMMMy/.-::.+Ns+/.--///:/+++oo+/MMMMMMMMh-:/o+mMMM',
            'MMMMN/::/:-.dmo+:./+ooossoooo+/oMMMMMMMMy/:/o:oNMM',
            'MMMMy/-/:-.yN+-:-//+ooo/+o+////:dMMMMMMM+:/:/-:yMM',
            'MMMN+:--:-hNso//-:++++/-::-::-/::sMMMMMMs:::/:+yMM',
            'MMMy/:..:dNo+++++:--:-./++:-/o/:--dMMMMMN/::::/mMM',
            'MMN+:-.-mMo:///++/--..-://+/:+//..yMMMMMMy-/+//NMM',
            'MMd/::.hMM+/::///:-----:-///-:---.dMMMMMMd//+//MMM',
            'MMs:--yMMd///-./+/.--.--:::--.//:+NMMMMMMMo:/:+NMM',
            'Mm::-+MMNo+-//--.``.-`.-:..:--+//+dMMMMMMMs-::+MMM',
            'My+/:/yMm:::-://--.``` `.--+:-+://sMMMMMMM/---+MMM',
            'd//::+:hN:/-//:::--`/md/:::/-:+/+/+NMNMMmo++++dMMM',
            'o::oNMy:N+:://--:..`/MM+:--:-:+++/oohmyo+//+++hMMM',
            'o-/oMMNoh:-:---:..``oMMd-.:/--////+:hm/:+:+o/+yMMM',
            'h:-/NMMMs:-::..:...`dMMM+-:/--:://+-s+sNm:::/:+MMM',
            'No-++NMMs--:::-:--.`MMMMd-::.:::.-:-//NMh:/---oMMM',
            'Mm/:+yMMd-.:::...-.:MMMMM:::..::--:-/mMM+/+/--mMMM',
            'MMNdyNMMN:.---.-..`sMMMMMm/-..--./-..mMh:/-.-hMMMM',
            'MMMMMMMMMs--..:.:-`hMMMMMMm/-.:--/--.+h-.-:omMMMMM',
            'MMMMMMMMMy:-.:-.-.`oMMMMMMMd:-/:.:-:-.+++hNMMMMMMM',
            'MMMMMMMMMh-:-/-..``yMMMMMMMN/--/:---:.dMMMMMMMMMMM',
            'MMMMMMMMMh-:--:.-..dMMMMMMMM+:-----::-dMMMMMMMMMMM',
            'MMMMMMMMMN:--.-...`yMMMMMMMMN+-:-.:-..-yMMMMMMMMMM',
            'MMMMMMMMMM/--..````.yMMMMMMMM/-.`...-.-.sMMMMMMMMM',
            'MMMMMMMMMN-```````.`.hMMMMMMN:-..-:..-..-dMMMMMMMM',
            'MMMMMMMMMN-`..```````.yMMMMMM+-..-..-.--./MMMMMMMM',
            'MMMMMMMMMM/...-..`````:MMMMMMy-``..---.--.mMMMMMMM',
            'MMMMMMMMMMo.`......```:MMMMMMN:.`--..-:...hMMMMMMM',
            'MMMMMMMMMMN:...``.-.``yMMMMMMMm:...`.--:.-hMMMMMMM',
            'MMMMMMMMMMMs.`...``..:NMMMMMMMMd-.-.`...--sMMMMMMM',
            'MMMMMMMMMMMd-....`````sMMMMMMMMMo`--`.-.-.:NMMMMMM',
            'MMMMMMMMMMMm-..-.`..``hMMMMMMMMMm:.-`-:...-hMMMMMM',
            'MMMMMMMMMMMN:`-.-.....NMMMMMMMMMMs.------.:sMMMMMM',
            'MMMMMMMMMMMd-.-`.`.`..NMMMMMMMMMMh.::---:--+MMMMMM',
            'MMMMMMMMMMMN:.-...```+MMMMMMMMMMMm..-.----::MMMMMM',
            'MMMMMMMMMMMd/--.-:-.-+NMMMMMMMMMMM::/-/+-:/:yNMMMM',
            'MMMMMMMMMMy/:--.-:-`-`hMMMMMMMMMMd-:+:/+/:+:-sMMMM',
            'MMMMMMMMMh:/-.``::.`../MMMMMMMMMMo-/::://-::::dMMM',
            'MMMMMMMNy://-.`.:..``.`hMMMMMMMMm-.+/.::--..://NMM',
            'MMMMMMd:-:--``-:-``.`..-mMMMMMMN/.-//-/+/-`.-/++mM',
            'MMMMMm---.``..--```.``../NMMMMMo`.//-:+++/.`.-///h',
            'MMMMMMmddmmNNhhyhmmmmNMMMMMMMMh----:s+//omMmsoossd'
        ]

        for i in range(len(protection)):
            print(protection[i])
            time.sleep(0.05)

    elif select == '0':
        break
    else:
        print('Error! Try again')

print("Finish")
