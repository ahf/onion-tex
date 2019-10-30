import csv
import sys
import itertools

if __name__ == '__main__':
    result = []

    with open(sys.argv[1]) as f:
        reader = csv.reader(f, delimiter=',')

        for data in reader:
            # Skip first values.
            skip = False

            if data[0].startswith("#"):
                skip = True

            if data[0] == "date":
                skip = True

            if skip:
                continue

            date = data[0]

            if len(data) < 3:
                advbw = 0
            else:
                if data[3] == '':
                    advbw = 0
                else:
                    advbw = float(data[3])

            if len(data) < 4:
                bwhist = 0
            else:
                if data[4] == '':
                    bwhist = 0
                else:
                    bwhist = float(data[4])

            result.append((date, advbw, bwhist))

    print("date,advbw,bwhist")
    for key, group in itertools.groupby(result, lambda x: x[0]):
        advbw_sum  = 0
        bwhist_sum = 0

        for date, advbw, bwhist in group:
            advbw_sum += advbw
            bwhist_sum += bwhist

        if advbw_sum == 0.0:
            advbw_value = ""
        else:
            advbw_value = "%f" % advbw_sum

        if bwhist_sum == 0.0:
            bwhist_value = ""
        else:
            bwhist_value = "%f" % bwhist_sum

        print("%s,%s,%s" % (key, advbw_value, bwhist_value))
