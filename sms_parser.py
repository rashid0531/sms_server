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


def get_sms(d, K):
    """
    Try and make it as simple as possible. Added this method to solve the problem
    But you can fintune the variables and try and make it testable or use similar
    ideas for your methods

    Testing
    ========
    Test for varying number of SMS e.g. message with varying length
    Test that the method accepts only Strings for :d
    Test that the method accepts only integers for K
    Test for special chars in message
    Test that -1 is returned when K is less than one word (means cannot divide message)

    :param d: (str) The Message to divide
    :param K: (int) The length of letters per SMS
    :return: (str) Array of SMS and number of divisions
    """
    smsdata = []
    sms = ""
    words = d.split(" ")

    for word in words:
        if len(word) > K:
            return -1

        # Sample exception used in your test for K as integer
        # In your test you can do something like:
        # with self.assertRaises(TypeError):
        #   getSMS("fake SMS", 2)

        if not isinstance(K, int):
            raise TypeError("K must be an Integer")

        if len(sms.strip()) + len(word) <= K:
            sms += word + " "
        else:
            smsdata.append(sms.strip())
            sms = word + " "

    smsdata.append(sms.strip())
    print(smsdata)
    return 'Number of SMS is {}'.format(len(smsdata))

if __name__ == "__main__":

    # string_taken_as_input = input("Enter the string that will be sent as sms : \n")
    # ob1kenobi = sms(string_taken_as_input)
    # ob1kenobi.adjust_sms(10)

    print(get_sms("This is a very long SMS to send", 4))
