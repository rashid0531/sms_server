class sms:
    """
    A simple class that adjusts ....

    """

    def __init__ (self,data):
        """
        Constructor to set the initial value passsed as parameter.
        :param data: [string] data
        """
        self._sms_data = data

    # Getter and Setter methods to encapsulate the private data.
    def get_sms_data(self):

        return self._sms_data

    def set_sms_data(self,data):

        self._sms_data = data

    def adjust_sms(self,threshold):
        """
        This function splits the sms data if the length of the sms exceeds a certain threshold (passed as parameter).
        The exceeded parts of the sms are then sent in the next consequent text messages.
        :param threshold: the value which represents the limit of characters which each sms is allowed to contain at max.
        :return: ?????????
        """

        individual_words_in_sms_data = self._sms_data.split(" ")
        list_of_flags = list(map(lambda x: check_length(x,threshold),individual_words_in_sms_data))
        if sum(list_of_flags) > 0:
            print("Your word exceeds the maximum number of characters allowed to be sent as sms")

        else:

            limit = threshold

            string_to_be_sent_in_one_sms = ""

            array_of_sms = []

            for each in individual_words_in_sms_data:

                if (len(each + " ") < limit):
                    limit -= len(each + " ")
                    string_to_be_sent_in_one_sms += each + " "

                else:
                    array_of_sms.append(string_to_be_sent_in_one_sms)
                    string_to_be_sent_in_one_sms = ""
                    string_to_be_sent_in_one_sms += each + " "



            print(array_of_sms)


def check_length(data,length):
    if len(data) <= length:
        return 0
    else:
        return 1

if __name__ == "__main__":

    string_taken_as_input = input("Enter the string that will be sent as sms : \n")
    ob1kenobi = sms(string_taken_as_input)
    ob1kenobi.adjust_sms(10)
