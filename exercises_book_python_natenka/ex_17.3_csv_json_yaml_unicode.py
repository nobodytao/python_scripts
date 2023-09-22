import csv, datetime

def convert_str_to_datetime(datetime_str):
    """
    Converts a string in the format 11/10/2019 14:05 into a datetime object.
    """
    return datetime.datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")

def convert_datetime_to_str(datetime_obj):
    """
    Converts a datetime in the format 11/10/2019 14:05 into a string.
    """
    return datetime.datetime.strftime(datetime_obj, "%d/%m/%Y %H:%M")

def write_last_log_to_csv(source_log, output):
    '''
    The function does not return anything.
    The write_last_log_to_csv function processes the csv file mail_log.csv. 
    The mail_log.csv file contains logs of username changes. 
    At the same time, the user cannot change the email, only the name.
    The write_last_log_to_csv function should select only the most recent entries 
    for each user from the mail_log.csv file and write them to another csv file. 
    In the output file, the first line should be the column headings, the same as in the source_log file.
    For some users, there is only one entry, and then only it should be written to the final file.
    '''
    with open(source_log, 'r') as source_f:
        dict_from_csv = csv.DictReader(source_f)
        result_users_list = []

        for one_dictionary in dict_from_csv:
            one_user = [one_dictionary['Email'], one_dictionary['Name'], convert_str_to_datetime(one_dictionary['Last Changed'])]
            result_users_list.append(one_user)
        result_users_list = sorted(result_users_list)

        user_mail = ''
        user_name = ''
        user_date = ''

        list_to_csv = []
        for one_list_user in result_users_list:
            if (one_list_user[0] == user_mail):
                #Duplicate
                if (one_list_user[2] > user_date):
                    #Duplicate. And date bigger
                    user_name = one_list_user[1]
                    user_date = one_list_user[2]
                    list_to_csv.pop(-1)
                    list_to_csv.append([user_name, user_mail, convert_datetime_to_str(user_date)])        
            else:
                user_mail = one_list_user[0]
                user_name = one_list_user[1]
                user_date = one_list_user[2]
                list_to_csv.append([user_name, user_mail, convert_datetime_to_str(user_date)])

        with open(output, 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerows(list_to_csv)


'''
MAIN
'''
source_file = 'mail_log.csv'
output_file = 'mail_log_wo_duplicates.csv'
write_last_log_to_csv(source_file, output_file)

