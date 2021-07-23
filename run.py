import sys
from NexusPHP.tasks.say_thanks import main as saythanks
from NexusPHP.tasks.sign_in import main as signin
from NexusPHP.tasks.hda_sign_in import main as hdasignin
from NexusPHP.tasks.hdu_sign_in import main as hdusignin

if __name__ == '__main__':
    project = sys.argv[1]
    action = sys.argv[2]

    if project == 'nexusphp':
        eval('%s()' % action)
    elif project == 'hda':
        hdasignin()
    elif project == 'hdu':
        hdusignin()
    else:
        print('命令参数1 不正确!')