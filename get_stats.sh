for FILE in cs330e-collatz-tests/*TestCollatz.out; do
  echo {
  echo \"name\": \"$(basename $FILE -TestCollatz.out)\",
  gawk -f test_process.awk $FILE
  echo }
done

for FILE in cs330e-collatz-tests/*RunCollatz.out; do
  echo {
  echo \"name\": \"$(basename $FILE -RunCollatz.out)\",
  echo \"ntests\": $(wc -l $FILE | awk '{ print $1 }')
  echo }
done
