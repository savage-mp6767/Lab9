############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.

def more(a,b):
    return a > b

diagnose = True
questions = ['What is your temperature?','Have you been sick in the last 24 hours? (y/n)','Have you recently traveled to West Africa? (y/n)']

while diagnose:
    results = []
    print questions[1]
    results[1] = raw_input()
    print questions[2]
    results[2] = raw_input()
    print questions[3]
    results[3] = raw_input()
    
    if results[1] >= 105:
        admit = True
    if results[1] >= 102 and results[2] == 'y':
        admit = True
    if results[1] >= 100 or results[2] == 'y' and results[3] == 'y':
        admit = True
    
    if admit:
        print 'You have been admitted to the hospital.'