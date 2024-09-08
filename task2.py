mobiles={}
while True:
    print(
        '''
1.Add mobile phone
2.view mobile phone detail
3.Update mobile phone details
4.delete phone details
5.search mobile phone
6.Exit
'''
    )
    ch=int(input('enter your choice:'))
    if ch==1:
        id=int(input('Enter the ID of phone: '))
        brand=input('enter the brand name: ')
        name=input('Enter the phone name: ')
        camera=int(input('enter the resolution: '))
        price=int(input('enter the price: '))
        stock=int(input('Enter the Stock available: '))
        mobiles[id]={'brand':brand,'name':name,'camera':camera,'price':price,'stock':stock}
  
    elif ch==2:  
         print('{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('ID', 'BRAND', 'NAME', 'CAMERA', 'PRICE', 'stock'))
         print('-' * 65)
         for id, details in mobiles.items():
            print('{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(id, details['brand'], details['name'], details['camera'], details['price'], details['stock']))
    elif ch == 3:
        id = int(input('Enter ID of the phone that you want to update : '))
        if id in mobiles:
            while True:
                print(
                    '''
1. Update ID
2. Update brand name
3. Update name
4. Update camera resolution
5. Update price
6. Update quantity
7. Exit'''
                )
                ch = int(input('Enter your choice : '))
                if ch == 1:
                    new_id = int(input('Enter new ID : '))
                    mobiles[new_id] = mobiles.pop(id)  
                    id = new_id  
                elif ch == 2:
                    mobiles[id]['brand'] = input('Enter new brand name : ')
                elif ch == 3:
                    mobiles[id]['name'] = input('Enter new name : ')
               
                elif ch == 4:
                    mobiles[id]['camera'] = int(input('Enter new camera resolution : '))
                elif ch == 5:
                    mobiles[id]['price'] = int(input('Enter new price : '))
                elif ch == 6:
                    mobiles[id]['stock'] = int(input('Enter new stock : '))
                elif ch == 7:
                    break
                else:
                    print('Invalid choice!')
        else:
            print('Mobile phone not found in list')
    elif ch==4:
        code=int(input('enter the code :'))
        f=0
        for i in details:
            if i['code']==code:
                f=1
                del mobiles[id]
                print('Mobile phone deleted successfully.')
                break
        if f==0:
            print('code not found')
    elif ch == 5:
        id = int(input('Enter ID of the phone that you want to search : '))
        f = 0
        for current_id, details in mobiles.items():
            if id == current_id:
                f = 1
                print('{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('ID', 'BRAND', 'NAME', 'CAMERA', 'PRICE', 'stock'))
                print('-*80')   
                print('{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(id, details['brand'], details['name'], details['camera'], details['price'], details['stock']))
                break
    elif ch==6:
        break
    else:
        print('invalid choise')
