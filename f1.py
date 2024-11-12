import time
import copy
from datetime import datetime
import sharedState 

# declared lanes
regular_lane1 = [] 
regular_lane2 = [] 
regular_lane3 = [] 
regular_lane4 = [] 
regular_lane5 = [] 
self_lane = []  
waiting_lane = []

class Insertion:
    # function for inserting customers in different lanes
    # receive data through a list called a
    def insertCustomer(self, a):
        from f2 import Lottery
        # This function will be called after to print lane situation
        lane_inst = Lane_situation()
        lane_inst.print_stat()

        #   total customers are waiting
        present_lane_length = len(regular_lane1)+len(regular_lane2)+len(regular_lane3)+len(regular_lane4)+len(regular_lane5)+len(self_lane)
        


        # execute when the regular lane has no space but the self-lane has
        # sort out the incoming, newly generated customer
        if (len(regular_lane1)+len(regular_lane2)+len(regular_lane3)+len(regular_lane4)+len(regular_lane5)) == 25 and len(self_lane) < 15:
            print("Reguler lane over flow!")
            # Remember the indexes that need to be deleted.
            remove_ele = []

            # Customers with more than nine products move to the waiting lane.
            for pos in range(len(a)):
                if a[pos] > 9:
                    print("Customer with ",a[pos]," products has to join in waiting_lane line")
                    waiting_lane.append(a[pos])
                    remove_ele.append(pos)

            # delete them from list a by using remove_ele indexes.
            for pos in reversed(remove_ele):
                if 0 <= pos < len(a):
                    a.pop(pos)

        # If the current total customers, along with lists, exceed exeed limit of 40
        if (present_lane_length + len(a) ) > 40:
            k = 0
            while len(a) != k:
                waiting_lane.append(a[k]) # appending all customers in the waiting lane
                k += 1

        # return if there is no space left in any lanes
        if present_lane_length == 40:
            print("Both regular and selfservice lanes are full. Customer have to wait.")
            print("First in waiting_lane will enter to lane first")
            return

        tmp = [] # temporary array to hold customers from the waiting lane
        customer_index = [] # Remember their indexes from the waiting lane.
        lnth = 40 - present_lane_length  # how many spaces left in regular and service lane

        #  If the current total customers, along with lists, exceed exeed limit of 40
        if len(waiting_lane) > 0 and lnth > 0:
            tmp_reg_line = len(regular_lane1) + len(regular_lane2) + len(regular_lane3) + len(regular_lane4) + len(regular_lane5)  #total customers in regular lane
            tmp_slf_line = len(self_lane) # total customers in self services till

            k = 0
            # check space availability in lanes and customers are waiting
            while k != len(waiting_lane) and lnth != 0:

                if tmp_reg_line < 25 and tmp_slf_line < 15: #if both regular and self service lane has space left
                    tmp.append(waiting_lane[k])
                    if waiting_lane[k] > 9:
                        tmp_reg_line += 1
                    else:
                        tmp_slf_line += 1
                    customer_index.append(k) # remember indexes for appended customer from waiting
                    lnth -= 1
                    k += 1
                elif tmp_reg_line == 25 and tmp_slf_line < 15: # regular space full, self service left
                    if waiting_lane[k] > 9:
                        k += 1
                    else:
                        tmp.append(waiting_lane[k])
                        customer_index.append(k)
                        tmp_slf_line += 1
                        lnth -= 1
                        k += 1
                elif tmp_reg_line < 25 and tmp_slf_line == 15: # regular space left, self service full
                    tmp.append(waiting_lane[k])
                    customer_index.append(k)
                    tmp_reg_line += 1
                    lnth -= 1
                    k += 1

        # delete the customer from the waiting lane using the customer index list.
        if customer_index:
            for pos in reversed(customer_index):
                if 0 <= pos < len(waiting_lane):
                    waiting_lane.pop(pos)

        # copy the temporary customers to list a
        if tmp:
            a = copy.copy(tmp)

        lottery_ins = Lottery()
        lottery_ins.lottery_generator(a) # Check the letter by calling the function.


        # Push customers with products to different lanes.
        i = 0
        while i != len(a):
            if len(self_lane) < 15 and a[i] < 10: # total product in bucked less than 9 and has space left in self
                self_lane.append(a[i])
            else: # or we have spaces left in others lanes.
                if len(regular_lane1) < 5:
                    regular_lane1.append(a[i])
                elif len(regular_lane2) < 5:
                    regular_lane2.append(a[i])
                elif len(regular_lane3) < 5:
                    regular_lane3.append(a[i])
                elif len(regular_lane4) < 5:
                    regular_lane4.append(a[i])
                elif len(regular_lane5) < 5:
                    regular_lane5.append(a[i])
            i += 1

# customer checkout in different lanes also multithreaded
class Lane_services:

    # delete customer from lane following criteria if customer exists
    def clearing_regular_lane1(self):
        while sharedState.is_done:
            if len(regular_lane1) > 0:
                time.sleep(regular_lane1[0]*4)
                regular_lane1.pop(0)
            else:
                continue
    # delete customer from lane following criteria if customer exists
    def clearing_regular_lane2(self):
        while sharedState.is_done:
            if len(regular_lane2) > 0:
                time.sleep(regular_lane2[0]*4)
                regular_lane2.pop(0)
            else:
                continue

    # delete customer from lane following criteria if customer exists
    def clearing_regular_lane3(self):
        while sharedState.is_done:
            if len(regular_lane3) > 0:
                time.sleep(regular_lane3[0]*4)
                regular_lane3.pop(0)
            else:
                continue

    # delete customer from lane following criteria if customer exists
    def clearing_regular_lane4(self):
        while sharedState.is_done:
            if len(regular_lane4) > 0:
                time.sleep(regular_lane4[0]*4)
                regular_lane4.pop(0)
            else:
                continue

    # delete customer from lane following criteria if customer exists
    def clearing_regular_lane5(self):
        while sharedState.is_done:
            if len(regular_lane5) > 0:
                time.sleep(regular_lane5[0]*4)
                regular_lane5.pop(0)
            else:
                continue
    # delete customer from lane following criteria if customer exists
    def clearing_self_lane(self):
        while sharedState.is_done:
            if len(self_lane) > 0:
                time.sleep(self_lane[0]*6)
                self_lane.pop(0)
            else:
                continue

# class holds print_stat function
class Lane_situation:

    # print current situation of lanes after 30 sec continuously
    def print_stat(self):
        current_datetime = datetime.now()

        print("Total number of customers waiting_lane to check out at", current_datetime, " is: ", len(regular_lane1)+len(regular_lane2)+len(regular_lane3)+len(regular_lane4)+len(regular_lane5)+len(self_lane))
        lanes = [regular_lane1, regular_lane2, regular_lane3, regular_lane4, regular_lane5, self_lane, waiting_lane] # creating a list containing lists for better iteration process

        # idea generated from chat gpt
        for i, lane in enumerate(lanes, start=1):
            length = len(lane)
            if length < 1:
                if i == 7:
                    print("No customer in waiting_lane")
                elif i == 6:
                    print(f"L{i}(Self) ->", end=" ")
                    print("Open", end=" ")
                else:
                    if i != 1:
                        print(f"L{i}(Reg) ->", end=" ")
                        print("Close", end=" ")
                    else:
                        print(f"L{i}(Reg) ->", end=" ")
                        print("Open", end=" ")
            else:
                if i == 7:
                    print(length,"customers are waiting_lane to join in line")
                else:
                    if i == 6:
                        print(f"L{i}(Self) ->", end=" ")
                    else:
                        print(f"L{i}(Reg) ->", end=" ")

                    for _ in lane:
                        print("*", end=" ")
            print("")
