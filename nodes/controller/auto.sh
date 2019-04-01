#press ctrl-z and kill it to terminate
for i in {85..100}
do
    count="normal${i}"
    python3 controller.py -t "${count}'s test" -d 11 -f "${count}"
done
