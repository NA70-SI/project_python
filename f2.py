import random
import time
import sharedState
from f1 import Insertion

# class containing two functions
class CreateCustomerElement:
    def generate_product(self,customer_number):    # receive parameter, generate bucket products and return
        customer_with_basket_items = [random.randint(1, 30) for _ in range(customer_number)]
        return customer_with_basket_items
    def generate_customer(self): # Generate between 1-10  customers using thread
        insert_ins = Insertion() # importing the class called Insertion from f1.py
        while sharedState.is_done:
            customer_number = random.randint(1,10)
            cus_with_prod = self.generate_product(customer_number) # calling function for generating items for each customer
            insert_ins.insertCustomer(cus_with_prod) # send them to the face insertion process in f1.py
            time.sleep(30)


class Lottery:

    # generate a lottery for each customer in the list
    def lottery_generator(self, a):

        b = 1
        print("### Customer details ###")
        for cus in a: #cus = customer
            if cus > 9:
                random_boolean = bool(random.randint(0, 1)) # generate true or false for every customer entering in line with more thn 9 products in their buscket
                if random_boolean:
                    print(f'C{b}', "-> Items in basket: ", cus, ", wins a lottery ticket!")
                    print("Time to process basket at cashier till :", cus*4)
                    print("Time to process basket at self-service till :", cus*6)
                else:
                    print(f'C{b}', "-> Items in basket: ", cus, ", hard luck!")
                    print("Time to process basket at cashier till :", cus*4)
                    print("Time to process basket at self-service till :", cus*6)

            else:
                print(f'C{b}', "-> Items in basket: ", cus)
                print("Time to process basket at cashier till :", cus*4)
                print("Time to process basket at self-service till :", cus*6)
            b += 1
