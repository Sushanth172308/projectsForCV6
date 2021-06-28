'Note : National Academies of Science , Engineering , '
'and Medicine determined that Men needs  3.7liter and woman  needs 2.7liters'

import time
from plyer import notification

if __name__ == '__main__':
    while True:

        notification.notify(
            title='***Please Drink Water***',
            message= 'Note : National Academies of Science , Engineering , and Medicine determined that Men needs  3.7liter and woman  needs 2.7liters',
            app_icon='icon.ico.ico',
            timeout=5
        )
        #time.sleep(6)
        time.sleep(60*60)

