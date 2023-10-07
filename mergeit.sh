for FILE in submissions/*; do
  echo [\"$(basename $FILE .json | cut -d_ -f1)\",
  cat $FILE
  echo ]
done
