import mysql.connector as Tshirt

class herme():
    def __init__(self):
        self.fits = Tshirt.connect(host="localhost",
                                   user="root",
                                   password="",
                                   port=3307,
                                   database="outfits")
        query = "create table if not exists boutique(userid int primary key, brand varchar(50), category varchar(50), country varchar(50))"
        color = self.fits.cursor()
        color.execute(query)
        print("created")



# insert
    def insert_boutique(self, userid, brand, category, country):
        color = self.fits.cursor()
        self.user= userid
        self.bra=brand
        self.cat=category
        self.count=country
        query = "insert into boutique(userid,brand,category,country) " \
                "values({},'{}','{}','{}')".format(self.user, self.bra, self.cat, self.count)
        print(query)
        color.execute(query)
        self.fits.commit()
        print("save to database")

    def display(self):
        color = self.fits.cursor()
        color.execute("select * from boutique;L")

        for a in color:
            print(a)






Herme = herme()

#Herme.insert_boutique(2, 'fashion nova', 'red', 'china')
Herme.display()









# fits = Tshirt.connect (host="localhost",
#                   user="root",
#                   password="",
#                  port=3307,
#                 database ="outfits")
# print(fits)