lib=[{'id': 101, 'name': 'agnaey', 'email': 'a', 'address': 'aaa', 'mobile': 36345, 'password': '1234','book':[]}]
book=[{'id': 101, 'name': 'one piece', 'stock': 20, 'price': 2000},{'id': 102, 'name': 'naruto', 'stock': 15, 'price': 1500}]

def add_book():
    if len(book)==0:
        id=101
    else:
        id=book[-1]['id']+1
    print('book id:',id)
    name=input('enter book name: ')
    stock=int(input('enter the avalible stock: '))
    price=int(input('enter the prize: '))
    book.append({'id':id,'name':name,'stock':stock,'price':price})
    print('-------book added-------')
    
def view_book():
    print('{:<10}{:<20}{:<10}{:<10}'.format('id','name','stock','price'))
    print('-'*50)
    for i in book:
        print('{:<10}{:<20}{:<10}{:<10}'.format(i['id'],i['name'],i['stock'],i['price']))

def update_book():
    id=input('enter your id: ')
    f2=0
    for i in book:
        if i ['id']==int(id):
            f2=1
            name=(input('update books name: '))
            stock=int(input('update books stock: '))
            price=int(input('update books price: '))
            i['name']=name
            i['stock']=stock
            i['price']=price
            print('updated successfully')
    if f2==0:
        print('---------invalid id-------')

def delete_book():
    id=input('enter your id: ')
    f2=0
    for i in book:
        if i ['id']==int(id):
            f2=1
            book.remove(i)
            print('-----deleted successfully-----')
    if f2==0:
        print('---------invalid id-------')

def view_users():
    print('{:<10}{:<20}{:<10}{:<10}'.format('id','name','email','address','mobile'))
    print('-'*50)
    for i in lib:
        print('{:<10}{:<20}{:<10}{:<10}'.format(i['id'],i['name'],i['email'],i['address'],i['mobile']))

    