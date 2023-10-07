/TOTAL/ { print "\"coverage\": \"" $6 "\","}
match($0, /Ran ([0-9]+) tests/, a) {print "\"tests\": " a[1] ","}
END { print "\"dummy\": 2" }
