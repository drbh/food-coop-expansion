# coding: utf-8
import math

# food coop operational stuff
days_of_week = ['M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su']
hours_of_opr = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 17, 19, 20, 21, 22]
workslot_hours = 2.66
number_needed_for_hour = 60

# new member predictions
percent_of_missed_workslots = 0.2
est_num_members = 4050
average_weekly_spend_per_member = 40.0

# building related
cost_of_building = 10000000.0
years_paying_off_lease = 20.0

print("")
print("MY COOP FEASIBILITY CALCULATOR! ")
print("")

print("")
print("MY INPUTS ")
print("")

print("Days open:\t\t\t\t %s" % ' '.join(days_of_week))
print("Hours open:\t\t\t\t %s" % ' '.join([str(x) for x in hours_of_opr]))

print("Workslot hours:\t\t\t\t %s" % str(workslot_hours))
print("Number needed for hour:\t\t\t %s" % str(number_needed_for_hour))
print("Percent of missed workslots:\t\t %s" % str(percent_of_missed_workslots))
print("Est num members:\t\t\t %s" % str(est_num_members))
print("Cost of building:\t\t\t %s" % str(cost_of_building))
print("Loan payback years:\t\t\t %s" % str(years_paying_off_lease))
print("Average weekly spend per member:\t %s" %
      str(average_weekly_spend_per_member))

print("")
print("")
print("COOP OPERATIONAL NEEDS ")
print("")

number_hours_open = len(days_of_week) * len(hours_of_opr) * 1.0
print("Numbers hours open:\t\t %s" % str(number_hours_open))

hours_of_work_needed = (number_needed_for_hour * number_hours_open)
print("Hours of work needed:\t\t %s" % str(hours_of_work_needed))

workslots_needed = hours_of_work_needed / workslot_hours
print("Number workslots needed:\t %s" % str(workslots_needed))

people_needed_for_work_slots = math.ceil(workslots_needed)
print("Number members needed:\t\t %s" % str(people_needed_for_work_slots))

print("")
print("")
print("COOP OPERATIONAL FEASIBILITY ")
print("")

est_num_contributing_members = est_num_members * \
    (1 - percent_of_missed_workslots)
print("Contributing members:\t\t %s" % str(est_num_contributing_members))

members_can_support_work = est_num_contributing_members > people_needed_for_work_slots
print("Members can support work:\t %s" % str(members_can_support_work))

surplus_work_members = est_num_contributing_members - people_needed_for_work_slots
print("Surplus members:\t\t %s" % str(surplus_work_members))

print("")
print("")
print("COOP CASHFLOW FEASIBILITY ")
print("")

est_weekly_rev = est_num_contributing_members * average_weekly_spend_per_member
print("Est weekly revenue:\t\t %s" % str(est_weekly_rev))

est_monthly_rev = est_weekly_rev * 4
print("Est monthly revenue:\t\t %s" % str(est_monthly_rev))

monthly_building_cost_rent_morg = cost_of_building / (12 * years_paying_off_lease)
print("Monthly Building Cost:\t\t %s" % str(monthly_building_cost_rent_morg))

rev_gen_for_operations = est_weekly_rev - monthly_building_cost_rent_morg
print("Revenue after building:\t\t %s" % str(rev_gen_for_operations))
