#press ctrl-z and kill it to terminate
for i in {1..7}
do
    count="attack${i}"
    python3 controller.py -t "${count}'s test" -d 11 -f "${count}"
done
