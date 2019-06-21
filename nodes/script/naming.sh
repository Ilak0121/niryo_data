read -p "name:" name
for i in {1..100}
do
    mv "./tmp/${name}.${i}.csvt" "./tmp/${name}.${i}.csv"
done
