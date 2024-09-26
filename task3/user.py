lib=[{'id': 101, 'name': 'agnaey', 'email': 'a', 'address': 'aaa', 'mobile': 36345, 'password': '1234','book':[]}]
book=[{'id': 101, 'name': 'one piece', 'stock': 20, 'price': 2000},{'id': 102, 'name': 'naruto', 'stock': 15, 'price': 1500}]

def view_profile(user):
    print('-'*50)
    print('{:<10}{:<20}{:<10}{:<10}'.format('id','name','email','address','mobile'))
    print('-'*50)
    print('{:<10}{:<20}{:<10}{:<10}'.format(user['id'],user['name'],user['email'],user['address'],user['mobile']))

def view_book():
    print('-'*50)
    print('{:<10}{:<20}{:<10}{:<10}'.format('id','name','stock','price'))
    print('-'*50)
    for i in book:
        print('{:<10}{:<20}{:<10}{:<10}'.format(i['id'],i['name'],i['stock'],i['price']))

def book_take(user):
    id=int(input('enter book id you want to add: '))
    f=0
    for i in book:
        if i['id']==id:
            f=1
            if i['stock']>0:
                user['book'].append(i['id'])
                i['stock']-=1
                print('----book added----')
            else:
                print('-----out of stock------')
    if f==0:
            print('-----id not found--------')

def book_return(user):
    id=int(input('enter book id you want to return: '))
    f=0
    for i in book:
        if i['id']==id and id in user['book']:
            f=1
            i['stock']+=1
            user['book'].remove(id)
            print('--------book returned-------')
    if f==0:
        print('-----book not found------')

def book_in_hand(user):
    print(user['book'])