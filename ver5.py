import csv


def auto():

    #######################################################################################

    # Calculator for geek bits with right input

    def days_to_target(current_geekbits, target_score, current_streak):
        days = 0
        while current_geekbits < target_score:
            current_geekbits += 1  # Earn one Geek Bit per day
            current_streak += 1
            days += 1
            if current_streak == 8:  # If you solve problems for 8 consecutive days
                current_geekbits += 8  # Get 8 additional Geek Bits
                current_streak = 0  # Reset the streak
        return days

    #######################################################################################

    def writeToCsv(current_geek_bits, consecutive_days):
        with open(
            "/home/nigmu/NPersonal/Projects/GFG geekbits calculator/testfile.csv",
            "w",
            newline="",
        ) as f:
            writer = csv.writer(f)

            writer.writerow(["Current Geek Bits", "Current no of continuous days"])
            writer.writerow([current_geek_bits, consecutive_days])

            print("Data Updated")

    #######################################################################################################33

    def readFromCsv():
        with open(
            "/home/nigmu/NPersonal/Projects/GFG geekbits calculator/testfile.csv", "r"
        ) as g:
            data = csv.reader(g)
            next(data)
            gb, cd = next(data)

        print("Data read")

        return int(gb), int(cd)

    ###################################################################################################################
    def check():
        completion_status = input(
            "Did you complete today's Problem of the Day? (y/n): "
        ).lower()

        target_geek_bits = 210

        gb, cd = readFromCsv()

        if completion_status == "y":

            # increment of value here
            gb = gb + 1
            cd = cd + 1

            if cd == 8:
                gb = gb + 8
                cd = 0

            writeToCsv(gb, cd)
            days_required = days_to_target(gb, target_geek_bits, cd)

            print(f"Congratulations! You now have {gb} Geek Bits.")
            print(
                f"Number of days needed to reach {target_geek_bits} Geek Bits: {days_required}"
            )

        else:
            cd = 0
            days_required = days_to_target(gb, target_geek_bits, cd)
            writeToCsv(gb, cd)
            print(f"No worries! Try again tomorrow. You now have {gb} Geek Bits.")
            print(
                f"Number of days needed to reach {target_geek_bits} Geek Bits: {days_required}"
            )

    ##################################################################################################

    check()


###########################################################################################
auto()
