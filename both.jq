map([try {name: .name1 | join(" "), tests, coverage, ntests, bonus},
  try {name: .name2 | join(" "), tests, coverage, ntests, bonus}]) | add
