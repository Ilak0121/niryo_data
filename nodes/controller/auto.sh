#press ctrl-z and kill it to terminate
for i in {92..100}
do
    count="collision_MJ${i}"
    python3 controller.py -t "${count}'s test" -d 11 -f "${count}"
done
