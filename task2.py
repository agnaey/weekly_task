mobiles=[{'id':101,'brand':'asus','name':'rog','camera':64,'price':59000,'stock':29}]
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
        camera=int(input('enter the camera resolution: '))
        price=int(input('enter the price: '))
        stock=int(input('Enter the Stock available: '))
        mobiles.append([id,brand,name,camera,price,stock])   
    elif ch==2:  
         print('-' * 65)
         print('{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('id', 'brand', 'name', 'camera', 'price', 'stock'))
         print('-' * 65)
         for i in mobiles:
            print('{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i['id'], i['brand'], i['name'], i['camera'], i['price'], i['stock']))
    elif ch == 3:
        id = int(input('Enter ID of the phone that you want to update : '))
        for i in mobiles:
            if id==i['id']:
                f=1
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
                ch=int(input('Enter your choice : '))
                if ch==1:
                    new_id=int(input('Enter new ID : '))
                    i[id]=new_id 
                elif ch==2:
                    new_brand=input('Enter new brand name : ')
                    i['brand']=new_brand
                elif ch==3:
                    new_name=input('Enter new name : ')
                    i['name']=new_name
               
                elif ch==4:
                    new_camera=int(input('Enter new camera resolution : '))
                    i['camera']=new_camera
                elif ch==5:
                    new_price=int(input('Enter new price : '))
                    i['price']=new_price
                elif ch == 6:
                    new_stock=int(input('Enter new quantity : '))
                    i['stock']=new_stock
                elif ch == 7:
                    break
                else:
                    print('----Invalid choice!-----')
        if f==0:
            print('-----Mobile phone not found in list-----')
    elif ch==4:
        id=int(input('enter the code :'))
        f=0
        for i in mobiles:
            if id==i['id']:
                f=1
                mobiles.remove(i)
                print('-----Mobile phone deleted successfully.-----')

        if f==0:
            print('----code not found----')
    elif ch == 5:
        id = int(input('Enter CODE of the phone that you want to search : '))
        f = 0
        for i in mobiles:
            if id==i['id']:
                f=1
                print('-'*80)   
                print('{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('id', 'brand', 'name', 'camera', 'price', 'stock'))
                print('-'*80)   
                print('{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i['id'], i['brand'], i['name'], i['camera'], i['price'], i['stock']))
                
        if f==0:
            print('-----Mobile phone not found in list-----')
    elif ch==6:
        break
    else:
        print('-----invalid choise-----')
