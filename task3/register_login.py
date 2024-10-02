lib=[{'id': 101, 'name': 'agnaey', 'email': 'a', 'address': 'aaa', 'mobile': 36345, 'password': '1234','book':[]}]
id_count=101

def register():
    email=input('enter your email :')
    f1=0
    for i in lib:
        if i['email']==email:
            f1=1
            print('------email already exits------')
            register()
    if f1==0:
        if len(lib)==0:
            id=101
        else:
            id=lib[-1]['id']+1
        print('your id: ',id)
        name=input('enter your name :')
        address=input('enter your address :')
        mobile=int(input('enter your mobile :'))
        password=input('enter your password :')
        lib.append({'id':id,'name':name,'email':email,'address':address,'mobile':mobile,'password':password,'book':[]})
        print('------registered------')

def login():
    username=input('enter username :')
    password=input('enter password :')
    f=0
    user=''
    if username=='admin' and password=='admin':
        f=1
    for i in lib:
        if username==i['email'] and password==i['password']:
            f=2
            user=i
    if f==0:
        print('-----invalid id or password-----')
    return f,user

