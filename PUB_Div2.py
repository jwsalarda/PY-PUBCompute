#PUB Divion App
"""'''
#from datetime import timedelta, datetime
import datetime
#from datetime import datetime

Day1 = datetime.timdelta(hours=24)


BillDaysStart = datetime.datetime.strptime(input("Enter Start of Billing Date (dd/mm/yyyy): "), '%d/%m/%Y')
#DS = date.striptime(BillDaysStart, "%m/%d/%y")

BillDaysEnd = datetime.datetime.strptime(input("Enter End of Billing Date (dd/mm/yyyy): "), '%d/%m/%Y')

DaysDiff = BillDaysEnd - BillDaysStart
DaysDiff2 = DaysDiff + Day1

print(DaysDiff2)
'''
"""
#Input for Bill amount
pub_month = float(input("How much is the bill for this month?: "))
#wifi_month = int(60)

print(" ")
print("==== MASTER BEDROOM ====")
#Master Room Days and visitors
mas_days_out = int(input("Master's room tenant is out for how many days?: "))
#int(mas_days_out)

vis_mas_count = int(input("How many visitors for Master's room tenant?: "))
if vis_mas_count > 0 :
    vis_mas_days_stay = int(input("How many days did the master's room visitor stayed?: "))
    vis_mas_total_days = vis_mas_count * vis_mas_days_stay
else :
    #Master Room Computation
    mas_total_days = 30 - mas_days_out



#print("Master Room Total Days Stay: ", mas_total_days)
#print("Master Room Total Visitors: ", vis_mas_count)
#print("Master's Room",vis_mas_count, "visitor(s) stayed for", vis_mas_total_days/vis_mas_count ,"days each or a total of ", vis_mas_total_days,"days")

print("")
print("==== COMMON ROOM 1 (ZIP) ====")
#COMMON ROOM1 DAYS AND VISITORS
common1_days_out = int(input("Common Room 1 tenat (Zip) is out for how many days?: "))
vis_room1_count = int(input("How many visitors for Common Room 1 (Zip)?: "))

if vis_room1_count > 0 :
    vis_room1_days_stay = int(input("How many days did the common room1 visitor stayed?: "))
    vis_room1_total_days = vis_room1_count * vis_room1_days_stay
else :
#COMMON ROOM1 Computation
    room1_total_days = 30 - common1_days_out

print("")
print("==== COMMON ROOM 2 (JOEY) ====")
#COMMON ROOM2 DAYS AND VISITORS
common2_days_out = int(input("Common Room 2 (Joey) is out for how many days?: "))
vis_room2_count = int(input("How many visitors for Common Room 2 (Joey)?: "))
if vis_room2_count > 0 :
    vis_room2_days_stay = int(input("How many days did the common room1 visitor stayed?"))
    vis_room2_total_days = vis_room2_count * vis_room2_days_stay
else :
#COMMON ROOM COMPUTATION
    room2_total_days = 30 - common2_days_out


#OVERALL COMPUTATION
print("======== COMPUTATION SUMMARY =======")
print("")
print("== TENANT  == DAYS STAY === VISITOR(S) === DAYS STAY ===")
print("=== JOHN   = (",mas_total_days,"/ 30 )      ",vis_mas_count,"           ",vis_mas_total_days)
print("=== ZIP    = (",room1_total_days,"/ 30 )      ",vis_room1_count,"           ",vis_room1_total_days)
print("=== JOEY   = (",room2_total_days,"/ 30 )      ",vis_room2_count,"           ",vis_room2_total_days)
