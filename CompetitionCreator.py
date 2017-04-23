import sys
import random

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print('Usage: python3 CompetitionCreator.py competitors_file.txt')
        sys.exit()

    fileName = sys.argv[1]

    try:
        competitorsFile = open(fileName, 'r')
        competitors = []

        for line in competitorsFile:
            competitors.append(line.strip())

        if len(competitors) == 0:
            raise Exception('File is empty')

        outcast = ""
        outcastOpponent = ""

        if len(competitors) % 2 != 0:
            outcast = random.choice(competitors) 
            competitors.remove(outcast)

            outcastOpponent = random.choice(competitors)
        
        battles = []
        while len(competitors) > 0:
            first = random.choice(competitors)
            competitors.remove(first)

            second = random.choice(competitors)
            competitors.remove(second)

            battles.append([first, second])

        battleFile = open('battle.txt', 'w') 

        for battle in battles:
            battleFile.write("{} vs {}\n".format(battle[0], battle[1]))

        if len(outcast) > 0:
            battleFile.write("Outcast: {} vs {}\n".format(outcast, outcastOpponent))

    except FileNotFoundError:
        print("Error: {} not found!".format(fileName))
    except Exception as exception:
        print("Error: {}".format(exception))

