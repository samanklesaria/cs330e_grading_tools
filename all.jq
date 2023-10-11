try {
 name: ."Project #1"."GitLab Username",
 bonus: ."Project #1"."Completed Sphere Challenge",
 uri: ."Project #1"."GitLab URL" | match("gitlab.com/([^/]+)/(.+)") |
    .captures | map(.string) | join("%2F"),
 name1: ([
   ."Project #1"."Member #1 First Name",
   ."Project #1"."Member #1 Last Name"] | join(" ")),
 name2: (try [
  ."Project #1"."Member #2 First Name",
  ."Project #1"."Member #2 Last Name"] | join(" "))
}
