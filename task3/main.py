book=[{'id': 101, 'name': 'one piece', 'stock': 20, 'price': 2000},{'id': 102, 'name': 'naruto', 'stock': 15, 'price': 1500}]

import register_login as rl
import admin,user
while True:
    print(
    '''
1.register
2.login
3.exit'''
    )
    while True:
        try:
            ch=int(input('enter your choice :'))
            break
        except:
            print('----enter data correctly----')

    if ch==1:
        rl.register()
    elif ch==2:
        f,user=rl.login()
        # rl.login()
        if f==1:

            #admin
            while True:
                print('''
1.add book
2.view book
3.update book
4.delete book
5.view user
6.logout
'''          )
                while True:
                    try:
                        ch=int(input('enter your choice :'))
                        break
                    except:
                        print('----enter data correctly----')

                if ch==1:
                    admin.add_book()
                elif ch==2:
                    admin.view_book()
                elif ch==3:
                    admin.update_book()
                elif ch==4:
                    admin.delete_book()
                elif ch==5:
                    admin.view_users()
                elif ch==6:
                    break
        elif f==2:
            while True:
                print('''
                    1.view profile
                    2.view book
                    3.book take
                    4.book return
                    5.book in hand
                    6.exit
                      
                      ''')
                while True:
                    try:
                        sub_ch=int(input('enter your choice:'))
                        break
                    except:
                        print('----enter data correctly----')

                if sub_ch==1:
                    user.view_profile(user)
                elif sub_ch==2:
                    user.view_book()
                elif sub_ch==3:
                    user.book_take(user)
                elif sub_ch==4:
                    user.book_return(user)
                elif sub_ch==5:
                    user.book_in_hand(user)
                else:
                    break
        else:print('------invalid username or password-------')

    elif ch==3:
        break

